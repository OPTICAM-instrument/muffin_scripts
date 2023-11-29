import os
import sys
import datetime
import logging
import subprocess
#%%
def create_directories(username, hostname, remote_folder_path, folder_name):
    try:
        # Create list of targets (directories) in mini-pc
        dirlist_command = f'ssh {username}@{hostname} ls {remote_folder_path}'
        print(dirlist_command)
        ex_dirlist = os.popen(dirlist_command).read()
        
        # Make directory per target in pc
        dirlist_spl = ex_dirlist.split('\n')[:-1] # Remove last in list since it is ''
        for i in range(len(dirlist_spl)): dirlist_spl[i] = folder_name + dirlist_spl[i]
        dirlist = str(dirlist_spl).translate({ord(i): None for i in '[],'})
        
        for i in range(len(dirlist_spl)):
            try:
                cdirs_command = f'mkdir {dirlist[i]}'
                print(cdirs_command)
                ex_cdirs = subprocess.run(['mkdir', f'{dirlist[i]'],
                                          capture_output=True, text=True, check=True)
                print(f'Directory {dirlist[i]} succesfully created')
                logging.info(f'Directory {dirlist[i]} succesfully created'')
                             
            except Exception as err:
                print(f'Failed to create directory, {dirlist[i]} already exists')
                error = err.stderr.strip()
                logging.error(f'{error}')
        
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f'{e}')
        
def transfer_folder(hostname, username, remote_folder_path, local_destination):
    try:
        # Transfer the compressed file to the local machine using scp
        scp_command = f'scp -r {username}@{hostname}:{remote_folder_path} {local_destination}'
        print(scp_command)
        ex_transf = os.system(scp_command)
        
        if ex_transf == 0:
            print(f"Folder '{remote_folder_path}' transferred successfully")
            logging.info(f'Ran command "{scp_command}" succesfully')
        else:
            print(f'Problem copying folder {remote_folder_path}')
            logging.error('Command "{ex_transf}" did not execute succesfully')
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f'{e}')
        
def compress_local_folder(local_file_path, local_destination):

    try:
        # Compress the folder on the remote machine
        compress_command = f'tar -czf {local_file_path} {local_destination[:-3]}'
        print(compress_command)
        ex_complf = os.system(compress_command)
        
        if ex_complf == 0:
            print(f"Folder '{local_file_path}' compressed successfully.")
            logging.info(f'Ran command "{compress_command}" succesfully')
        else:
            print(f'Problem compressing folder {local_file_path}')
            logging.error(f'Command "{ex_complf}" did not execute succesfully')
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f'{e}')

def remove_local_folder(local_destination):
    # Remove the folder on the local machine
    try:
        # Check succes of compression seperately
        if ex_complf == 0: # Compression succesfull
            rm_loc_command = f'rm -r {local_destination[:-3]}'
            ex_rmlf = os.system(rm_loc_command)
            
            print(f"Folder '{local_destination[:-3]}' removed successfully.")
                
    except Exception as e:
        print(f"Error: {e}")
        logging.error(f'{e}')
        
def remove_remote_folder(hostname, username, remote_folder_path, local_file_path):
    try:
        # Remove the folder on the remote machine
        if os.path.exists(local_file_path) and ex_transf == 0 and ex_complf == 0:
            rm_rem_command = f'ssh {username}@{hostname} "rm -rf {remote_folder_path}"'
            print(rm_rem_command)
            ex_rmrf = os.system(rm_rem_command)

            print(f"Folder '{remote_folder_path}' removed successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder name>")
        sys.exit(1)

    # use datetime to determine the day of the previous night
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    observing_night = yesterday.strftime("%Y-%m-%d")

    # use the day of the starting night to determine the folder name
    # check if the folder exist if not create it
    folder_name = f'/backup_images/opticam/{observing_night}/'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        # report it
        print(f"Folder '{folder_name}' created successfully.")
        
    # Create log file for process tracking
    logging.basicConfig(filename=f'{folder_name}data_transfer.log',
                        level=logging.DEBUG, format='[%(asctime)s]%(levelname)s: %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S')
    remote_folder = sys.argv[1]
    # check if foldn has the / at the end. If it does, remove it
    if remote_folder[-1] == '/':
        remote_folder = remote_folder[:-1]

    for cam in [1, 2, 3]:
        hostname = f'10.0.0.{cam}'
        username = f'opticamc{cam}'
        remote_folder_path = f'/images/opticamc{cam}/{remote_folder}'
        local_file_path = f'{folder_name}{remote_folder}.tar.gz'
        local_destination = f'{folder_name}{remote_folder}/{remote_folder}_c{cam}'

        # Run the function
        logging.info(f'Start of run for c{cam}')
        create_directories(username, hostname, remote_folder_path, folder_name)
        transfer_folder(hostname, username, remote_folder_path, local_destination)
        compress_local_folder(local_file_path, local_destination)

        #remove_local_folder(local_destination)
        #remove_remote_folder(hostname, username, remote_folder_path, local_file_path)
        logging.info(f'End of run for c{cam}')
    logging.info(f'End of script run\n')

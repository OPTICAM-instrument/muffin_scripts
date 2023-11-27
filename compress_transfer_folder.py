import os
import sys
import datetime


def compress_and_transfer_folder(hostname, username, remote_folder_path, local_destination):
    try:
        # Compress the folder on the remote machine
        compressed_filename = remote_folder_path.rstrip('/') + '.tar.gz'
        compress_command = f'ssh {username}@{hostname} "tar -czf {compressed_filename} {remote_folder_path}"'
        os.system(compress_command)

        # Transfer the compressed file to the local machine using scp
        scp_command = f'scp {username}@{hostname}:{compressed_filename} {local_destination}'
        os.system(scp_command)

        # Delete the compressed folder on the remote machine
        ssh_delete_command = f'ssh {username}@{hostname} "rm {compressed_filename}"'
        os.system(ssh_delete_command)

        print(f"Folder '{remote_folder_path}' compressed and transferred successfully.")

    except Exception as e:
        print(f"Error: {e}")

def trasnfer_folder(hostname, username, remote_folder_path, local_destination):
    try:
        # Transfer the compressed file to the local machine using scp
        scp_command = f'scp -r {username}@{hostname}:{remote_folder_path} {local_destination}'
        print(scp_command)
        ex = os.system(scp_command)

        print(f"Folder '{remote_folder_path}' transferred successfully. exit with{ex}")

    except Exception as e:
        print(f"Error: {e}")

def compress_local_folder(local_file_path, local_destination):

    try:
        # Compress the folder on the remote machine
        compress_command = f'tar -czf {local_file_path} {local_destination}'
        print(compress_command)
        os.system(compress_command)

        print(f"Folder '{local_folder_path}' compressed successfully.")

    except Exception as e:
        print(f"Error: {e}")

def remove_local_folder(local_folder_path):
    try:
        # Compress the folder on the remote machine
        compress_command = f'rm -r {local_folder_path}'
        os.system(compress_command)

        print(f"Folder '{local_folder_path}' removed successfully.")

    except Exception as e:
        print(f"Error: {e}")

def remove_remote_folder(hostname, username, remote_folder_path):
    try:
        # Compress the folder on the remote machine
        compress_command = f'ssh {username}@{hostname} "rm -rf {remote_folder_path}"'
        os.system(compress_command)

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
    observing_night = today.strftime("%Y-%m-%d")

    # use the day of the starting night to determine the folder name
    # check if the folder exist if not create it
    folder_name = f'/backup_images/opticam/{observing_night}/'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        # report it
        print(f"Folder '{folder_name}' created successfully.")

    remote_folder = sys.argv[1]
    # check if foldn has the / at the end if it does remove it
    if remote_folder[-1] == '/':
        remote_folder = remote_folder[:-1]

    for cam in [1, 2, 3]:
        hostname = f'10.0.0.{cam}'
        username = f'opticamc{cam}'
        remote_folder_path = f'/images/opticamc{cam}/{remote_folder}'
        local_file_path = f'{folder_name}{remote_folder}_c{cam}.tar.gz'
        local_destination = f'{folder_name}{remote_folder}_c{cam}'

        # Run the function
        # compress_and_transfer_folder(hostname, username, remote_folder_path, local_destination)
        trasnfer_folder(hostname, username, remote_folder_path, local_destination)
        compress_local_folder(local_file_path, local_destination)

        #remove_local_folder(local_destination)
        #remove_remote_folder(hostname, username, remote_folder_path)


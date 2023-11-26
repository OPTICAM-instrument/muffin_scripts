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


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder name>")
        sys.exit(1)

    # use datetime to determine the day of the starting night
    today = datetime.date.today()
    today = today.strftime("%Y-%m-%d")

    # use the day of the starting night to determine the folder name
    # check if the folder exist if not create it
    folder_name = f'/images/{today}/
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        # report it
        print(f"Folder '{folder_name}' created successfully.")

    # Replace these variables with your own values
    for cam in [1, 2, 3]:
        hostname = f'10.0.0.{cam}'
        username = f'opticamc{cam}'
        remote_folder_path = f'/images/opticamc{cam}/{sys.argv[1]}'
        local_destination = f'{folder_name}{sys.argv[1].rstrip("/").replace("/", "_")}_c{cam}.tar.gz'

        # Run the function
        compress_and_transfer_folder(hostname, username, remote_folder_path, local_destination)

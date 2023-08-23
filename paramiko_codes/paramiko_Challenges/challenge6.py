import paramiko
import time
import os
from dotenv import load_dotenv
import pathlib


# Get the current directory of the script
current_directory = pathlib.Path(__file__).parent.absolute()
# Go up two directories to the root folder and join with the .env filename
env_path = current_directory.parent.parent/'credentials.env'

# Load the .env file
load_dotenv(dotenv_path=env_path)

# Access the environment variable
user = os.getenv('CISCO_USER')
password = os.getenv('CISCO_PASS')

# creating an ssh client object
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router = {'hostname': '192.168.122.10', 'port': '22', 'username': user, 'password': password }


print('Connecting to 192.168.122.10')
ssh_client.connect(**router,
                   look_for_keys=False, allow_agent=False)


shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show ip int brief\n')
time.sleep(1)

output = shell.recv(100000).decode()
print(output)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()

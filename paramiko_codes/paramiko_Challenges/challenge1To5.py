# Create a Python script that connects to a Cisco Router using SSH and Paramiko. 
# Ask user for the SSH password securely
# The script should execute the show users command in order to display the logged-in users.
# Print out the output of the command.

import paramiko
import time
import getpass
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

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

passwd = getpass.getpass('Enter your ssh password: ')

router = {'hostname': '192.168.122.10', 'port': '22', 'username': user, 'password': f'{passwd}' }
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()

shell.send('terminal length 0\n')
shell.send('enable\n')
shell.send(f'{passwd}\n')
shell.send('show users\n')
time.sleep(1)

output = shell.recv(10000).decode()

with open('../paramiko_Challenges/challenge.txt', 'w') as f:
    f.write(output)
    print('File created')

#Task 5
shell.send('show running-config\n')
time.sleep(1)
output = shell.recv(10000).decode()
#print(output)
with open('../paramiko_Challenges/challenge2.txt', 'w') as f:
    f.write(output)
    print('File created')

#print(output)

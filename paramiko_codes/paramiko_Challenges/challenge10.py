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


#Open and read commands into a list
with open('../paramiko_Challenges/commands.txt', 'r') as f:
    cmds = f.read()
#Split the lines up in to a list
commands = cmds.splitlines()
print(commands)

shell = ssh_client.invoke_shell()

for cmd in commands:
    shell.send(f'{cmd}\n')
    time.sleep(0.5)

output = shell.recv(10000).decode()
print(output)



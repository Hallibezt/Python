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
ssh_client.connect(**router,
                   look_for_keys=False, allow_agent=False)


shell = ssh_client.invoke_shell()

# the second element (cisco) is the enable command
commands = ['enable', password, 'conf t', 'username admin1 secret cisco', 'access-list 1 permit any', 'end',
            'terminal length 0',  'sh run | i user']


for cmd in commands:
    print(f'Sending command: {cmd}')
    shell.send(f'{cmd}\n')
    time.sleep(0.5)

output = shell.recv(100000)
# decoding from bytes to string
output = output.decode()
print(output)


if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()
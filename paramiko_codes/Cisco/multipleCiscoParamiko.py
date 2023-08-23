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


#Create a ssh client, like putty
ssh_client = paramiko.SSHClient()

#Accept the host key before
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


#get admin password to connect to the remote device
password = getpass.getpass('Enter Password')

#if connection to device using json or dictionaries - **kwargs (keyword arguments) is used to call the dictonary items like key=value
router1 = {'hostname': '192.168.122.10', 'port': '22', 'username': user, 'password': password }
router2 = {'hostname': '192.168.122.20', 'port': '22', 'username': user, 'password': password }
router3 = {'hostname': '192.168.122.30', 'port': '22', 'username': user, 'password': password }

#python list to include above dictionaries
routers = [router1, router2, router3]

for router in routers:
    print(f'connecting to {router["hostname"]}')
    #** means passing a dictionary
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    #Create a shell object
    shell = ssh_client.invoke_shell()
    shell.send('enable\n')
    shell.send(f'{password}\n')
    time.sleep(1)
    shell.send('terminal length 0\n')
    shell.send('conf t\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('show ip protocols\n')
    time.sleep(2)

    output = shell.recv(10000).decode()
    print(output)



    #If connection is open, then close
    if ssh_client.get_transport().is_active() == True:
        print('closing connection...')
        ssh_client.close()
        print('connection closed')
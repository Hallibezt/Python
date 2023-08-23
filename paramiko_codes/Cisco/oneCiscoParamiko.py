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

#connect - ath look_for_keys is for public key authentication - allow_agent is a ssh keeping clear text key in the RAM
#print('connecting to 192.168.122.10')
#ssh_client.connect(hostname='192.168.122.10', port='22', username='halli', password='halli',
#                  look_for_keys= False, allow_agent= False)

#get admin password to connect to the remote device
password = getpass.getpass('Enter Password')
#if connection to device using json or dictionaries - **kwargs (keyword arguments) is used to call the dictonary items like key=value
router = {'hostname': '192.168.122.10', 'port': '22', 'username': user, 'password': password }
print(f'connecting to {router["hostname"]}')
#** means passing a dictionary
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

#Create a shell object
shell = ssh_client.invoke_shell()
#Send commands to remote devices ath \n is eaqual to pressing enter after the command on the device shell
shell.send('terminal length 0\n') #Make shure that the cisco terminal prints everything to the shell, not just part
shell.send('show version\n')
time.sleep(1) #give remote device time to digest and return

#get the shell response as bytes
output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

#If connection is open, then close
if ssh_client.get_transport().is_active() == True:
    print('closing connection...')
    ssh_client.close()
    print('connection closed')
from netmiko import ConnectHandler
import os
from dotenv import load_dotenv
import pathlib


# Get the current directory of the script
current_directory = pathlib.Path(__file__).parent.absolute()
# Go up two directories to the root folder and join with the .env filename
env_path = current_directory.parent/'credentials.env'

# Load the .env file
load_dotenv(dotenv_path=env_path)

# Access the environment variable
user = os.getenv('UBUNTU_VM_USER')
password = os.getenv('UBUNTU_VM_PASS')

linux = {
    'device_type': 'linux',
    'host': '192.168.122.237',
    'username': user,
    'password': password,
    'port': '22',
    'secret': password, #sudo password - Netmiko uses sudo su
    'verbose': True,
    'global_delay_factor': 8  #Delay multiplier for netmiko, 2 means - 2 times longer then the normal, 0.5 2x faster etc
    }

connection = ConnectHandler(**linux) 
connection.enable() #Getting sudu su

output = connection.send_command('apt update && apt install -y apache2')


#To troubleshoot netmiko this is very important - use a logger
import logging
logging.basicConfig(filename='testLogger.log', level=logging.DEBUG)
logger = logging.getLogger('netmiko')
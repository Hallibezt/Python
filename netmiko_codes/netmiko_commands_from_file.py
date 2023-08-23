''' from netmiko import Netmiko

#https://github.com/ktbyers/netmiko Good resource on Netmiko (for device type look at https://github.com/ktbyers/netmiko/blob/develop/netmiko/ssh_dispatcher.py)
connection = Netmiko(host='192.168.122.10', port='22', username='halli', password='halli', device_type = 'cisco_ios')


'''

#Another way to connect with a dictonary
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
user = os.getenv('CISCO_USER')
password = os.getenv('CISCO_PASS')

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.10',
    'username': user,
    'password': password,
    'port': '22',
    'secret': password,
    'verbose': True
    }

#Connection is startded in non-priv mode = '>'
connection = ConnectHandler(**cisco_device)
print('Entering enable mode.....')
connection.enable()

print('sending commands from file....')
config_path = os.path.join('netmiko_codes', 'ospf.txt')

connection.send_config_from_file(config_path)


print('closing connection....')
connection.disconnect()
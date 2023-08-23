''' from netmiko import Netmiko

#https://github.com/ktbyers/netmiko Good resource on Netmiko (for device type look at https://github.com/ktbyers/netmiko/blob/develop/netmiko/ssh_dispatcher.py)
connection = Netmiko(host='192.168.122.10', port='22', username='halli', password='halli', device_type = 'cisco_ios')


'''
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

#Another way to connect with a dictonary
from netmiko import ConnectHandler
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
#Find the priv mode
prompt = connection.find_prompt()
print(prompt)

#We can use if statement to move to priv mode
if '>' in prompt:
    #Get admin access to the device
    connection.enable() 
    # Now the priv mode has changed to '#'
    prompt = connection.find_prompt()
    print(prompt)

#Check if we are in configure mode or enable mode
if not connection.check_config_mode():
    connection.config_mode()

print(connection.check_config_mode())

connection.send_command('username u3 secret cisco')

#Check if we are in configure mode or enable mode
if connection.check_config_mode():
    connection.exit_config_mode()
#output = connection.send_command('sh ip int brief')
output = connection.send_command('sh run | include user') #admin command

#Classical approach for list of commands is using a for loop, like with paramiko
#but better way in Netmiko as special method



print(output)
connection.disconnect()
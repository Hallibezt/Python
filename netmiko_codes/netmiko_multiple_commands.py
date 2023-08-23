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
    'password': user,
    'port': '22',
    'secret': password,
    'verbose': True
    }

#Connection is startded in non-priv mode = '>'
connection = ConnectHandler(**cisco_device)
print('Entering enable mode.....')
connection.enable()



#commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']

#We can also send commands as one string instead of a list like above, by using a separator e.g. ';'
commands2 = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'

#We can also use '\n' as our separator if we want like one command per line layout
commands3 = '''ip ssh version 2
access-list 1 permit any
ip domain-name net-auto.io
'''

#This enters the config mode and then enters back to enable mode automatically
#output = connection.send_config_set(commands) #Here we pass our list of commands
#output = connection.send_config_set(commands2.split(';')) #Here we use the normal string list of commands and separator split
output = connection.send_config_set(commands3.split('\n')) #Here we use string, one command per line and '\n' separator
print(connection.find_prompt())

print(output)

connection.send_command('wr mem')

print('closing connection....')
connection.disconnect()
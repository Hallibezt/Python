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

device_path = os.path.join('netmiko_codes', 'devices.txt')

with open(device_path) as f:
    devices = f.read().splitlines()

device_list = list()

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': user,
        'password': password,
        'port': '22',
        'secret': password,
        'verbose': True
    }
    device_list.append(cisco_device)

#print(device_list)
#exit(1)

for device in device_list:
    connection = ConnectHandler(**device)

    print('entering enable mode.....')
    connection.enable()

    file = input(f'Enter a configuration file (use a valid path) for {device["host"]}: ')
    file = os.path.expanduser(file)  # This line expands the ~ to the user's home directory, else python does not recognize ~
    
    print(f'Running commands from file: {file} on device: {device["host"]}')
    output = connection.send_config_from_file(file)
    print(output)

    print(f'Closing connection to {device["host"]}')
    connection.disconnect()

    print('#' * 30)

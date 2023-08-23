from netmiko import ConnectHandler
from datetime import datetime
import threading
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

def backup(device):
    connection = ConnectHandler(**device)
    connection.enable()

    output = connection.send_command('show run')
    
    #Create the filename for the backup file
    prompt = connection.find_prompt()
    hostname = prompt[0:-1] #Skip the last element '#'

    #Configure the backupfile
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    
    filename = os.path.join('netmiko_codes', f'{hostname}-backup_{year}-{month}-{day}.txt')
    with open(filename,'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')
        print('#' * 30)

   
    print(f'Closing connection to {device["host"]}')
    connection.disconnect()



device_path = os.path.join('netmiko_codes', 'devices.txt')
with open(device_path) as f:
    devices = f.read().splitlines()

threads = list()

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
   # backup(cisco_device) the for loop calling the backup function. Slower.
    th = threading.Thread(target=backup, args=(cisco_device,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

#print(device_list)
#exit(1)



#Much faster to use multithreading (multiple processes at once) then a single process pyton script
import threading
import myParamikoModul
import getpass
from datetime import datetime
import os
from dotenv import load_dotenv
import pathlib


def backup(router):
    client = myParamikoModul.connect(**router)
    shell = myParamikoModul.get_shell(client)

    myParamikoModul.send_command(shell, 'terminal length 0')
    myParamikoModul.send_command(shell, 'enable')
    myParamikoModul.send_command(shell, f'{password}')
    myParamikoModul.send_command(shell, 'show run')

    output = myParamikoModul.show(shell)


    #Now clean the output to have just the settings needed to copy/paste the backup to cisco
    output_list = output.splitlines()
    output_list = output_list[9:-1] #-1 means last element excluded, so basically from element 10 to second last we keep
    #print(output_list)
    #Can not write list to file, have to change to string first so use join
    output = '\n'.join(output_list) #This joins the elements and add  \n between them
    #print(output)

    #Configure the backupfile
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    filename = f'{router["server_IP"]}_{year}-{month}-{day}.txt'
    #save to backupfile
    with open(filename, 'w') as f:
        f.write(output)
    
    myParamikoModul.close(client)

# Get the current directory of the script
current_directory = pathlib.Path(__file__).parent.absolute()
# Go up two directories to the root folder and join with the .env filename
env_path = current_directory.parent.parent/'credentials.env'

# Load the .env file
load_dotenv(dotenv_path=env_path)

# Access the environment variable
user = os.getenv('CISCO_USER')

password = getpass.getpass('Enter your password')

#if connection to device using json or dictionaries - **kwargs (keyword arguments) is used to call the dictonary items like key=value
router1 = {'server_IP': '192.168.122.10', 'server_port': '22', 'user': user, 'passwd': password }
router2 = {'server_IP': '192.168.122.20', 'server_port': '22', 'user': user, 'passwd': password }
router3 = {'server_IP': '192.168.122.30', 'server_port': '22', 'user': user, 'passwd': password }

#python list to include above dictionaries
routers = [router1, router2, router3]

threads = list()

#Create and define the threads, add them to list
for router in routers:
    #First choose the target function, no call so no (), then the arguments - because they should be tuple we use , when we have just router (one arg)
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

#start all the threads
for th in threads:
    th.start()

#Make the main program to wait for all thread processes to finish before ending
for th in threads:
    th.join()
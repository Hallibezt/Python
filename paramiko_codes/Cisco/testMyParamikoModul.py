import myParamikoModul
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
LUser = os.getenv('USER')



password = getpass.getpass('Please enter your password: ')

client = myParamikoModul.connect('192.168.122.10', '22', user, password)
shell = myParamikoModul.get_shell(client)

myParamikoModul.send_command(shell, 'enable')
myParamikoModul.send_command(shell, password)
myParamikoModul.send_command(shell, 'term len 0')
myParamikoModul.send_command(shell, 'sh version')
myParamikoModul.send_command(shell, 'sh ip int brief')

#print(myParamikoModul.show(shell))

myParamikoModul.close(client)

Lpass = getpass.getpass(f'Please enter your admin password for user {LUser}: ')
client = myParamikoModul.connect('127.0.0.1','22', LUser, Lpass)
shell = myParamikoModul.get_shell(client)
myParamikoModul.send_command(shell, 'sudo userdel u2')
myParamikoModul.send_command(shell, Lpass)
myParamikoModul.send_command(shell, 'cat /etc/passwd')

print(myParamikoModul.show(shell))

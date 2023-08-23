from .. import myParamikoModul
import getpass

admin = input('Please enter your username: ')
password = getpass.getpass('Please enter your password')

ssh_client = myParamikoModul.connect('127.0.0.1', '22', admin, password)
shell = myParamikoModul.get_shell(ssh_client)
user = input('Please enter the username to add: ')
myParamikoModul.send_command(shell, f'sudo useradd -m -d /home/{user} -s /bin/bash {user}')
myParamikoModul.send_command(shell, f'{password}')
if input('Would you like to see the passwd file? ').lower() == 'y':
   users = myParamikoModul.send_command(shell, 'cat /etc/passwd')
   print(myParamikoModul.show(shell))

myParamikoModul.close(ssh_client)
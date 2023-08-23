import paramiko
import time
import getpass


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

username = input('Please enter your username: ')
password = getpass.getpass('Please enter your password: ')
linux = {'hostname': '127.0.0.1', 'port': '22', 'username': username, 'password': password}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)


shell = ssh_client.invoke_shell()
shell.send('cat /etc/passwd\n')
time.sleep(1)

shell.send('sudo cat /etc/shadow\n')  
#Attention the password is printed in clear text in the shell output, not good
#But hard to overcome since the .invoke_shell() opens an interactive shell, 
#.exec_command() can be used in stead but it is non-interactive shell, so I can
#not change shell settings, maintain environmental variables between commands.
# in exec_command() I use stdin, stdout, stderr
shell.send(f'{password}\n')
time.sleep(1)



output = shell.recv(10000)
output = output.decode('utf-8')

print(output)
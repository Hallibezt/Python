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

#When executing a command as a root we need a second argument to exec - pty=True
stdin, stdout, stderr = ssh_client.exec_command('sudo useradd u2\n', get_pty=True)
stdin.write(f'{password}\n')
time.sleep(2)



stdin, stdout, stderr = ssh_client.exec_command('cat /etc/passwd\n', get_pty=True)
print(stdout.read().decode())
time.sleep(1)


if ssh_client.get_transport().is_active() == True:
    print('Closing Connection')
    ssh_client.close()
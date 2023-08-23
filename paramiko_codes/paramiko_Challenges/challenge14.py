import paramiko
import time


#First function - Connect
def connect(server_IP, server_port, user, passwd):
    #Create a ssh client
    ssh_client = paramiko.SSHClient()
    #Accept the all host keys to ~/.ssh/known_hosts
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'connecting to {server_IP}')
    #connect, look_for_keys mean if private keys for authentication are used and allow_agent is to let host ssh to get private keys
    ssh_client.connect(hostname=server_IP, port=server_port, username=user, password=passwd, look_for_keys=False, allow_agent=False)

    return ssh_client

def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell

def send_command(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)

def show(shell, n=10000):
    output = shell.recv(n)
    output = output.decode('utf-8')
    return output

def close(ssh_client):
    if ssh_client.get_transport().is_active() == True:
        print('Closing connection')
        ssh_client.close()

def send_from_list(shell,commands):
    for cmd in commands:
        send_command(shell, cmd)

def send_from_file(shell,file):
    #Open and read commands into a list
    with open(file, 'r') as f:
        cmds = f.read()
    #Split the lines up in to a list
    commands = cmds.splitlines()
    for cmd in commands:
        send_command(shell, cmd)



#downder means double-under score __
if __name__ == '__main__':
    print('This is just printed if this module is run, not if if is imported my another')
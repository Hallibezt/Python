#Connect to the router, either R1 or R2. 
#Check if interface is is up or down, and if down then send 'no shut' to it
#The interface should be a user input
from netmiko import ConnectHandler
import time

def checkStatus(Interface):
    # Split the returned string into a list of words
    statusList = interfaceStatus.split()
    # The 'status' is the 6th in the list
    status = statusList[5]
    if status == 'up':
        return True
    else:
        return False

r1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.10',
    'username': 'admin',
    'password': 'cisco',
    'port': '22',
    'secret': 'cisco',
    'verbose': True
    }

r2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.20',
    'username': 'admin',
    'password': 'cisco',
    'port': '22',
    'secret': 'cisco',
    'verbose': True
    }

while True:
    router = input('Enter r1 for router R1, r2 for router R2 or exit to close: ')
    if router == 'exit':
        print('closing console.....')
        break
    interface = input('What interface to check: ')

    if router == 'r1':
        connection = ConnectHandler(**r1)
        interfaceStatus = connection.send_command(f'show ip interface brief | include {interface}')    

        if checkStatus(interfaceStatus):
            print(f'{interface} is up')
        else:
            print(f'{interface} is down and will be turned on now.....')
            connection.send_config_set([f'interface {interface}', 'no shut'])
            interfaceStatus = connection.send_command(f'show ip interface brief | include {interface}')  
            if checkStatus(interfaceStatus):
                print(f'{interface} is up')
            else:
                print(f'{interface} Error turning interface up')
        connection.disconnect()
    
    elif router == 'r2':
        connection = ConnectHandler(**r2)
        interfaceStatus = connection.send_command(f'show ip interface brief | include {interface}')    
        
        if checkStatus(interfaceStatus):
            print(f'{interface} is up')
        else:
            print(f'{interface} is down and will be turned on now.....')
            connection.send_config_set([f'interface {interface}', 'no shut'])
            time.sleep(5)     
            interfaceStatus = connection.send_command(f'show ip interface brief | include {interface}')    
            if checkStatus(interfaceStatus):
                print(f'{interface} is up')
            else:
                print(f'{interface} Error turning interface up')
        connection.disconnect()
    else:
        print('Router input not correct, enter again r1 or r2: ')
    
   
   
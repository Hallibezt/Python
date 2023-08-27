#1. Not possible to run enable command through scp, thats is why a admin user must be in place on router (user with priv level 15)
#  - conf t; username admin privilege 15 secret cisco
#2. Configure ssh
#  - ip domain-name something.com
#  - crypto key generate rsa
#  - line vty 0 ? #to see how many vty lines there are (maybe 1-1869)
#  - line vty 0 1869
#  - transport input telnet ssh #to allow ssh and telnet on all lines
#  - login local
from netmiko import ConnectHandler
from netmiko import file_transfer #scp file transfer
import os

#Another way to connect with a dictonary
from netmiko import ConnectHandler
cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.122.10',
    'username': 'admin',
    'password': 'cisco',
    'port': '22',
    'secret': 'cisco',
    'verbose': True
    }

#Connection is startded in non-priv mode = '>'
connection = ConnectHandler(**cisco_device)

config_path = os.path.join('netmiko_codes', 'ospf.txt')

#First the connection to the device, the file to transfer, name of it at destination,
#file system of destination, direction (from local == put, else pull), overwrite existing file on destination
transfer_output = file_transfer(connection, source_file=config_path, dest_file='ospf1.txt',
                                 file_system='disk0:', direction='put', overwrite_file=True)
print(transfer_output)

connection.disconnect()
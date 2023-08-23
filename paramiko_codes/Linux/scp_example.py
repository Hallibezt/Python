import paramiko
from scp import SCPClient


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
router = {'hostname': '192.168.122.237', 'port': '22', 'username': 'delpux', 'password': 'Kalldur5%1984' }
print(f'connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

scp = SCPClient(ssh_client.get_transport())

#Copy file
scp.put('../README.md', '/tmp/transferredWithParamiko.txt')

#copy directory - recursive to copy the dir and its content
#scp.put('directoryname', recursive=True, remote_path='/tmp')

#Now get from the client to the local
scp.get('/tmp/transferredWithParamiko.txt', 'fromClientSCP.txt')

scp.close()
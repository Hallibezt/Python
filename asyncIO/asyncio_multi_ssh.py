#Run multiple ssh clients in paralell and process the results when all are completed.
#E.g. multiple servers to be concurrently configured
import asyncio
import asyncssh
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
user = os.getenv('UBUNTU_VM_USER')
password = os.getenv('UBUNTU_VM_PASS')
# Access the environment variable
user_local = os.getenv('UBUNTU_USER')
password_local = os.getenv('UBUNTU_PASS')

async def run_client(host, username, password, command):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        return await connection.run(command)

async def run_multiple_clients(hosts):
    tasks = []
    for host in hosts:
        task = run_client(**host)
        tasks.append(task)
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for  i, result in enumerate(results):
        if isinstance(result, Exception):
                      print(f'Task {i} failed: {str(result)}')
        elif result.exit_status != 0:
             print(f'Task {i} exited with status: {result.exit_status}')
             print(result.stderr, end='')
        else:
             print(f'Task {i} succeeded')
             print(result.stdout, end='')
        print('#'*50)

hosts = [
      {'host': '192.168.122.237', 'username': user, 'password': password, 'command': 'ifconfig'},
      {'host': '127.0.0.1', 'username': user_local, 'password': password_local, 'command': 'sleep 10'},
      {'host': '127.0.0.1', 'username': user_local, 'password': password_local, 'command': 'ls'},
      {'host': '192.168.122.237', 'username': user, 'password': password, 'command': 'who -a'}
]

#Since asyncio.gather(*task) waits for all to complete before it returns, we can use asyncio.as_completed() to return an iterator with tasks
#as soon as they are completed
async def run_multiple_clients_as_completed(hosts):
    tasks = []
    for host in hosts:
        task = run_client(**host)
        tasks.append(task)
    
    for i, task in enumerate(asyncio.as_completed(tasks)):
        result = await task
        if isinstance(result, Exception):
            print(f'Task {i} failed: {str(result)}')
        elif result.exit_status != 0:
            print(f'Task {i} exited with status: {result.exit_status}')
            print(result.stderr, end='')
        else:
            print(f'Task {i} succeeded')
            print(result.stdout, end='')
        print('#'*50)

hosts = [
      {'host': '192.168.122.237', 'username': user, 'password': password, 'command': 'ifconfig'},
      {'host': '127.0.0.1', 'username': user_local, 'password': password_local, 'command': 'sleep 10'},
      {'host': '127.0.0.1', 'username': user_local, 'password': password_local, 'command': 'ls'},
      {'host': '192.168.122.237', 'username': user, 'password': password, 'command': 'who -a'}
]

asyncio.run(run_multiple_clients_as_completed(hosts))
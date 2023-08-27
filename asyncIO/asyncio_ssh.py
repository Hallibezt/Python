#AsyncSSH 
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

async def connect_and_run(host, username, password, commands):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        #results = await connection.run(command)
        #return results

        #2. run multiple commands
        results = []
        for cmd in commands:
            result = await connection.run(cmd)
            results.append(result)
        return results
    

commands = ('ifconfig', 'ls', 'who -a')
results = asyncio.run(connect_and_run('192.168.122.237',user, password, commands))
for result in results:
    print(f'STDOUT:\n {result.stdout}')
    print(f'STDERR:\n {result.stderr}')
    print('#' * 30)
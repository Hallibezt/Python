import myParamikoModul
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
password = os.getenv('CISCO_PASS')


router1 = {'server_ip': '192.168.122.10', 'server_port': '22', 'user': user, 'passwd': password, 'config':'ospf.txt'}

router2 = {'server_ip': '192.168.122.20', 'server_port': '22', 'user': user, 'passwd': password, 'config':'eigrp.txt'}

router3 = {'server_ip': '192.168.122.30', 'server_port': '22', 'user': user, 'passwd': password, 'config':'router3.conf'}

routers = [router1, router2, router3]

for router in routers:
    ssh_client = myParamikoModul.connect(router['server_ip'], router['server_port'],router['user'],router['passwd'])
    shell = myParamikoModul.get_shell(ssh_client)

    # Construct the relative path using os.path.join
    config_path = os.path.join('paramiko_codes', 'paramiko_Challenges', router["config"])

    myParamikoModul.send_from_file(shell, config_path)
    myParamikoModul.show(shell, 10000)

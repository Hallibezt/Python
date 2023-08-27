#Classic approach is to use OS or subprocesses moduls, but that is synchronous
import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()

    print(f'{cmd} exited with status code: {proc.returncode}')

    if stdout:
        print(f'STDOUT: \n {stdout.decode("UTF-8")}')
    
    if stderr:
        print(f'STDERR: \n {stderr.decode("UTF-8")}')

async def main(commands):
    tasks = []
    for cmd in commands:
        tasks.append(run(cmd))
    await asyncio.gather(*tasks)

#Asynch means that the other commands will all be executed, but not have to wait for the sleep 5 to finish
commands = ('ifconfig', 'ls', 'sleep 5', 'who', 'uname -a')
asyncio.run(main(commands))
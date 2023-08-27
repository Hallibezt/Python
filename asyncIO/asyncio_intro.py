import asyncio
import time

#Synchrounous function
def sync_f():
    print('one ', end='')
    time.sleep(1)
    print('two ', end='')

#Asynchrounous function
async def async_f():
    print('one ', end='')
    #Create a coroutine, then we need await - task is suspended here
    await asyncio.sleep(1)
    print('two ', end='')

#This function is the starting point for asynchrounous task - toplevel coroutine
async def main():
    #Three avaitable objects: coroutine, tasks, future
    #List tasks 
    # below is the same call tasks = [async_f(), async_f(),async_f()]
    tasks = [async_f() for _ in range(3)]
    
    #Run the task list as soon as possible
    await asyncio.gather(*tasks)

#Start the eventloop
asyncio.run(main())

#Compare the synchronous code
print('*'*30)

for _ in range(3):
    sync_f()
'''
async def f():
    pass

async def g():
    await f()  #avait moves the execution back to the eventloop until finished waiting. 
    #Here it will call f() and wait for its return and in the meantime the process is back to the evenloop
'''
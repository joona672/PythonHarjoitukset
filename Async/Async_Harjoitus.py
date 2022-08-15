import asyncio
import time




async def main_func():
    print("Start")
    task = asyncio.create_task(second_func('task 2 running'))
    await asyncio.sleep(1)
    print('finish 1')
    await task
    
    
async def second_func(msg):
    print(msg)
    await asyncio.sleep(5)
    print('finish 2')
    
    
    
asyncio.run(main_func())

    
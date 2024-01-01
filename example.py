"""
https://docs.python.org/3.11/library/asyncio-task.html
"""


import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = asyncio.create_task(
            say_after(1, 'hello'))
        
        task2 = asyncio.create_task(
            say_after(2, 'world'))
    
        print(f"started at {time.strftime('%X')}")
        await task1
        await task2
    
    print(f"finished at {time.strftime('%X')}")
    
asyncio.run(main())
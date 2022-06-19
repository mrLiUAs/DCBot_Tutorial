## DON'T Test it on Jupyter Notebook !!!!

import asyncio
import time

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def task():
    await asyncio.gather(count(), count(), count())

start = time.time()
asyncio.run(task())
print(f"executed in {time.time() - start:0.2f} seconds.")
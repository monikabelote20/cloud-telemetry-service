import asyncio
async def worker_loop():
    while True:
        await asyncio.sleep(1)

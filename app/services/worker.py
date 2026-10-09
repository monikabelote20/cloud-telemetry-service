import asyncio
async def worker_loop(stop_event: asyncio.Event):
    while not stop_event.is_set():
        await asyncio.sleep(0.1)

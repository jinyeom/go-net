import asyncio
import websockets
from time import sleep
import random

async def hello():
    async with websockets.connect("ws://localhost:8080/ws") as websocket:
        while True:
            await websocket.send("Hello from Python!")
            await websocket.send(f"Here's a random number from Python: {random.random()}")
            data = await websocket.recv()
            print("From Go server:", data)
            sleep(3)

asyncio.get_event_loop().run_until_complete(hello())
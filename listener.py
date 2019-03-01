import asyncio
import websockets
import json

users = set()

async def hello(websocket, path):
    users.add(websocket)
    print(path)
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    if users:       # asyncio.wait doesn't accept an empty list
        await asyncio.wait([user.send(json.dumps(greeting)) for user in users])

    print(f"> {greeting}")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

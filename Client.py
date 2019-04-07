import os
import websockets
import asyncio
import json


def main():

    server = input("Enter the Host you want to connect to: ")
    port = int(input("Enter the port: "))

    print("Opening a websocket connection...")
    
    async def hello():
        print('ws://'+server+':'+str(port))
        async with websockets.connect('ws://'+server+':'+str(port)) as websocket:
            print('ws://'+server+':'+str(port))
            print("Connection established")
            name = input("Name:")
            json_text = {'Name': name}
            d = json.loads(json_text)

            await websocket.send(d)

            greeting = await websocket.recv()
            print(greeting)

    asyncio.get_event_loop().run_until_complete(hello())
    
if __name__ == "__main__":
    main()
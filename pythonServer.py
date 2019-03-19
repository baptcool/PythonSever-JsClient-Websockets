import asyncio
import websockets

async def handle_message(message):
    print(message)


	## code     message is as string 


	## code

async def consumer_handler(websocket, path):
	print("IN")
	while True:
		try:
			message = await websocket.recv()
			await handle_message(message)

		except Exception:
			pass

	print("OUT")


start_server = websockets.serve(consumer_handler, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

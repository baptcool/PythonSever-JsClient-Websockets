import asyncio
import websockets
from functools import partial
from classActivity import mainly


async def handle_message(message):
   # classMainlyInstance.writeMessage(message)
	pass
async def consumer_handler(websocket, path ):
	print("IN")
	while True:
		try:
			message = await websocket.recv()
			await handle_message(message)

		except Exception:
			pass

	print("OUT")



classMainlyInstance = mainly()



#start_server = websockets.serve(consumer_handler, 'localhost', 8765)
#asyncio.new_event_loop().run_until_complete(classMainlyInstance.loope())
#asyncio.new_event_loop()


#loop1 = asyncio.new_event_loop()
#count1_1 = loop1.create_task(classMainlyInstance.loope())
#asyncio.ensure_future(websockets.serve(consumer_handler, 'localhost', 8765))
#asyncio.ensure_future(classMainlyInstance.loope())
#loop1.run_forever()


start_server = websockets.serve(consumer_handler, 'localhost', 8765)

#asyncio.get_event_loop().run_until_complete(start_server)
#asyncio.get_event_loop().run_forever()

asyncio.ensure_future(start_server)
asyncio.ensure_future(classMainlyInstance.loope())
asyncio.get_event_loop().run_forever()
import asyncio
import websockets
from functools import partial





class mainly:
    def __init__(self):
        self.message = ""
        self.flag = 0
    def writeMessage(m):
        self.message=m
        self.flag = 1


    async def loope(self):
        while True:
            print("salut")
            if self.flag == 1:
                self.flag = 0
                # un message est arrivé !!!
                # self.message pour le lire
                #code

                print(self.message)
                #code
            await asyncio.sleep(1)


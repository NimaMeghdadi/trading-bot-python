import asyncio
from kucoin.client import Client
from kucoin.asyncio import KucoinSocketManager
import numpy as np
import json
import time

api_key = '<api_key>'
api_secret = '<api_secret>'
api_passphrase = '<api_passphrase>'


async def main():
    global loop

    # callback function that receives messages from the socket
    async def handle_evt(msg):
        if msg['topic'] == '/market/ticker:ETH-USDT':
            price :int = {msg["data"]["price"]}
            #print(price)
            return price

    client = Client(api_key, api_secret, api_passphrase)

    ksm = await KucoinSocketManager.create(loop, client, handle_evt)

    # for private topics such as '/account/balance' pass private=True
    ksm_private = await KucoinSocketManager.create(loop, client, handle_evt, private=True)

    # ETH-USDT Market Ticker
    price = await ksm.subscribe('/market/ticker:ETH-USDT')
    

    while True:
        print("sleeping to keep loop open")
        await asyncio.sleep(20, loop=loop)
        



# _GOODBYE_MESSAGE = u'Goodbye'

# x = np.arange(0,np.pi*10,0.1).tolist()
# y = np.sin(x).tolist()
# data_size = len(x)
# counter = 0
# graph_size = 100

# samples = 0
# tic = time.time()

# def web_socket_do_extra_handshake(request):
#     # This example handler accepts any request. See origin_check_wsh.py for how
#     # to reject access from untrusted scripts based on origin value.

#     pass  # Always accept.


# def get_graph_data():

#     global counter,data_size,graph_size,x,y
#     global samples,tic

#     #Calculate FPS
#     samples += 1
#     if (time.time() - tic) > 2:
#         print ("FPS is : ",samples /(time.time() - tic))
#         samples = 0
#         tic = time.time()
    
#     counter += 1
#     if counter > (data_size - graph_size):
#         counter = 0

#     graph_to_send = json.dumps({
#         'x':x[counter:counter+graph_size],
#         'y':y[counter:counter+graph_size]
#     })
#     return graph_to_send

# def web_socket_transfer_data(request):
#     while True:
#         line = request.ws_stream.receive_message()
#         if line is None:
#             return
#         if isinstance(line, unicode):
#             request.ws_stream.send_message(get_graph_data(), binary=False)
#             if line == _GOODBYE_MESSAGE:
#                 return
#         else:
#             request.ws_stream.send_message(get_graph_data(), binary=True)




if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
import asyncio
from kucoin.client import Client
from kucoin.asyncio import KucoinSocketManager
from sqlalchemy import true
import websockets
import asyncio
import json
import time
import matplotlib.pyplot as plt

api_key = '<api_key>'
api_secret = '<api_secret>'
api_passphrase = '<api_passphrase>'

# fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.show()

# xdata = []
# ydata = []
# x1data = []
# y1data = []


# def update_graph():
#     ax.plot(xdata, ydata, color='g')
#     ax.plot(xdata, y1data, color='r')
    
#     ax.legend([f"Last price: {ydata[-1]}$"])

#     fig.canvas.draw()
#     plt.pause(0.1)


async def main():
    global loop
    url = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"
    
    async def handle_evt(msg):
        #kucoin
        if msg['topic'] == '/market/ticker:BTC-USDT':
            price  = msg["data"]["price"]
            timekucoin = msg["data"]["time"]
            event_time =  time.localtime(timekucoin // 1000)
            event_time = f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}"
            # print("kucoin",event_time, price)
            print("kucoin : " + event_time +" : " + price)

                # xdata.append(event_time)
                # ydata.append(int(float(price)))
                #  update_graph()
            #binance
        # x1data.append(event_time)
        # y1data.append(int(float(data['c'])))
        # update_graph()
        async with websockets.connect(url) as client:
            data = json.loads(await client.recv())['data']
            event_time = time.localtime(data['E'] // 1000)
            event_time = f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}"
            print("binance",event_time, data['c'])

    client = Client(api_key, api_secret, api_passphrase)

    ksm = await KucoinSocketManager.create(loop, client, handle_evt)

    # for private topics such as '/account/balance' pass private=True
    # ksm_private = await KucoinSocketManager.create(loop, client, handle_evt, private=True)
    # ETH-USDT Market Ticker
    await ksm.subscribe('/market/ticker:BTC-USDT')
    
    while True:
        print("sleeping to keep loop open")
        await asyncio.sleep(20, loop=loop)


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


# import websockets
# import asyncio
# import json
# import time
# import matplotlib.pyplot as plt


# fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.show()

# xdata = []
# ydata = []


# def update_graph():
#     ax.plot(xdata, ydata, color='g')
#     ax.legend([f"Last price: {ydata[-1]}$"])

#     fig.canvas.draw()
#     plt.pause(0.1)


# async def main():
#     global loop
#     url = "wss://stream.binance.com:9443/stream?streams=btcusdt@miniTicker"

#     async with websockets.connect(url) as client:
#         while True:
#             data = json.loads(await client.recv())['data']

#             event_time = time.localtime(data['E'] // 1000)
#             event_time = f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}"

#             print(event_time, data['c'])

#             xdata.append(event_time)
#             ydata.append(int(float(data['c'])))

#             update_graph()

# if __name__ == "__main__":

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())






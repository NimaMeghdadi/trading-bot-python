from client import Client
from json import loads
from datetime import datetime

import requests


class Binance(Client):
    def __init__(self, url, exchange, orderbook, lock):
        super().__init__(url, exchange)

        # local data management
        self.orderbook = orderbook[exchange]
        self.lock = lock
        self.updates = 0
        self.last_update = orderbook

    # convert message to dict, process update
    def on_message(self, message):
        data = loads(message)

        # check for orderbook, if empty retrieve
        # print(f" price : {data['c']}")

        # self.orderbook['bids'] = data['c']
        # self.orderbook[key] = data['c']
        # print(f"price {data['c']}")
        # print(self.get_snapshot().items())

        # print(f"key: {key} value: {value}")
        
        key = "Binance"
        value = data['c']
        self.orderbook[key] = value
        
        # if len(self.orderbook) == 0:
        #     for key, value in self.get_snapshot().items():
        #         self.orderbook[key] = value
        #         print(self.get_snapshot().items())

        # get lastUpdateId
    #     lastUpdateId = self.orderbook['lastUpdateId']

    #     # drop any updates older than the snapshot
    #     if self.updates == 0:
    #         if data['U'] <= lastUpdateId+1 and data['u'] >= lastUpdateId+1:
    #             self.orderbook['lastUpdateId'] = data['u']
    #             self.process_updates(data)

    #     # check if update still in sync with orderbook
    #     elif data['U'] == lastUpdateId+1:
    #         self.orderbook['lastUpdateId'] = data['u']
    #         self.process_updates(data)
    #     else:
    #         print('Out of sync, abort')

    # # Loop through all bid and ask updates, call manage_orderbook accordingly
    # def process_updates(self, data):
    #     with self.lock:
    #         # for update in data['a']:
    #         #     self.manage_orderbook('bids', update)
    #         # for update in data['a']:
    #         #     self.manage_orderbook('asks', update)
    #         self.last_update['last_update'] = datetime.now()

    # Update orderbook, differentiate between remove, update and new

    # retrieve orderbook snapshot
    def get_snapshot(self):
        r = requests.get('https://www.binance.com/api/v1/ticker?symbol=BTCUSDT&limit=1000')
        return loads(r.content.decode())
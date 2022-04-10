from client import Client
from json import loads
from datetime import datetime

import requests



class Kucoin(Client):
    def __init__(self, url, exchange, orderbook, lock):
        print("ku")
    #     super().__init__(url, exchange)

    #     # local data management
    #     self.orderbook = orderbook[exchange]
    #     self.lock = lock
    #     self.updates = 0
    #     self.last_update = orderbook

    # # convert message to dict, process update
    # def on_message(self, message):
    #     data = loads(message)
        
    #     key = "binance"
    #     value = data['c']
    #     self.orderbook[key] = value
        

    # # retrieve orderbook snapshot
    # def get_snapshot(self):
    #     r = requests.get('https://www.binance.com/api/v1/ticker?symbol=BTCUSDT&limit=1000')
    #     return loads(r.content.decode())
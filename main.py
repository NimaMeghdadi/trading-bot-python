from binance import Binance
from huobi import Huobi
from kucoin import Kucoin
from datetime import datetime

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time
# from pylive import live_plotter
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Create figure for plotting
def run(orderbooks, lock):
    # local last_update
    current_time = datetime.now()

    while True:
        try:
            # check for new update
            if orderbooks['last_update'] != current_time:
                with lock:
                    i = 2
                    # print("i =" + i)
                    for key, value in orderbooks.items():
                        
                        i= i-1
                        price = value[key]
                        print(f"{key} price: {price} i={i}")
                        if i == 0:
                            break
                    print()
                    time.sleep(0.1)
                    # plt.show()

                    # set local last_update to last_update
                    current_time = orderbooks['last_update']
            time.sleep(0.1)
        except Exception:
            pass




if __name__ == "__main__":
    # data management
    lock = threading.Lock()
    orderbooks = {
        "Binance": {},
        "Huobi": {},
        "Kucoin": {},
        "last_update": None,
    }

    # create websocket threads
    binance = Binance(
        url="wss://stream.binance.com:9443/ws/btcusdt@ticker",
        exchange="Binance",
        orderbook=orderbooks,
        lock=lock,
    )

    huobi = Huobi(
        url="wss://api.huobipro.com/ws",
        exchange="Huobi",
        orderbook=orderbooks,
        lock=lock,
    )
    
    kucoin = Kucoin(
        url="wss://ws-api.kucoin.com/endpoint",
        exchange="Kucoin",
        orderbook=orderbooks,
        lock=lock,
    )

    # start threads
    binance.start()
    huobi.start()
    # kucoin.start()

    # process websocket data
    run(orderbooks, lock)
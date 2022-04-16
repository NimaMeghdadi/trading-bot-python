from binance import Binance
from huobi import Huobi
from kucoin import Kucoin
from datetime import datetime

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import time

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
# run forever
def run(orderbooks, lock):
    # local last_update
    current_time = datetime.now()

    while True:
        try:
            # check for new update
            if orderbooks['last_update'] != current_time:
                with lock:
                    i = 2
                    for key, value in orderbooks.items():
                        i-=1
                        price = value[key]
                        print(f"{key} price: {price} wtf")
                        
                        if i == 0:
                            break
                        ani = animation.FuncAnimation(price , fig, animate, fargs=(xs, ys))
                        
                        # price = round(price, 2)
                        # Add x and y to lists
                    # plt.show()
                    print()
                    time.sleep(0.1)
                    plt.show()

                    # set local last_update to last_update
                    current_time = orderbooks['last_update']
            time.sleep(0.1)
        except Exception:
            pass

def animate(price , xs, ys):
    # Read temperature (Celsius) from TMP102
    print(orderbooks.items())
    temp_c = round(price, 2)
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)
    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')
# Set up plot to call animate() function periodically
# plt.show()


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
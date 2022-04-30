from cProfile import label
from operator import index
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('fivethirtyeight')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x = []
y = []

index = count()

def animate(i):
    
    data = pd.read_csv('data.csv')
    x=data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']
    
    plt.cla()
    
    x = x[-20:]
    y1 = y1[-20:]
    y2 = y2[-20:]
    
    ax.clear()
    plt.plot(x , y1,label = 'Binance')
    plt.plot(x , y2,label = 'Huobi')
    
    plt.xticks(rotation=45, ha='right')
    plt.title('BTC Binance vs Huobi')
    plt.ylabel('Price')
    plt.xlabel('Time')
    plt.legend(loc = 'upper left')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf() , animate, interval = 1000)

plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt
from datetime import datetime



lastPrices = {"kucoin":{'prices':[] ,'color':'blue' }  }
xLabel = []
setLegend = False
onCloseApp = False
fig = plt.figure()
plt.xticks(rotation='60')

def toggleOnCloseApp(eve):
    global onCloseApp
    onCloseApp = True
    print("onClose")

fig.canvas.mpl_connect('close_event', toggleOn CloseApp)



while onCloseApp == False:
    kucoin = float(kucoin_api.getLastPrice('BTC-USDT'))
    lastPrices['kucoin']["prices"].append(kucoin)

    # xLabel.append(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    xLabel.append(datetime.now().strftime("%H:%M:%S"))
    plt.pause(0.0001)
    
    for item in lastPrices:
        plt.plot(xLabel,lastPrices[item]["prices"],label=item,color=lastPrices[item]["color"])
    
    if setLegend == False :
        setLegend = True
        plt.legend()
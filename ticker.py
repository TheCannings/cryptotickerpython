import time
from datetime import datetime
import sys
from coinmarketcap import Market

def restart_line():
    sys.stdout.write('\r')
    sys.stdout.flush()

while True:
    coinmarketcap = Market()
    myjs = coinmarketcap.ticker('myriadcoin')
    curtime = datetime.now()
    name = myjs[0]['name']
    rank = myjs[0]['rank']
    curprice = myjs[0]['price_usd']
    onehour = myjs[0]['percent_change_1h']
    oneday = myjs[0]['percent_change_24h']
    sevenday = myjs[0]['percent_change_7d']

    restart_line()

    for x in range(30,0,-1):
        sys.stdout.write("{:%H:%M:%S %d/%m/%Y} - {} - Rank: {} - Price: {} - 1H: {:.2f}% - 24H: {:.2f}% - 1W: {:.2f}% - Refresh in {:02d}".format(curtime, name, rank, curprice, float(onehour), float(oneday), float(sevenday), x))
        sys.stdout.flush()
        time.sleep(1)
        restart_line()



    

from binance.client import Client
from pprint import pprint as p
import time

def fetchPrice():
	public = 'CmmByW3DwxkXEEJ9kUWjAbpoMH37A99ZbOAP5R54arTOWmMxXoyEjNtY62PYIXmy'
	private = 'js7tj01HsBhi6uO8jOpcj09eLrDdaL1TQmVVE29T67K38DJoCRYDJr7rs3JBZfwH'

	#interval = 60
	interval = 30
	start_time = time.time()
	time_range = 5000*interval
	 
	BTC='BTCUSDT'
	client = Client(public,private)
	#klines = client.get_historical_klines(BTC, Client.KLINE_INTERVAL_1HOUR, str(time_range)+" hour ago UTC")
	klines = client.get_historical_klines(BTC, Client.KLINE_INTERVAL_30MINUTE, str(time_range)+" min ago UTC")
	p(klines)
	timeLen = len(klines)
	f = open("price.csv",'w')
	for i in range(timeLen):
		f.write(str(klines[i][0])+",")
		f.write(klines[i][4])
		f.write("\n")
	f.close()
	f = open("now_price.txt",'w')
	f.write(klines[timeLen-1][4])
	f.close()
	 
	print("--- %s seconds ---" % (time.time() - start_time))


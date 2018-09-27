from telegram.ext import Updater
import os
from datetime import datetime
import get_price
import lstmTest
import time
#t1 = 10
#t2 = 200
a=0.5
def price(n,k,t1,t2):
	return t1+((t2-t1)/(k-1)-(k/2)*a)*n + ((n*(n+1))/2)*a


updater = Updater(token='608543581:AAGNRok7N83CHAK25dG7DzA2_ox23xd5Ys0')



dispatcher = updater.dispatcher



#dispatcher 는 이벤트 왔을때 처리해줄수 있는 객체 입니다. 



#아래와 같이 start 함수를 만들어 놓습니다. 

def trade(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text="lstm auto bot")
	now = datetime.now()
	get_price.fetchPrice()
	lstmTest.lstmStart()
#	mmtest.csRun()
	f = open("past_predict.txt",'r')
	position = f.readline().split('\n')[0]
	f.close()
	f = open("ml_predict.txt",'r')
	pre_price = f.readline().split('\n')[0]
	f.close()
	f = open("now_price.txt",'r')
	now_price = f.readline().split('\n')[0]
	f.close()
	bot.send_message(chat_id=update.message.chat_id, text="predicted position: " + str(position))
	bot.send_message(chat_id=update.message.chat_id, text="predicted price@binance: " + str(pre_price))
	bot.send_message(chat_id=update.message.chat_id, text="now price@binance: " + str(now_price))


	
def calc(bot, update,args):
	bot.send_message(chat_id=update.message.chat_id, text=args[0]+"분할로 설정하였습니다.")
	bot.send_message(chat_id=update.message.chat_id, text="수량: "+args[1])
	amount = int(args[1])
	start = int(args[2])
	end = int(args[3])
	interval = end-start
	
	price_list = []
	k = int(args[0])
	for i in range(k):
		price_list.append(price(i,k,10,k*10))
	price_sum = sum(price_list)/100
	changed_list = []
	for i in range(k):
		changed_list.append(price_list[i]/price_sum)
	total = 0
	for i in range(k):
		bot.send_message(chat_id=update.message.chat_id, text="가격: "+str(int(start)+int(int(interval)*i/(k-1)))+", 수량: "+str(int(changed_list[i]/100*amount)))
		total = total + int(changed_list[i]/100*amount)
	bot.send_message(chat_id=update.message.chat_id, text="총수량: "+str(total))



	






from telegram.ext import CommandHandler



calc_handler = CommandHandler('calc', calc,pass_args=True)
trade_handler = CommandHandler('trade', trade)

dispatcher.add_handler(calc_handler)
dispatcher.add_handler(trade_handler)



updater.start_polling()



#여기서 CommandHandler 는 /start 메세지 를 들어 올때는 의미합니다 / 가 붙으면 커맨더 명령이라고 인식 합니다. 



# 그리고 dispatcher 에 해당 핸들러를 추가 해 줍니다. 



# 그럼/start 채팅이 홨을때 update.message.chat_id-> /start 메세지를 보낸 ID 에 



# "I'm a bot, please talk to me!" 을 보냅니다. 

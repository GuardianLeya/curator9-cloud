import telebot
bot = telebot.TeleBot('6486769450:AAEIju-EuWa6G041VMAihASG59XVfyV_TXM')

@bot.message.handler(commands=['start'])
def main(message):
	bot.send_message(message.chat.id, 'Привет, я пушистик, а ты?')
    
@bot.message.handler(commands=['Polina'])
def main(message):
	bot.send_message(message.chat.id, '*я люблю тебя*', parse_mode='Markdown')

@bot.message.handler(commands=[link])
def main(message):
	bot.send_message(message.chat.id, 'Жмак на [ссылку](https://w.forfun.com/fetch/c4/c493aac67877288476b0fc52d55f55cf.jpeg);)', parse_mode='Markdown')

bot.infinity_polling()

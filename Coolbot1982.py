import telebot

token = ("6736617509:AAHH0BVsvRn5fTpTxQWgw4T3CJGBZN5t6p4")
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda message: message.text.lower() == 'привет')
def handle_message(message):
    bot.send_message(message.chat.id, 'Привет!')

# Запуск бота
bot.polling()

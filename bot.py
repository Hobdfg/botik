import telebot
from info import information, help, visitochka
from config import bottoken

bot = bottoken


def secretfilter(message):
    password = "12345"
    return password in message.text.lower()


def Goodbye(message):
    key = "пока"
    return key in message.text.lower()


@bot.message_handler(content_types=['text'], func=secretfilter)
def secret_way(message):
    bot.send_message(message.chat.id, f"Здравствуй! Ты открыл секрет, прими мои поздравления!")


@bot.message_handler(content_types=['text'], func=Goodbye)
def say_bye(message):
    bot.send_message(message.chat.id, f"Эхх, прощай.")


@bot.message_handler(commands=['start'])
def reply(message):
    bot.send_message(message.chat.id, f"{information}")


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(message.chat.id, f"{help}")


@bot.message_handler(commands=['visitka'])
def giveinfo(message):
    bot.send_message(message.chat.id, f"{visitochka}")


@bot.message_handler(content_types=['text'])
def send_media(message):
    if message.text.lower() == "отправь pepe":
        photo = open('pepe.png', 'rb')
        bot.send_photo(message.chat.id, photo)


bot.polling()

import telebot;
from credentials import token;

bot = telebot.TeleBot(token)


#@bot.message_handler(commands=['start', 'gm', 'help'])

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Hi! How can I help you?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "List of commands: \n"
        "1) /help \n"
        "2) /gm \n" )
    elif message.text == "/gm":
        pic = open('D:/repos/python/unrealClown_bot/telegram_bot/pic/gm.jpg', 'rb')
        bot.send_photo(message.from_user.id, pic)
    else:
        bot.send_message(message.from_user.id, "I do not understand you. Try command /help.")



bot.polling(none_stop=True, interval = 0)
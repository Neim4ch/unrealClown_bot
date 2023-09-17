import telebot;
from credentials import token;
from echo import echoGame

bot = telebot.TeleBot(token)
echoGameEx = echoGame()

@bot.message_handler(commands=['start'])
def start(message):
    answer = f'Привет!!! <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.from_user.id, text=answer, parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.from_user.id,  "Доступны следующие команды: \n"
                                            "1) /help \n"
                                            "2) /gm \n" 
                                            "3) /echo [on/off]" )

@bot.message_handler(commands=['gm'])
def gm(message):
    pic = open('pic/pic_gm.jpg', 'rb')
    bot.send_photo(message.from_user.id, pic)

@bot.message_handler(commands=['echo'])
def echo(message):
    arg = ' '.join(message.text.split(' ')[1:])
    answer = "Режим \"Эхо\" сейчас "
    if echoGameEx.echo_func(arg):
        answer += 'включен.\n'
    else:
        answer += 'выключен.\n'
    bot.send_message(message.from_user.id, answer)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if(echoGameEx.echo_func('')):
        bot.send_message(message.from_user.id, message.text)
    else:
        bot.send_message(message.from_user.id, "I do not understand you. Try command /help.")



bot.polling(none_stop=True, interval = 0)
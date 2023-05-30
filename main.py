import telebot
bot = telebot.TeleBot('5946796978:AAHXcMpBuBVB6e5ZHWxtns0q3-Vhcaq4ylo')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добрий день💸')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, "Усі кажуть " + message.text + " ,а ти купи слона")
bot.polling()
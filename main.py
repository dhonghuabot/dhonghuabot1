import os
import telebot

bot = telebot.TeleBot("Api key")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"hello i am dhonghua bot")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message,"i am fine")

bot.polling()
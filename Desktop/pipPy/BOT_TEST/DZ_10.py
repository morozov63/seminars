import telebot
import requests

bot = telebot.TeleBot("5819002344:AAEi3a6FAQJk63G03xJOzws8vJokgRs2MT8")


@bot.message_handler(commands=['currency'])
def send_welcome(message):
	bot.reply_to(message, "Введите код валюты в формате USD, EUR, CNY:  ")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    
   currency_name = (message.text)
   res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
   for i in res.values():
   
    if  currency_name in i:
     bot.send_message(message.chat.id, res['Valute'][f"{ currency_name}"]['Name'])
     bot.send_message(message.chat.id, res['Valute'][f"{ currency_name}"]['Value'])
     bot.send_message(message.chat.id, "Номинал: ")
     bot.send_message(message.chat.id, res['Valute'][f"{ currency_name}"]['Nominal'])
bot.infinity_polling()
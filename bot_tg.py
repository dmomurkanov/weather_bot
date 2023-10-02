import telebot
import requests
import json

bot = telebot.TeleBot('6583716138:AAEVOogVeUvavK1R5L3HpDruIh_dilniVps')
API = '58d52ecda68ae6736608b5601739859b'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Weather Bot! Напишите название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f"Сейчас погода : {temp}")
        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Название города указано не верно. Попробуйте еще раз')


bot.polling(none_stop=True)

import telebot
import config
import requests
bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types = ["text"])
def ip(message):
    data = requests.get("https://api.2ip.ua/geo.json?ip="+str(message.text))
    print(str(message))
    bot.send_message(message.chat.id, data.json()["country"])
    bot.send_message(message.chat.id,  data.json()["city"])
    bot.send_message(message.chat.id, data.json()["zip_code"])



if __name__ =='__main__':
    bot.polling(none_stop=True)
    

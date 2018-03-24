import telebot
import config

bot = telebot.TeleBot(config.token)
produkt = ("картофель","лук","колбаса","майонез","соленые огурцы","морковь")
gramm = (50, 20, 100, 15, 30, 30)
@bot.message_handler(commands = ["olivie"])
def answer_olivie(message):
    bot.send_message(message.chat.id, "Введите количество человек: ")
    olivie(message)


@bot.message_handler(content_types = ["text"])
def olivie(message):
    print(message)
    try:
        people_count = int(message.text)
        for i in range(0, len(produkt)):
            bot.send_message(message.chat.id, produkt[i] + " - " + str(gramm[i] * people_count) + "гр.")
    except:
        print("Неправильное число")
        
if __name__ =='__main__':
    bot.polling(none_stop=True)
    
    

import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = '7616075220:AAFpvIg2w0C-uWVDZYMF7k9SANMSH9WM77U'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Привет, это бот-проект школы "Третье Место". здесь ты можешь узнать необходимую для тебя информацию о школе.
/info - Получить информацию
/question - Задать вопрос
""")


#@bot.message_handler(commands=['question'])
#def support(message):
#    inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
#    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
#    bot.reply_to(message, text='Задайте интересующий вас вопрос:', )


def main():
    bot.infinity_polling()
if __name__ == '__main__':
    main()
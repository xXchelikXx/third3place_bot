

import telebot
from telebot import types

API_TOKEN = '7616075220:AAFpvIg2w0C-uWVDZYMF7k9SANMSH9WM77U'
CHAT_ID = '@third3bot_tgc'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Привет, это бот-проект школы "Третье Место". здесь ты можешь узнать необходимую для тебя информацию о школе.
/info - Получить информацию
/question - Задать вопрос
""")


@bot.message_handler(commands=['info'])
def info_selection(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    main_info = types.KeyboardButton('📕 Основная информация 📕') # информация о компании и обучении
    interactions = types.KeyboardButton('👨‍🏫 Связь и кураторская поддержка 👨‍🏫') # Информация про дискорд и кураторская поддержка
    events = types.KeyboardButton('🧑‍💻 Хакатон и Интенсив 🧑‍💻')
    holidays_and_pay = types.KeyboardButton('😴 Каникулы и оплата 💵')
    markup.add(main_info, interactions, events, holidays_and_pay)
    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def holidays_and_pay_func(message):
    if message.text == '😴 Каникулы и оплата 💵':
        photo = open('pay.jpg', 'rb')
        bot.send_photo(CHAT_ID, photo, caption="Вот как производится оплата:")
    else:
        bot.send_message(CHAT_ID, text='⚠️ Не найдено функции для данной команды ⚠️')


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()


#@bot.message_handler(commands=['question'])
#def support(message):
#    inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
#    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
#    bot.reply_to(message, text='Задайте интересующий вас вопрос:', )
import telebot
from telebot import types
from text import text # взятие текста из text.py

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
    main_info = types.KeyboardButton('📕 Основная информация 📕')
    interactions = types.KeyboardButton('👨‍🏫 Связь и кураторская поддержка 👨‍🏫')
    events = types.KeyboardButton('🧑‍💻 Хакатон и Интенсив 🧑‍💻')
    holidays_and_pay = types.KeyboardButton('😴 Каникулы и оплата 💵')
    markup.add(main_info, interactions, events, holidays_and_pay)
    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def command_processing(message):
    if message.text == '😴 Каникулы и оплата 💵':
        bot.send_message(message.chat.id, text=text.get('holidays_and_pay')) # получение текста из словаря text и вывод
    elif message.text == '🧑‍💻 Хакатон и Интенсив 🧑‍💻':
        bot.send_message(message.chat.id, text=text.get('events')) # получение текста из словаря text и вывод
    elif message.text == '📕 Основная информация 📕':
        bot.send_message(message.chat.id, text=text.get('main_info')) # получение текста из словаря text и вывод
    elif message.text == '👨‍🏫 Связь и кураторская поддержка 👨‍🏫':
        bot.send_message(message.chat.id, text=text.get('interactions')) # получение текста из словаря text и вывод
    else:
        bot.send_message(CHAT_ID, text='⚠️ Не найдено функции для данной команды ⚠️')


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
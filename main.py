import telebot
from telebot import types
from text import text

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
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    main_info = types.KeyboardButton('📕 Основная информация 📕')
    interactions = types.KeyboardButton('👨‍🏫 Связь и кураторская поддержка 👨‍🏫')
    events = types.KeyboardButton('🧑‍💻 Хакатон и Интенсив 🧑‍💻')
    holidays_and_pay = types.KeyboardButton('😴 Каникулы и оплата 💵')
    cancel = types.KeyboardButton('Отмена')
    markup.add(main_info, interactions, events, holidays_and_pay, cancel)
    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)
    if message.text == 'Отмена':
        pass


@bot.message_handler(func=lambda message: True)
def command_processing(message):
    try:
        if message.text == '😴 Каникулы и оплата 💵':
            markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
            pay_button = types.KeyboardButton('💲 Оплата 💸')
            holidays_button = types.KeyboardButton('🌞 Каникулы 😎')
            back_button = types.KeyboardButton('К категориям')
            markup.add(pay_button, holidays_button, back_button)
            bot.send_message(message.chat.id, 'Выберите вопрос:', reply_markup=markup)
        elif message.text == '🧑‍💻 Хакатон и Интенсив 🧑‍💻':
            markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
            hackathon_button = types.KeyboardButton('🧑‍💻 Хакатон 🏅') # МЕСТО ДЛЯ КЛЮЧА ТЕКСТА ПРО ХАКАТОН
            intensive_button = types.KeyboardButton('🏃 Интенсив 👨‍💻') # МЕСТО ДЛЯ КЛЮЧА ТЕКСТА ПРО ИНТЕНСИВ
            back_button = types.KeyboardButton('К категориям')
            markup.add(hackathon_button, intensive_button, back_button)
            bot.send_message(message.chat.id, 'Выберите вопрос:', reply_markup=markup)
        elif message.text == '📕 Основная информация 📕':
            markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
            info_button = types.KeyboardButton('🏢 Информация о компании 🧑‍💻')
            education_button = types.KeyboardButton('🧑‍🎓 Обучение 📖')
            back_button = types.KeyboardButton('К категориям')
            markup.add(info_button, education_button, back_button)
            bot.send_message(message.chat.id, 'Выберите вопрос:', reply_markup=markup)
        elif message.text == '👨‍🏫 Связь и кураторская поддержка 👨‍🏫':
            markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
            discord_button = types.KeyboardButton('💬 Информация про дискорд 👨‍🏫')
            support_button = types.KeyboardButton('🤗 Кураторская поддержка 👋')
            back_button = types.KeyboardButton('К категориям')
            markup.add(discord_button, support_button, back_button)
            bot.send_message(message.chat.id, 'Выберите вопрос:', reply_markup=markup)
        elif message.text == 'Отмена':
            pass
        bot.send_message(CHAT_ID, text=text.get(message.text))
    except Exception as error:
        print(f'An error occurred while executing the program: {error}')
        bot.send_message(CHAT_ID, text='⚠️ Ошибка при попытке выполнения команды. ⚠️')


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
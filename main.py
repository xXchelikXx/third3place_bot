import telebot
from telebot import types
from text import text


API_TOKEN = '7616075220:AAFpvIg2w0C-uWVDZYMF7k9SANMSH9WM77U'
ADMINS_CHAT_ID = '@tech_support_thirdplace'
COMMANDS = [
    '📕 Основная информация 📕',
    '👨‍🏫 Связь и кураторская поддержка 👨‍🏫',
    '🧑‍💻 Хакатон и Интенсив 🧑‍💻',
    '😴 Каникулы и оплата 💵',
    '💲 Оплата 💸',
    '🌞 Каникулы 😎',
    '🧑‍💻 Хакатон 🏅',
    '🏃 Интенсив 👨‍💻',
    '🏢 Информация о компании 🧑‍💻',
    '🧑‍🎓 Обучение 📖',
    '💬 Информация про дискорд 👨‍🏫',
    '🤗 Кураторская поддержка 👋',
    '❓ Не нашли ответа на свой вопрос? ❓',
    'Написать вопрос',
    'Отмена'
]
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """
Привет, это бот-проект школы "Третье Место". здесь ты можешь узнать необходимую для тебя информацию о школе.
/info - Получить информацию
""")


@bot.message_handler(commands=['info'])
def info_selection(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    main_info = types.KeyboardButton('📕 Основная информация 📕')
    interactions = types.KeyboardButton('👨‍🏫 Связь и кураторская поддержка 👨‍🏫')
    events = types.KeyboardButton('🧑‍💻 Хакатон и Интенсив 🧑‍💻')
    holidays_and_pay = types.KeyboardButton('😴 Каникулы и оплата 💵')
    question_button = types.KeyboardButton('❓ Не нашли ответа на свой вопрос? ❓')
    back_button = types.KeyboardButton('Отмена')
    markup.add(main_info, interactions, events, holidays_and_pay, question_button, back_button)
    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def command_processing(message):
    if message.text in COMMANDS:
        try:
            is_need_to_send = True
            if message.text == '😴 Каникулы и оплата 💵':
                markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
                pay_button = types.KeyboardButton('💲 Оплата 💸')
                holidays_button = types.KeyboardButton('🌞 Каникулы 😎')
                back_button = types.KeyboardButton('Отмена')
                markup.add(pay_button, holidays_button, back_button)
                bot.send_message(message.chat.id, 'Выберите вопрос:', reply_markup=markup)
            elif message.text == '🧑‍💻 Хакатон и Интенсив 🧑‍💻':
                markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
                hackathon_button = types.KeyboardButton('🧑‍💻 Хакатон 🏅')
                intensive_button = types.KeyboardButton('🏃 Интенсив 👨‍💻')
                back_button = types.KeyboardButton('Отмена')
                markup.add(hackathon_button, intensive_button, back_button)
                bot.send_message(message.chat.id, 'Выберите вопрос:', reply_markup=markup)
            elif message.text == '📕 Основная информация 📕':
                markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
                info_button = types.KeyboardButton('🏢 Информация о компании 🧑‍💻')
                education_button = types.KeyboardButton('🧑‍🎓 Обучение 📖')
                back_button = types.KeyboardButton('Отмена')
                markup.add(info_button, education_button, back_button)
                bot.send_message(message.chat.id, 'Выберите вопрос:', reply_markup=markup)
            elif message.text == '👨‍🏫 Связь и кураторская поддержка 👨‍🏫':
                markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
                discord_button = types.KeyboardButton('💬 Информация про дискорд 👨‍🏫')
                support_button = types.KeyboardButton('🤗 Кураторская поддержка 👋')
                back_button = types.KeyboardButton('Отмена')
                markup.add(discord_button, support_button, back_button)
                bot.send_message(message.chat.id, 'Выберите вопрос:', reply_markup=markup)
            elif message.text == '❓ Не нашли ответа на свой вопрос? ❓':
                is_need_to_send = False
                print('test')
                markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
                ask_button = types.KeyboardButton('Написать вопрос')
                back_button = types.KeyboardButton('Отмена')
                markup.add(ask_button, back_button)
                bot.send_message(message.chat.id, 'Желаете написать вопрос Администрации?', reply_markup=markup)
            elif message.text == 'Написать вопрос':
                is_need_to_send = False
                bot.send_message(message.chat.id, 'Напишите сюда вопрос, и он будет отправлен Администрации. Вам постараются ответить в ближайшие сроки!')
                bot.register_next_step_handler(message, report)
            elif message.text == 'Отмена':
                is_need_to_send = False
                bot.send_message(message.chat.id, 'Действие отменено.', reply_markup=types.ReplyKeyboardRemove())
            if is_need_to_send:
                bot.send_message(message.chat.id, text=text.get(message.text))
            else:
                pass
        except Exception as error:
            print(f'An error occurred while executing the program: {error}')
            bot.send_message(message.chat.id, text='⚠️ Ошибка при попытке выполнения команды. ⚠️')
    else:
        pass


def report(message):
    bot.send_message(ADMINS_CHAT_ID, text=f'''
Новый вопрос!

Вопрос от пользователя @{message.from_user.username}:
--------------------
{message.text}
--------------------
''')


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
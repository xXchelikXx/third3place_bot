import telebot
from telebot import types
from text import text
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
ADMINS_CHAT_ID = os.getenv("ADMINS_CHAT_ID")
COMMANDS = {
    "📕 Основная информация 📕": {
        'buttons': {
            "🏢 Информация о компании 🧑‍💻": 'company_info',
            "🧑‍🎓 Обучение 📖": 'education',
            "Отмена": 'cancel'
        },
        'callback': 'main_info'
    },
    "👨‍🏫 Связь и кураторская поддержка 👨‍🏫": {
        'buttons': {
            "💬 Информация про дискорд 👨‍🏫": 'discord',
            "🤗 Кураторская поддержка 👋": 'cur_support',
            "Отмена": 'cancel'
        },
        'callback': 'communication'
    },
    "🧑‍💻 Хакатон и Интенсив 🧑‍💻": {
        'buttons': {
            "🧑‍💻 Хакатон 🏅": 'hackathon',
            "🏃 Интенсив 👨‍💻": 'intensive',
            "Отмена": 'cancel'
        },
        'callback': 'events'
    },
    "😴 Каникулы и оплата 💵": {
        'buttons': {
            "💲 Оплата 💸": 'pay',
            "🌞 Каникулы 😎": 'holidays',
            "Отмена": 'cancel'
        },
        'callback': 'holidays_and_pay'
    },
    "❓ Не нашли ответа на свой вопрос? ❓": {
        'buttons': {
            "Написать вопрос": 'question',
            "Отмена": 'cancel'
        },
        'callback': 'support'
    }
}
CALLBACK_INFO = {
    'main_info': '📕 Основная информация 📕',
    'communication': '👨‍🏫 Связь и кураторская поддержка 👨‍🏫',
    'events': '🧑‍💻 Хакатон и Интенсив 🧑‍💻',
    'holidays_and_pay': '😴 Каникулы и оплата 💵',
    'support': '❓ Не нашли ответа на свой вопрос? ❓'
}
bot = telebot.TeleBot(API_TOKEN)


def create_keyboard(buttons, task, selection=''):
    markup = types.InlineKeyboardMarkup()
    if task == 'section':
        for button in buttons:
            callback = COMMANDS[button]['callback']
            markup.add(types.InlineKeyboardButton(button, callback_data=callback))
    elif task == 'action':
        for button_text, callback in buttons['buttons'].items():
            markup.add(types.InlineKeyboardButton(button_text, callback_data=callback))
    return markup


@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(
        message,
        """
Привет, это бот-проект школы "Третье Место". здесь ты можешь узнать необходимую для тебя информацию о школе.
/info - Получить информацию
""",
    )


@bot.message_handler(commands=["info"])
def info_selection(message):
    markup = create_keyboard(list(COMMANDS.keys()), task='section')
    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in CALLBACK_INFO)
def handle_section(call: types.CallbackQuery):
    bot.send_message(call.message.chat.id, text=text[call.data])

    buttons = COMMANDS[CALLBACK_INFO[call.data]]
    bot.send_message(
        call.message.chat.id, "Выберите вопрос (действие):",
        reply_markup=create_keyboard(buttons, task='action')
    )
    bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data in COMMANDS[CALLBACK_INFO['main_info']]['buttons'].values())
def handle_action(call: types.CallbackQuery):
    bot.send_message(call.message.chat.id, text=text[call.data])
    markup = create_keyboard(list(COMMANDS.keys()), task='section')
    bot.send_message(call.message.chat.id, "Выберите раздел:", reply_markup=markup)
    bot.delete_message(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == 'cancel')
def cancel(call: types.CallbackQuery):
    bot.send_message(call.message.chat.id, text=text[call.data])
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)


@bot.callback_query_handler(func=lambda call: call.data == 'question')
def question(call: types.CallbackQuery):
    bot.send_message(
        call.message.chat.id,
        "Напишите сюда вопрос, и он будет отправлен Администрации. Вам постараются ответить в ближайшие сроки!",
    )
    bot.register_next_step_handler(call.message, report)


def report(message):
    bot.send_message(
        message.chat.id, "Ваш вопрос отправлен Администрации. Ожидайте ответа!"
    )
    answer = bot.send_message(
        ADMINS_CHAT_ID,
        text=f"""
Новый вопрос!

Вопрос от пользователя @{message.from_user.username}:
--------------------
{message.text}
--------------------
Свайпните, чтобы ответить.
""",
    )
    bot.register_next_step_handler(answer, reply, message.chat.id)


def reply(answer, user_chat_id):
    bot.send_message(user_chat_id, text=f"""
Пришёл ответ от Администрации!

Ответ от Администратора:
--------------------
{answer.text}
--------------------
""")


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()

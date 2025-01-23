import telebot
from telebot import types
from text import text
from dotenv import load_dotenv
import os


load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
ADMINS_CHAT_ID = os.getenv("ADMINS_CHAT_ID")
COMMANDS = {
    "📕 Основная информация 📕": [
        "🏢 Информация о компании 🧑‍💻",
        "🧑‍🎓 Обучение 📖",
        "Отмена",
    ],
    "👨‍🏫 Связь и кураторская поддержка 👨‍🏫": [
        "💬 Информация про дискорд 👨‍🏫",
        "🤗 Кураторская поддержка 👋",
        "Отмена",
    ],
    "🧑‍💻 Хакатон и Интенсив 🧑‍💻": ["🧑‍💻 Хакатон 🏅", "🏃 Интенсив 👨‍💻", "Отмена"],
    "😴 Каникулы и оплата 💵": ["💲 Оплата 💸", "🌞 Каникулы 😎", "Отмена"],
    "❓ Не нашли ответа на свой вопрос? ❓": ["Написать вопрос", "Отмена"],
}
bot = telebot.TeleBot(API_TOKEN)


def create_keyboard(buttons):
    markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
    for button in buttons:
        markup.add(types.KeyboardButton(button))
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
    markup = create_keyboard(list(COMMANDS.keys()))
    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def command_processing(message):
    if message.text in text:
        bot.send_message(message.chat.id, text=text.get(message.text))
    if message.text in COMMANDS:
        buttons = COMMANDS[message.text]
        bot.send_message(
            message.chat.id, "Выберите вопрос:", reply_markup=create_keyboard(buttons)
        )

    if message.text == "Отмена":
        bot.send_message(
            message.chat.id,
            "Действие отменено.",
            reply_markup=types.ReplyKeyboardRemove(),
        )
        return
    elif message.text == "Написать вопрос":
        bot.send_message(
            message.chat.id,
            "Напишите сюда вопрос, и он будет отправлен Администрации. Вам постараются ответить в ближайшие сроки!",
        )
        bot.register_next_step_handler(message, report)


def report(message):
    bot.send_message(
        ADMINS_CHAT_ID,
        text=f"""
Новый вопрос!

Вопрос от пользователя @{message.from_user.username}:
--------------------
{message.text}
--------------------
""",
    )
    bot.send_message(
        message.chat.id, "Ваш вопрос отправлен Администрации. Ожидайте ответа!"
    )


def main():
    bot.infinity_polling()


if __name__ == "__main__":
    main()

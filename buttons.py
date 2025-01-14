import telegram
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import telebot
from telebot import types
import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Это бот для школы 'Третье место'")
    bot.send_message(update.effective_chat.id, 'hi', reply_markup=mm)

@bot.message_handler(content_types=['start'])
def handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    button1 = types.KeyboardButton("🐣 Привет")
    markup.add(button1)
    bot.send_message(message.chat.id, "Push", reply_markup=markup)


async def info_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Инфа")

if __name__ == '__main__':
    application = ApplicationBuilder().token('7616075220:AAFpvIg2w0C-uWVDZYMF7k9SANMSH9WM77U').build()

    bot = telebot.TeleBot(config.Token)
    
    info_handler = CommandHandler('info', info_handler)
    application.add_handler(info_handler)
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    
    application.run_polling()
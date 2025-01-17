

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
        markup = types.ReplyKeyboardMarkup(row_width=2)
        pay_btn = types.KeyboardButton('💲 Оплата 💸')
        holidays_btn = types.KeyboardButton('🌞 Каникулы 😎')
        markup.add(pay_btn, holidays_btn)
        bot.send_message(message.chat.id, "Выберите вопрос:", reply_markup=markup)
    
    elif message.text == '💲 Оплата 💸':
        pay_txt = '''
Вы оплачиваете каждый период/абонемент (8 занятий по утвержденному расписанию), каждые 28 дней, в последний день предыдущего оплаченного периода. Мы будем об этом напоминать. Если нет возможности оплатить в срок - предупредите, мы подождем, занятия при этом не приостанавливаем.
+Бонус
Когда по вашей рекомендации к нам придет новый ученик фиксированная скидка 2500 рублей на
один период.
'''
        bot.send_message(CHAT_ID, pay_txt)
    elif message.text == '🌞 Каникулы 😎':
        holidays_txt ='''
Новогодние, майские и летние каникулы - исключение, когда абонемент можно заморозить. В остальное время оплата идет каждые 8 занятий по расписанию.
Пропущенные основные занятия по любым причинам у вас не сгорают, а отрабатываются, вне расписания, по договоренности с педагогом, без привязки к оплате периодов. По запросу мы пришлем вам варианты, когда можно подключиться на отработку. Отработки проводятся в другой группе при наличии свободного места, либо индивидуально, но длительностью 45 минут. Если нет возможности отработать в учебное время, то копим пропуски и отрабатываем во время школьных каникул.
При решении сделать паузу в занятиях более трех недель без оплаты будущих уроков место в группе открепляется, и по возвращению если место занято - подбирается новая группа или педагог.
'''
        bot.send_message(CHAT_ID, holidays_txt)
    else:
        bot.send_message(CHAT_ID, text='⚠️ Не найдено функции для данной команды ⚠️')


# @bot.message_handler(func=lambda message: True)
# def discord_and_help_fun(message):
#     if message.txt == '👨‍🏫 Связь и кураторская поддержка 👨‍🏫':
#         markup = types.ReplyKeyboardMarkup(row_width=2)
#         discord_btn = types.KeyboardButton('💬 Связь, дискорд 👨‍🏫')
#         help_btn = types.KeyboardButton('')




#             discord_file = open('discord.pdf', 'rb')


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()


#@bot.message_handler(commands=['question'])
#def support(message):
#    inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
#    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
#    bot.reply_to(message, text='Задайте интересующий вас вопрос:', )
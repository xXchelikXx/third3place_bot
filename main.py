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
        bot.send_message(CHAT_ID, text=text.get('holidays_and_pay')) # получение текста из словаря text и вывод
    elif message.text == '🧑‍💻 Хакатон и Интенсив 🧑‍💻':
        bot.send_message(CHAT_ID, text=text.get('events')) # получение текста из словаря text и вывод
    elif message.text == '📕 Основная информация 📕':
        bot.send_message(CHAT_ID, text=text.get('main_info')) # получение текста из словаря text и вывод
    elif message.text == '👨‍🏫 Связь и кураторская поддержка 👨‍🏫':
        bot.send_message(CHAT_ID, text=text.get('interactions')) # получение текста из словаря text и вывод
def buttons_func(message):
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
    elif message.text == '👨‍🏫 Связь и кураторская поддержка 👨‍🏫':
        markup = types.ReplyKeyboardMarkup(row_width=2)
        discord_btn = types.KeyboardButton('💬 Информация про дискорд 👨‍🏫')
        help_btn = types.KeyboardButton('🤗 Кураторская поддержка 👋')
        markup.add(discord_btn, help_btn)
        bot.send_message(message.chat.id, "Выберите вопрос:", reply_markup=markup)
    elif message.text == '💬 Информация про дискорд 👨‍🏫':
        discord_txt = '''
Чтобы зарегестрироваться в Discord нужно:
Шаг 1
Переходим по ссылке: https://discordapp.com/download
Затем нужно нажать кнопку "Вход" в открытом окне
Шаг 2
Затем нужно нажать "Зарегистрироваться"
Шаг 3
Для регистрации используйте гугл почту (gmail)
Не забудьте сохранить пароль куда-нибудь :)
При регистрации нужно будет указать год 2001 или более ранний, иначе
программа не сможет зарегистрировать аккаунт
После регистрации зайдите к себе на почту, чтобы подтвердить аккаунт.
Потом на сайте можно будет войти в дискорд, либо скачать его
Шаг 4
Как всё сделаете - напишите нам, пожалуйста, ваш никнейм, он будет
указан в левом нижнем углу
Если что-то непонятно будет - спрашивайте
'''
        bot.send_message(CHAT_ID, discord_txt)
    else:
        bot.send_message(CHAT_ID, text='⚠️ Не найдено функции для данной команды ⚠️')


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
import telebot
from telebot import types
from Kabo import token, chat_id


def k(buttons):
    keyboard = types.InlineKeyboardMarkup()
    for button in buttons:
        keyboard.add(types.InlineKeyboardButton(**button))
    return keyboard


telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

kabo = telebot.TeleBot(token=token)


@kabo.message_handler()
def f(message):
    if message.chat.id == 542658693:  # TG ID Кабо
        keyboard = types.InlineKeyboardMarkup()
        kabo.send_message(message.chat.id, 'Какие люди!\nЧего вы желаете?',
                          reply_markup=k([
                              {'text': 'Распределение по чайкам', 'callback_data': 'tea'},
                              {'text': 'none', 'callback_data': 'none'},
                              {'text': 'none', 'callback_data': 'none'},
                          ]))
    else:
        kabo.send_message(message.chat.id, 'Привет! Я бот чаёк.\n\nПрошу ждать оповещения в беседе.')
    # print(message)


@kabo.callback_query_handler(func=lambda call: True)
def f(call):
    if call.data == 'tea':
        kabo.send_message(call.message.chat.id, 'Начинаю распределение по чайкам!')
    elif call.data == 'none':
        kabo.send_message(call.message.chat.id, 'Ничего нет)')


kabo.polling(none_stop=True, timeout=100)

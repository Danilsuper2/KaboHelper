import telebot
from telebot import types
from Kabo import token, chat_id

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

kabo = telebot.TeleBot(token=token)


@kabo.message_handler()
def f(message):
    if message.chat.id == 542658693:  # TG ID Кабо
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='1', callback_data=1))
        keyboard.add(types.InlineKeyboardButton(text='2', callback_data=2))
        keyboard.add(types.InlineKeyboardButton(text='3', callback_data=3))
        kabo.send_message(message.chat.id, 'Какие люди!\nЧего вы желаете?',
                          reply_markup=keyboard)
    else:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text='1', callback_data=1))
        keyboard.add(types.InlineKeyboardButton(text='2', callback_data=2))
        keyboard.add(types.InlineKeyboardButton(text='3', callback_data=3))
        kabo.send_message(message.chat.id, 'Привет! Я бот чаёк.\n\nПрошу ждать оповещения в беседе.')
    # print(message)


@kabo.callback_query_handler(func=lambda call: True)
def f(call):
    kabo.send_message(call.message.chat.id, 'Вы нажали на кнопку {}'.format(call.data))

kabo.polling(none_stop=True)

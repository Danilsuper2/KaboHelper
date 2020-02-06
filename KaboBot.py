import telebot
from Kabo import token, chat_id

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

kabo = telebot.TeleBot(token=token)
# kabo.send_message(chat_id, 'Чай?')

import telebot
from KaboToken import token

telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

kabo = telebot.TeleBot(token=token)
kabo.send_message(-1001213915805, 'Чай?')

import math
import random

from telegram.ext import *
from telegram import *
import argparse
import requests
import telebot
from telebot import types

bot = telebot.TeleBot("6443463170:AAH1a3G2p72uA2INs3_5_WHgDHB7HlnHIwM")
players = dict()
count = 0
user_name = ''  # Переменная с именем пользователя
user_city = ''  # Переменная с городом пользователя
user_address = ''  # Переменная с адресом пользователя
user_comment = ''  # Переменная с комментарием пользователя
country = ''
current_city = ''  # Переменная с текущим городом в игре "Угадай город"
try_counter = 0  # Счёичмк попыток в игре "Угадай город"
game_is_played = False  # Переменная с состаянием игры "Угадай город"
is_admin = True  # Переменна яс состоянием меню админа
dumb_touple = {'Московская область': '1', 'Санкт-Петербург': '2', 'Москва': '213', 'Россия': '225',
               'Севастополь': '959', 'Республика Крым': '977', 'Ленинградская область': '10174',
               'Ненецкий автономный округ': '10176', 'Республика Алтай': '10231', 'Республика Тыва': '10233',
               'Еврейская автономная область': '10243', 'Чукотский автономный округ': '10251',
               'Белгородская область': '10645', 'Брянская область': '10650', 'Владимирская область': '10658',
               'Воронежская область': '10672', 'Ивановская область': '10687', 'Калужская область': '10693',
               'Костромская область': '10699', 'Курская область': '10705', 'Липецкая область': '10712',
               'Орловская область': '10772', 'Рязанская область': '10776', 'Смоленская область': '10795',
               'Тамбовская область': '10802', 'Тверская область': '10819', 'Тульская область': '10832',
               'Ярославская область': '10841', 'Архангельская область': '10842', 'Вологодская область': '10853',
               'Калининградская область': '10857', 'Мурманская область': '10897', 'Новгородская область': '10904',
               'Псковская область': '10926', 'Республика Карелия': '10933', 'Республика Коми': '10939',
               'Астраханская область': '10946', 'Волгоградская область': '10950', 'Краснодарский край': '10995',
               'Республика Адыгея': '11004', 'Республика Дагестан': '11010', 'Республика Ингушетия': '11012',
               'Кабардино-Балкарская Республика': '11013', 'Республика Калмыкия': '11015',
               'Карачаево-Черкесская Республика': '11020', 'Республика Северная Осетия — Алания': '11021',
               'Чеченская Республика': '11024', 'Ростовская область': '11029', 'Ставропольский край': '11069',
               'Кировская область': '11070', 'Республика Марий Эл': '11077', 'Нижегородская область': '11079',
               'Оренбургская область': '11084', 'Пензенская область': '11095', 'Пермский край': '11108',
               'Республика Башкортостан': '11111', 'Республика Мордовия': '11117', 'Республика Татарстан': '11119',
               'Самарская область': '11131', 'Саратовская область': '11146', 'Удмуртская Республика': '11148',
               'Ульяновская область': '11153', 'Чувашская Республика': '11156', 'Курганская область': '11158',
               'Свердловская область': '11162', 'Тюменская область': '11176',
               'Ханты-Мансийский автономный округ — Югра': '11193', 'Челябинская область': '11225',
               'Ямало-Ненецкий автономный округ': '11232', 'Алтайский край': '11235', 'Иркутская область': '11266',
               'Кемеровская область': '11282', 'Красноярский край': '11309', 'Новосибирская область': '11316',
               'Омская область': '11318', 'Республика Бурятия': '11330', 'Республика Хакасия': '11340',
               'Томская область': '11353', 'Амурская область': '11375', 'Камчатский край': '11398',
               'Магаданская область': '11403', 'Приморский край': '11409', 'Республика Саха (Якутия)': '11443',
               'Сахалинская область': '11450', 'Хабаровский край': '11457', 'Забайкальский край': '21949'}
keyboard_main = [['🦠 Covid-19'],
                 ['🌤 Узнать погоду', '🖊️ Написать отзыв', '🌆 Ввести новый адрес'],
                 ['🚇 Найти ближайшее метро', '🍟 Найти ближайший макдональдс',
                  '🏥 Показать аптеки недалеко от вас'],
                 ['🎮 Игры']]
keyboard_games = [['🌆 Угадай город', '🎲 Кинуть кубик'],
                  ['🕶 Основные функции']]
covid_keyboard = [['🦠 В регионах', '🦠 В странах'],
                  ['🕶 Основные функции']]
keyboard_admin = [['Перезапустить бота']]
keyboard = keyboard_main


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать игру")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Начнем игру?".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    global players
    global count
    if message.text == "Начать игру":
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text="На сколько человек?", reply_markup=markup)

    elif message.text.isdigit():
        if int(message.text) < 7:
            count = 1
            print(count)
        elif int(message.text) > 6:
            count = math.ceil(int(message.text) / 4)
            print(count)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = types.KeyboardButton("Begin")
        b1 = types.KeyboardButton('All players are here')
        markup.add(b)
        markup.add(b1)
        bot.send_message(message.chat.id, f"В таком случае mafiosi: {count}", reply_markup=markup)

    elif message.text == 'Begin':
        bot.send_message(message.chat.id, text="Участники, пожалуйста, поставьте +")
    elif message.text == '+':
        players[message.from_user.id] = []
    elif message.text == 'All players are here':
        roles(message)
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован")


def roles(message):
    global count
    global players
    p = [i for i in players.items()]
    c = len(p)
    print(p, c, count)
    if c <= 6:
        roli = ['мафия' * count, 'мирный житель' * (c - count - 2), 'комиссар', 'путана']
    else:
        roli = ['мафия' * count, 'мирный житель' * (c - count - 3), 'комиссар', 'путана', 'doctor']
    for i in range(c):
        a = random.choice(roli)
        b = random.choice(p)
        print(a, b)
        players[b] = a
        bot.send_message(b, f"Привет! Твоя роль: {a}")
        roli.remove(a)
        p.remove(b)


def main():
    global updater_
    dp = updater_.dispatcher
    conv_handler = ConversationHandler(
        # Точка входа в диалог.
        # В данном случае — команда /start. Она задаёт первый вопрос.
        entry_points=[CommandHandler('start', start)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(Filters.text, get_city)],
            2: [MessageHandler(Filters.text, get_address)],
            3: [MessageHandler(Filters.text, second_start)],
            4: [MessageHandler(Filters.text, get_comments)],
            5: [MessageHandler(Filters.text, text_commands)],
            6: [MessageHandler(Filters.text, get_covid_info_reg)],
            7: [MessageHandler(Filters.text, get_covid_info_coun)]
        },

        fallbacks=[CommandHandler('stop', stop)]
    )
    dp.add_handler(conv_handler)


def start(update, context): # Приветствуем пользователя и просим ввести его данные о геолокации
    global user_city
    global is_admin
    update.message.reply_text(
        'Введите ваш город и адрес, '
        'чтобы разблокировать весь функционал бота')
    update.message.reply_text('Введите город',
                              reply_markup=ReplyKeyboardRemove())
    return 1


def get_city(update, context): # Получаем город пользователя

    global user_city
    user_city = update.message.text
    update.message.reply_text('Введите адрес')
    return 2


def get_address(update, context): # Получаем адрес пользователя

    global user_address
    user_address = update.message.text
    reply_keyboard = [['Да', 'Нет']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(f'Ваш город: {user_city}')
    update.message.reply_text(f'Ваш адрес: {user_address}')
    update.message.reply_text('Вы правильно ввели данные?',
                              reply_markup=markup)
    return 3


bot.polling(none_stop=True)

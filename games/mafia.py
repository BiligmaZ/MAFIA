from telegram import *
import random
import math
from main import keyboard
players = []
count = 0

def func(update, context):
    global players
    global count
    markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text("На сколько человек?", reply_markup=markup)
    if update.message.text.isdigit():
        if int(update.message.text) < 7:
            count = 1
            print(count)
        elif int(update.message.text) > 6:
            count = math.ceil(int(update.message.text) / 4)
            print(count)
        reply_keyboard = [['Начинаем', 'Все игроки на месте']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        update.message.reply_text("В таком случае mafiosi: {count}", reply_markup=markup)

    elif update.message.text == 'Начинаем':
        update.message.reply_text(text="Участники, пожалуйста, поставьте +")
    elif update.message.text == '+':
        players[update.message.from_user.id] = []
    elif update.message.text == 'Все игроки на месте':
        roles(update)


def roles(update):
    global count
    global players
    p = [i for i in players]
    c = len(p)
    if c <= 6:
        roli = ['мафия' * count, 'мирный житель' * (c - count - 2), 'комиссар', 'путана']
    else:
        roli = ['мафия' * count, 'мирный житель' * (c - count - 3), 'комиссар', 'путана', 'doctor']
    for i in range(c):
        a = random.choice(roli)
        b = random.choice(p)
        players[b] = a
        update.message.reply_text(b, f"Привет! Твоя роль: {a}")
        roli.remove(a)
        p.remove(b)

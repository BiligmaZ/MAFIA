from telegram import *
import random
from main import *


def func(update, context):
    reply_keyboard = [['⏪ Вернуться назад']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text("На сколько человек?", reply_markup=markup)


def roles(update):
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

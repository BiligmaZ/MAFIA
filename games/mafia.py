from telegram import *
import random


def func(update, context):
    reply_keyboard = [['⏪ Вернуться назад']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text("На сколько человек?", reply_markup=markup)


def roles(context, players, count):
    p = [i for i in players]
    c = len(p)
    if c <= 6:
        roli = ['мафия' * count, 'мирный житель' * (c - count - 2), 'комиссар', 'путана']
    else:
        roli = ['мафия' * count, 'мирный житель' * (c - count - 3), 'комиссар', 'путана', 'doctor']
    for i in range(c):
        a = random.choice(roli)
        b = random.choice(p)
        context.bot.send_message(chat_id=b, text=f"Твоя роль: {a}")
        roli.remove(a)
        p.remove(b)

import random
import math
import telebot
import telegram
from telebot import types  # для указания типов

bot = telebot.TeleBot("6443463170:AAH1a3G2p72uA2INs3_5_WHgDHB7HlnHIwM")
players = []
count = 0


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
        players.append(message.from_user.id)
    elif message.text == 'All players are here':
        roles(message)
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован")


def roles(message):
    global count
    global players
    p = players.copy()
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
        bot.send_message(b, f"Привет! Твоя роль: {a}")
        roli.remove(a)
        p.remove(b)


bot.polling(none_stop=True)

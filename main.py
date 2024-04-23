import random

import telebot
import telegram
from telebot import types  # для указание типов
from telegram.ext import ConversationHandler

bot = telebot.TeleBot("6443463170:AAH1a3G2p72uA2INs3_5_WHgDHB7HlnHIwM")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Создать комнату")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Начнем игру?".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Создать комнату":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("3-6")
        btn2 = types.KeyboardButton("7-9")
        btn3 = types.KeyboardButton("10-11")
        btn4 = types.KeyboardButton("больше 12")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="На сколько человек?", reply_markup=markup)

    elif message.text == '3-6':
        bot.send_message(message.chat.id, "В таком случае роль мафии отводится одному игроку.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = types.KeyboardButton("Раздать роли на 3-6 человек")
        markup.add(b)
        bot.send_message(message.chat.id,
                         text="Нажми на кнопку, чтобы раздать роли, а остальным нужно поставить +", reply_markup=markup)
    elif message.text == 'Раздать роли на 3-6 человек' or message.text == '+':
        roli = ['мафия', 'мирный житель'] # он короче берет и раздает одну и ту же роль, я хз как сделать условие, чтобы каждому разное было
        a = random.choice(roli)
        if a == 'мафия':
            roli.remove(a)
        bot.send_message(message.from_user.id, f"Привет! Твоя роль: {a}")
    elif message.text == "7-9":
        bot.send_message(message.chat.id, "В таком случае роль мафии отводится двум игрокам.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = types.KeyboardButton("Раздать роли на 7-9 человек")
        markup.add(b)
        bot.send_message(message.chat.id,
                         text="Нажми на кнопку, чтобы раздать роли", reply_markup=markup)
        roles(message)
    elif message.text == "10-11":
        bot.send_message(message.chat.id, "В таком случае роль мафии отводится трем игрокам.")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        b = types.KeyboardButton("Раздать роли на 10-11 человек")
        markup.add(b)
        bot.send_message(message.chat.id,
                         text="Нажми на кнопку, чтобы раздать роли", reply_markup=markup)
        roles(message)
    elif message.text == "больше 12":
        bot.send_message(message.chat.id, "Напишите точное количество.")
    elif message.text:
        bot.send_message(message.chat.id,
                         f'В таком случае, роль мафии отводится {round(int(message.text) / 4)} игрокам.')
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован")


def roles(message):
    if message.text == 'Раздать роли на 3-6 человек':
        bot.send_message(message.chat.id, 'Всем игрокам необходимо поставить +')
        roli = ['мафия', 'мирный житель']
        a = random.choice(roli)
        if a == 'мафия':
            roli.remove(a)
        bot.send_message(message.from_user.id, f"Привет! Твоя роль: {a}")
    elif message.text == 'Раздать роли на 7-9 человек':
        bot.send_message(message.chat.id, 'Всем игрокам необходимо поставить +')
        roli = ['мафия' * 2, 'мирный житель', 'доктор', 'комиссар']
        a = random.choice(roli)
        if a == 'мафия' or a == 'доктор' or a == 'комиссар':
            roli.remove(a)
        bot.send_message(message.from_user.id, f"Привет! Твоя роль: {a}")
    elif message.text == 'Раздать роли на 10-11 человек':
        bot.send_message(message.chat.id, 'Всем игрокам необходимо поставить +')
        roli = ['мафия' * 3, 'мирный житель', 'доктор', 'комиссар', 'путана']
        a = random.choice(roli)
        if a == 'мафия' or a == 'доктор' or a == 'комиссар' or a == 'путана':
            roli.remove(a)
        bot.send_message(message.from_user.id, f"Привет! Твоя роль: {a}")


bot.polling(none_stop=True)

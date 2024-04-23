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
        bot.send_message(message.chat.id, "В таком случае роль мафии отводится одному игроку. Всем игрокам необходимо "
                                          "поставить +")
    elif message.text == '+':
        roles = ['mafia', 'peace']
        bot.send_message(message.from_user.id, f"Привет! Твоя роль: {random.choices(roles)}")

    elif message.text == "7-9":
        bot.send_message(message.chat.id, "В таком случае роль мафии отводится двум игрокам.")
    elif message.text == "10-11":
        bot.send_message(message.chat.id, "В таком случае роль мафии отводится трем игрокам.")
    elif message.text == "больше 12":
        bot.send_message(message.chat.id, "Напишите точное количество.")
    elif message.text:
        bot.send_message(message.chat.id,
                         f'В таком случае, роль мафии отводится {round(int(message.text) / 4)} игрокам.')
    else:
        bot.send_message(message.chat.id, text="На такую команду я не запрограммирован")


bot.polling(none_stop=True)


async def stop(update):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END

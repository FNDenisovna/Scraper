import telebot
from scraper import getFilm

def go():
    bot = telebot.TeleBot('1062147143:AAH9XYPAAxuLQQF4TdXEKZ5CCK49_EXB4xY')

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Привет, что хочешь?')

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, 'Привет, господин')
        elif message.text.lower() == 'пока':
            bot.send_message(message.chat.id, 'Прощай, господин)')
        elif message.text.lower() == 'фильм':
            # pass
            bot.send_message(message.chat.id, getFilm())

    @bot.message_handler(content_types=['sticker'])
    def sticker_id(message):
        print(message)
        bot.send_sticker(message.chat.id, message.file_id)

    bot.polling()

    while True:  # Don't end the main thread.
        pass



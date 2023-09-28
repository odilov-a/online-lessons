import telebot
import os
from telebot import types

BOT_TOKEN = '6692561076:AAGT9fuWjGZmtacHq3o2EzeURCPJk1AQ_S0'
TARGET_GROUP_CHAT_ID = '-1001986050755'
UPLOAD_FOLDER = "public"

bot = telebot.TeleBot(BOT_TOKEN)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user = message.from_user
    full_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    welcome_message = f"Assalomu alaykum {full_name}!"
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    options = ["💳 To'lov qilish", "📑 To'liq ma'lumotlar", "☎️ Biz bilan bog'lanish", "📷 Screenshot yuborish"]
    keyboard.add(*[types.KeyboardButton(option) for option in options])
    bot.send_message(message.chat.id, welcome_message)
    bot.send_message(message.chat.id, "⬇️ Xizmat turini tanlang:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "💳 To'lov qilish")
def handle_payment_option(message):
    with open('photo.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption="💳 Uzcard : 6262720079127836 Turkona Amilova\n💳 VISA : 4023060209774784 Turkona Amilova")

@bot.message_handler(func=lambda message: message.text == "📑 To'liq ma'lumotlar")
def handle_info_option(message):
    with open('picture.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption="📹 Online mobilografiya intensiv kursi\n📹 Kurs Turkona Amilova mentorligida olib boriladi")

@bot.message_handler(func=lambda message: message.text == "☎️ Biz bilan bog'lanish")
def handle_send_string(message):
    custom_string = "📝 Admin : @online_mobilografiya\n☎️ Telefon raqam : +998 90 817 95 18"
    bot.send_message(message.chat.id, custom_string)

@bot.message_handler(func=lambda message: message.text == "📷 Screenshot yuborish")
def handle_send_photo_request(message):
    bot.send_message(message.chat.id, "📷 Screenshotni yuboring!")

@bot.message_handler(content_types=['photo'])
def handle_uploaded_photo(message):
    user = message.from_user
    full_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    username = user.username
    if message.photo:
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        photo_path = os.path.join(UPLOAD_FOLDER, f"{file_id}.jpg")
        with open(photo_path, 'wb') as photo_file:
            photo_file.write(downloaded_file)
        bot.send_message(message.chat.id, "📷 Screenshot yuborildi admin javobini kuting!")
        caption = f"Yuboruvchi: {full_name}\nUsername: @{username}"
        with open(photo_path, 'rb') as uploaded_photo:
            bot.send_photo(TARGET_GROUP_CHAT_ID, uploaded_photo, caption=caption)

if __name__ == '__main__':
    bot.polling(none_stop=True)
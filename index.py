import telebot
import os
from telebot import types


BOT_TOKEN = '6649575383:AAFSpP5Fmwcl4SjAnglEWJlYmD-xf3CO4R4'
TARGET_GROUP_CHAT_ID = '-1001986050755'
UPLOAD_FOLDER = "public"

bot = telebot.TeleBot(BOT_TOKEN)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user = message.from_user
    full_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    welcome_message = f"Assalomu alaykum <b>{full_name}</b> \n\nhttps://telegra.ph/Mobilografiya-nima-Va-kursimda-nimalar-orgataman-Qisqacha-bilib-oling-04-17"
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    options = ["💳 To'lov qilish", "📑 Ma'lumotlar", "☎️ Biz bilan bog'lanish", "📷 Screenshot yuborish", "📚 To'liq ma'lumotlar"]
    with open('photos.png', 'rb') as photo_file:
        bot.send_photo(message.chat.id, photo_file)

    keyboard.add(*[types.KeyboardButton(option) for option in options])
    bot.send_message(message.chat.id, welcome_message, parse_mode='HTML')
    bot.send_message(message.chat.id, "<b>Xizmat turini tanlang:</b>", reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == "💳 To'lov qilish")
def handle_payment_option(message):
    with open('photo.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, parse_mode='HTML', caption="💳 <b>Uzcard : 6262720079127836 Turkona Amilova</b>\n💳 <b>VISA : 4023060209774784 Turkona Amilova</b>")

@bot.message_handler(func=lambda message: message.text == "📑 Ma'lumotlar")
def handle_info_option(message):
    with open('picture.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, parse_mode='HTML', caption="📹 <b>Online mobilografiya intensiv kursi\n📹 Kurs Turkona Amilova mentorligida olib boriladi</b>")

@bot.message_handler(func=lambda message: message.text == "☎️ Biz bilan bog'lanish")
def handle_send_string(message):
    custom_string = "📝 <b>Admin : @online_mobilografiya\n☎️ Telefon raqam : +998 90 817 95 18</b>"
    bot.send_message(message.chat.id, custom_string, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text == "📚 To'liq ma'lumotlar")
def handle_full_documents(message):
    full_documents_link = "https://telegra.ph/Mobilografiya-nima-Va-kursimda-nimalar-orgataman-Qisqacha-bilib-oling-04-17"
    bot.send_message(message.chat.id, full_documents_link)

@bot.message_handler(func=lambda message: message.text == "📷 Screenshot yuborish")
def handle_send_photo_request(message):
    bot.send_message(message.chat.id, "📷 <b>Screenshotni yuboring!</b>", parse_mode='HTML')

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
        bot.send_message(message.chat.id, "📷 <b>Screenshot yuborildi admin javobini kuting!</b>", parse_mode='HTML')
        caption = f"Yuboruvchi: {full_name}\nUsername: @{username}"
        with open(photo_path, 'rb') as uploaded_photo:
            bot.send_photo(TARGET_GROUP_CHAT_ID, uploaded_photo, caption=caption)

if __name__ == '__main__':
    bot.polling(none_stop=True)
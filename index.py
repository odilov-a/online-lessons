import telebot
from telebot import types

BOT_TOKEN = '6649575383:AAHKtI5ZiPIJbt6m_lLwVc35E6iZqm4GgsI'
TARGET_GROUP_CHAT_ID = '-1001986050755'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user = message.from_user
    full_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    welcomes_message = "https://telegra.ph/Mobilografiya-nima-Va-kursimda-nimalar-orgataman-Qisqacha-bilib-oling-04-17"
    welcome_message = f"Assalomu alaykum <b>{full_name}</b>\n\n{welcomes_message}!"
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    options = ["💳 To'lov qilish", "📑 Ma'lumotlar", "📷 Screenshot yuborish", "☎️ Biz bilan bog'lanish", "📚 To'liq ma'lumotlar"]
    keyboard.add(*[types.KeyboardButton(option) for option in options])
    bot.send_message(message.chat.id, welcome_message, parse_mode='HTML')
    bot.send_message(message.chat.id, "<b>Xizmat turini tanlang:</b>", parse_mode='HTML', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "💳 To'lov qilish")
def handle_payment_option(message):
    with open('photo.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, parse_mode='HTML', caption="💳 <b>Uzcard</b> : 6262720079127836 <b>Turkona Amilova</b>\n💳 <b>VISA</b> : 4023060209774784 <b>Turkona Amilova</b>")

@bot.message_handler(func=lambda message: message.text == "📚 To'liq ma'lumotlar")
def handle_full_documents(message):
    full_documents_link = "https://telegra.ph/Mobilografiya-nima-Va-kursimda-nimalar-orgataman-Qisqacha-bilib-oling-04-17"
    bot.send_message(message.chat.id, full_documents_link)

@bot.message_handler(func=lambda message: message.text == "📑 Ma'lumotlar")
def handle_info_option(message):
    with open('picture.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, parse_mode='HTML', caption="📹 Online mobilografiya intensiv kursi\n📹 Kurs <b>Turkona Amilova</b> mentorligida olib boriladi")

@bot.message_handler(func=lambda message: message.text == "☎️ Biz bilan bog'lanish")
def handle_send_string(message):
    custom_string = "📝 <b>Admin</b> : @online_mobilografiya\n☎️ <b>Telefon raqam</b> : +998 90 817 95 18"
    bot.send_message(message.chat.id, custom_string, parse_mode='HTML')

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
        photo_path = f"{file_id}.jpg"
        with open(photo_path, 'wb') as photo_file:
            photo_file.write(downloaded_file)
        bot.send_message(message.chat.id, "📷 Screenshot yuborildi admin javobini kuting!")
        caption = f"Yuboruvchi: {full_name}\nUsername: @{username}"
        with open(photo_path, 'rb') as uploaded_photo:
            bot.send_photo(TARGET_GROUP_CHAT_ID, uploaded_photo, caption=caption)

if __name__ == '__main__':
    bot.polling(none_stop=True)
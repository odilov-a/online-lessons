const TelegramBot = require('node-telegram-bot-api');
const TOKEN = '6649575383:AAFSpP5Fmwcl4SjAnglEWJlYmD-xf3CO4R4';
const TARGET_GROUP_CHAT_ID = '-1001986050755';

const bot = new TelegramBot(TOKEN, { polling: true });

bot.onText(/\/start/, (msg) => {
  const user = msg.from;
  const full_name = user.last_name ? `${user.first_name} ${user.last_name}` : user.first_name;
  const welcomes_message = "https://telegra.ph/Mobilografiya-nima-Va-kursimda-nimalar-orgataman-Qisqacha-bilib-oling-04-17";
  const welcome_message = `Assalomu alaykum <b>${full_name}</b>\n\n${welcomes_message}!`;

  const keyboard = {
    reply_markup: {
      resize_keyboard: true,
      keyboard: [
        ["💳 To'lov qilish", "📑 Ma'lumotlar"],
        ["📷 Screenshot yuborish", "☎️ Biz bilan bog'lanish"],
        ["📚 To'liq ma'lumotlar"]
      ]
    },
    parse_mode: 'HTML'
  };

  bot.sendMessage(msg.chat.id, welcome_message, keyboard);
});

bot.onText(/💳 To'lov qilish/, (msg) => {
  const paymentInfo = "💳 <b>Uzcard</b> : 6262720079127836 <b>Turkona Amilova</b>\n💳 <b>VISA</b> : 4023060209774784 <b>Turkona Amilova</b>";
  bot.sendPhoto(msg.chat.id, 'photo.jpg', { caption: paymentInfo, parse_mode: 'HTML' });
});

bot.onText(/📚 To'liq ma'lumotlar/, (msg) => {
  const full_documents_link = "https://telegra.ph/Mobilografiya-nima-Va-kursimda-nimalar-orgataman-Qisqacha-bilib-oling-04-17";
  bot.sendMessage(msg.chat.id, full_documents_link);
});

bot.onText(/📑 Ma'lumotlar/, (msg) => {
  const courseInfo = "📹 Online mobilografiya intensiv kursi\n📹 Kurs <b>Turkona Amilova</b> mentorligida olib boriladi";
  bot.sendPhoto(msg.chat.id, 'picture.jpg', { caption: courseInfo, parse_mode: 'HTML' });
});

bot.onText(/☎️ Biz bilan bog'lanish/, (msg) => {
  const adminInfo = "📝 <b>Admin</b> : @online_mobilografiya\n☎️ <b>Telefon raqam</b> : +998 90 817 95 18";
  bot.sendMessage(msg.chat.id, adminInfo, { parse_mode: 'HTML' });
});

bot.onText(/📷 Screenshot yuborish/, (msg) => {
  bot.sendMessage(msg.chat.id, "📷 Screenshotni yuboring!");
});

bot.on('photo', (msg) => {
  const user = msg.from;
  const full_name = user.last_name ? `${user.first_name} ${user.last_name}` : user.first_name;
  const username = user.username;
  const file_id = msg.photo[msg.photo.length - 1].file_id;

  bot.downloadFile(file_id).then((filePath) => {
    const photo_path = filePath;
    bot.sendMessage(msg.chat.id, "📷 Screenshot yuborildi admin javobini kuting!");
    const caption = `Yuboruvchi: ${full_name}\nUsername: @${username}`;
    bot.sendPhoto(TARGET_GROUP_CHAT_ID, photo_path, { caption });
  });
});

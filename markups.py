from aiogram.types import ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton , KeyboardButton


# Главное меню
btnInfo = KeyboardButton("📚Информация")
btnVp = KeyboardButton("🦴Для чего этот бот?")
btnCha = KeyboardButton("🌎Ссылки")
btnNn = KeyboardButton("⚡Последние новости")
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnInfo,btnVp,btnCha,btnNn)

#SyatovMenu
btnRas = KeyboardButton("🌎Информация про покупку")
btnDd = KeyboardButton("🔗Главное меню")
btnDc = KeyboardButton("💳Расценки")
otherMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnRas,btnDd,btnDc)


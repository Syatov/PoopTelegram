import logging
from aiogram import Bot , Dispatcher ,executor , types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton , InlineKeyboardButton , InlineKeyboardMarkup
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import random
import markups as nav


TOKEN = ""


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, '{0.first_name}'.format(message.from_user), reply_markup= nav.mainMenu)
@dp.message_handler(commands=['syatov'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'привет Амир'.format(message.from_user), reply_markup= nav.otherMenu)

@dp.message_handler()
async def command_start(message: types.Message):
    if message.text == "🔗Главное меню":
        await bot.send_message(message.from_user.id,"🔗Главное меню" ,reply_markup= nav.mainMenu)
    
    elif message.text == "C10H15N":
        await bot.send_message(message.from_user.id, "Ну привет)",reply_markup= nav.otherMenu)

    elif message.text == "c10h15n":
        await bot.send_message(message.from_user.id, "Ну привет)",reply_markup= nav.otherMenu)

    elif message.text == "C10h15n":
        await bot.send_message(message.from_user.id, "Ну привет)",reply_markup= nav.otherMenu)
    
    elif message.text == "📚Информация":
        await bot.send_message(message.from_user.id, "PoopLand это в первую очередь сервер Сонечки.\nНаш сервер не похож ни на один из других. У вас\nне получится забиться в один угол и сидеть в дали\nот всех, всё завязано на РП. Экономика нашего\nсервера будет зависеть от фермы вашего города,\nвыбранной жеребьёвкой. На этом сервере есть\nинтересные плагины.\nПокупая данный товар, вы получаете доступ к\nигровому серверу PoopLand. Для входа и \nигры на данном сервере вам нужно иметь \nлицензионную копию игры для ПК Minecraft\nJava Edition и широкополосный доступ к сети Интернет.\n \n \nСоздатель тг - @syatov")
    
    elif message.text == "🌎Информация про покупку":
        await bot.send_message(message.from_user.id,"Коротко о том как делается покупка : \n 1 вы переводите деньги на карту \n 2 отписываете диллеру о покупке и кидайте что хотите\n 3 После того как все пройдет успешно вы получите координаты закладки\n \n Если вам интерсно о гарантии : боже чел ты покупаеш наркоту какая гарантия?")
    
    elif message.text == '💳Расценки':
        await bot.send_message(message.from_user.id,"✅В наличии:\nКодеинчик🥤\n• Зелье силы II - 1 ар за 2 зелья\n\nЛирика🤪\n• Зелье огнестоикости 8 мин - 1 ар за 2 зелья\n\nКрокодил 🐊💉\n• Зелье моментального уронаII(взрывное) - 1 ар за зелье\n\nКсанакс💊\n• Зелье отравления II(взрывное) - 1 ар за 2 зелья")

    elif message.text == "🦴Для чего этот бот?":
        await bot.send_message(message.from_user.id, "Пока что я могу давать информацию и новости.\n Со временем кодер сделает больше функционала")

    elif message.text == "🌎Ссылки":
        await bot.send_message(message.from_user.id, "Группа вк - https://vk.com/poop_land")

    elif message.text == "⚡Последние новости":
        await bot.send_message(message.from_user.id,"Здравствуйте дорогие жители Пупленда. В связи с тем, что у нас не будет государственной торговой федерации Вводится:-обязательная регистрация у минфина @Lelush_Iz_Butovo ваших одиночных магазинов/аналогов торговых федераций, других видов не рп-бизнесов;- еженедельный налоговый сбор за афк-торговлю, сумма которого 2ар с задействованной бочки/сундука(не подлежат налоговому сбору творческие и рп товары);-для всех остальных видов не рп-торговли фиксированный налог 32 ар в неделю;-если ваш афк-магащин работает без лицензии, вам будет выставлен штраф 10 стаков ар. Те магазины и аналоги ТФ, которые действуют сейчас, имеют неделю на то, чтобы обратится за регистрацией к @Lelush_Iz_Butovo .Всего хорошего и удачного завершения семестра пупы")

    else :
        await message.reply("⛔Неизвестная команда")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



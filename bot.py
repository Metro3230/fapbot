from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from PIL import Image, ImageEnhance
import os

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
workdir = os.getcwd()

def add_to_log(val, path):                    #added value to log file if this value is not there 
    with open(path, 'r+') as file:
        file_set = set(line.strip() for line in file)
        if str(val) not in file_set:
            file.write(f'\n{val}')



@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nПришли мне картинку, и я подрочу на неё!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Пришли мне картинку, и я подрочу на неё!")
    
    
@dp.message_handler(commands=['id'])
async def send_welcome(message: types.Message):    
    await message.reply(message.chat.id)
  
    
@dp.message_handler()
async def echo_message(msg: types.Message):
    usrid = msg.from_user.id
    text = msg.text
    if(text == 'Крыса' or text == 'крыса' or text == '🐀'):
        await bot.send_message(usrid, 'нет')
    else:
        await bot.send_message(usrid, 'Я не дрочу на буквы!')
    add_to_log(usrid, workdir + '/log.txt')
    await bot.send_message(-931442766, f'Username: {msg.from_user.first_name}\nMsg: {text}\nId: {usrid}')   #отправляем во второй чят


@dp.message_handler(content_types=["photo"])    
async def get_photo(message):
    usrid = message.from_user.id    
    caption = message.caption
    first_name = message.from_user.first_name
#    file_info = await bot.get_file(message.photo[-1].file_id)
    await message.photo[-1].download(destination_file=workdir + '/photo/send-' + message.photo[-1].file_unique_id + '.jpg')
    img = Image.open(workdir + '/photo/send-' + message.photo[-1].file_unique_id + '.jpg')
    hand = Image.open(workdir + '/photo/hand.png') 
    towidth = int(img.size[0])   #   До какой ширины растянуть руку.  0 - width   1 - height
    hsize = int((float(hand.size[1])*float(towidth/float(hand.size[0]))))                       # Формула подстройки высоты относительно нужной ширины
    hand = hand.resize((towidth,hsize), Image.Resampling.LANCZOS)                               #растягиваем
    zeropoint = int(img.size[1]) - hsize                                                        #начальная точка руки (что бы она была в левом нижнем углу)
    img.paste(hand, (0, zeropoint),  hand)                                                      #вставляем в нужное место
    img.save(workdir + '/photo/send-' + message.photo[-1].file_unique_id + '_hand.jpg')       #временно сохраняем
    await bot.send_photo(-931442766, message.photo[-1].file_id, caption=f'Username: {first_name}\nMsg: {caption}\nId: {usrid}')           #отправляем в мой другой чят
    await bot.send_photo(usrid, types.InputFile(workdir + '/photo/send-' + message.photo[-1].file_unique_id + '_hand.jpg'))   #отправляем измененное 
    add_to_log(usrid, workdir + '/log.txt')
    os.remove(workdir + '/photo/send-' + message.photo[-1].file_unique_id + '_hand.jpg')     #удаляем
    os.remove(workdir + '/photo/send-' + message.photo[-1].file_unique_id + '.jpg')



if __name__ == '__main__':
    executor.start_polling(dp)
    





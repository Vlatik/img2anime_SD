import os
from typing import Any, Dict

from aiogram import Bot, Router, types
from aiogram.types import (
    Message,
    FSInputFile,
)
from aiogram.filters import Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.botSI import img2img

date0 = os.getcwd()

router = Router()

@router.message()
async def search(message: types.Message, bot: Bot):
    date = date0 + '/img/' + message.from_user.full_name + '/'
    if message.photo:
        res0 = await bot.get_file(message.photo[-1].file_id)
        await bot.download_file(res0.file_path, date + message.from_user.full_name + '.png')
        ref = date + message.from_user.full_name + '.png'
    prompt = date + message.from_user.full_name + '.txt'
    im = img2img(prompt, ref)
    img = FSInputFile(im)
    with open(prompt, "r") as text_file:
        lines = text_file.readlines()
    if int(lines[5]) == 0:
        PromptT = lines[0]
        ds = lines[2]
        col = 'Colorize Off'
        if int(lines[4]) == 0:
            ad = 'Adetailer Off'
        else:
            ad = 'Adetailer On'
    else:
        PromptT = lines[1]
        ds = '1' + '\n'
        ad = 'Adetailer Off'
        col = 'Colorize On'
    Cap = int(lines[6])
    st = lines[7].split('=')[0]
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text = 'Redo',
        callback_data='search')
    )
    if Cap == 1:
       Caption = (
                f"User nickname:  {message.from_user.full_name}" + '\n' + '\n'
                f'Prompt:  {PromptT}'
                f'Style:  {st}' + '\n'
                f'{ad},   ' + col + '\n'
                f'Denoising strength:  {ds}'
                f'Resolution:  {lines[3]}' + '\n'
                'Press the button to generate a picture with another seed'
       ) 
       await message.reply_photo(photo=img, caption=Caption, reply_markup=builder.as_markup())
    else:
        await message.reply_photo(photo=img, reply_markup=builder.as_markup())

@router.callback_query(Text('search'))
async def search(callback: types.CallbackQuery):
    date = date0 + '/img/' + callback.from_user.full_name + '/'
    ref = date + callback.from_user.full_name + '.png'
    prompt = date + callback.from_user.full_name + '.txt'
    im = img2img(prompt, ref)
    img = FSInputFile(im)
    with open(prompt, "r") as text_file:
        lines = text_file.readlines()
    if int(lines[5]) == 0:
        PromptT = lines[0]
        ds = lines[2]
        col = 'Colorize Off'
        if int(lines[4]) == 0:
            ad = 'Adetailer Off'
        else:
            ad = 'Adetailer On'
    else:
        PromptT = lines[1]
        ds = '1' + '\n'
        ad = 'Adetailer Off'
        col = 'Colorize On'
    Cap = int(lines[6])
    st = lines[7].split('=')[0]
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text = 'Redo',
        callback_data='search')
    )
    if Cap == 1:
       Caption = (
                f"User nickname:  {callback.from_user.full_name}" + '\n' + '\n'
                f'Prompt:  {PromptT}'
                f'Style:  {st}' + '\n'
                f'{ad},   ' + col + '\n'
                f'Denoising strength:  {ds}'
                f'Resolution:  {lines[3]}' + '\n'
                'Press the button to generate a picture with another seed'
       ) 
       await callback.message.reply_photo(photo=img, caption=Caption, reply_markup=builder.as_markup())
    else:
        await callback.message.reply_photo(photo=img, reply_markup=builder.as_markup())
    await callback.answer()
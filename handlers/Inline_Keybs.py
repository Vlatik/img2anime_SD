from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

builder = InlineKeyboardBuilder()
ib1 = types.InlineKeyboardButton(text = 'none',
        callback_data='none=, ')
ib2 = types.InlineKeyboardButton(text = 'Ghibli',
        callback_data='Ghibli=, <lora:studioGhibliStyle_offset:')
ib3 = types.InlineKeyboardButton(text = 'Gravity_falls',
        callback_data='Gravity_falls=, <lora:gravityfalls:')
ib4 = types.InlineKeyboardButton(text = 'FlatColor',
        callback_data='FlatColor=, <lora:LORAFlatColor_flatColor:')
ib5 = types.InlineKeyboardButton(text = 'Minimalist',
        callback_data='Minimalist=, <lora:anime_minimalist_v1:')
ib6 = types.InlineKeyboardButton(text = 'Magotsuki',
        callback_data='Magotsuki=, <lora:Magotsuki:')
ib7 = types.InlineKeyboardButton(text = 'Dark',
        callback_data='Dark=, <lora:lowra_v10:')
ib8 = types.InlineKeyboardButton(text = 'Concept',
        callback_data='Concept=, <lora:concept:')
ib9 = types.InlineKeyboardButton(text = 'Blame',
        callback_data='Blame=, <lora:cibo:')
ib10 = types.InlineKeyboardButton(text = 'Pixel',
        callback_data='Pixel=, <lora:pixel_f2:')
ib11 = types.InlineKeyboardButton(text = 'Handdraw',
        callback_data='Handdraw=, <lora:handdraw:')
ib12 = types.InlineKeyboardButton(text = 'Arcane',
        callback_data='Arcane=, <lora:arcaneStyleLora_offset:')


builder.row(ib1,ib2,ib3).row(ib4,ib5,ib6).row(ib7,ib8,ib9).row(ib10,ib11,ib12)


builderStr = InlineKeyboardBuilder()
builderStr.add(
    types.InlineKeyboardButton(
        text = '0.6 ',
        callback_data='0.5'),
    types.InlineKeyboardButton(
        text = '0.7',
        callback_data='0.7'),
    types.InlineKeyboardButton(
        text = '0.8',
        callback_data='0.8'),
    types.InlineKeyboardButton(
        text = '0.9',
        callback_data='0.9'),
    types.InlineKeyboardButton(
        text = '1',
        callback_data='1'),
)
import os
from typing import Any, Dict

from aiogram import Bot, Dispatcher, F, Router, html, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Text
from aiogram.types import (
    Message,
    FSInputFile,
)
from handlers.Router_commands_defs import commP, commO
from handlers.Inline_Keybs import builder, builderStr

date0 = os.getcwd()

form_router = Router()

start_answer = (
        f"write requests after the command" + '\n'
        f"to set a command to its default state send d" + '\n' + '\n' + '\n'
        f"Commands:" + '\n' + '\n'
        f"/p - Prompt.   Write a prompt." + '\n' + "Default: (masterpiece, best quality:1.4), (flat color:1.4),(colorful:1.4), eye contact, solo,floating colorful water,(2D:1.4),beautiful eyes,eyes detailed" + '\n' + '\n'
        f"/pc - Prompt Colorize.   Write a prompt to lineart." + '\n' + "Default: a ginger girl, red eyes" + '\n' + '\n'
        f"/style - Style.   Choose a style of generated image." + '\n' + "Default: Ghibli" + '\n' + '\n'
        f"/ds - Denoising strength [0..1].   To control a creativity of AI." + '\n' + "Default: 0.5" + '\n' + '\n'
        f"/res - Smallest side resolution [0..768].   Must be divisible by 8. 512, 640, 768 are useful in most cases." + '\n' + "Default: 512" + '\n' + '\n'
        f"/ad - ADetailer [off or on].   If the face in the image is small, set the value to On." + '\n' + "Default: On" + '\n' + '\n'
        f"/col - Colorize [off or on].   To colorize lineart or manga." + '\n' + "Default: Off" + '\n' + '\n'
        f"/cap - Caption [off or on].   Add a caption with your settings to generated photo." + '\n' + "Default: On" + '\n' + '\n'
    )

with open('default_settings.txt', "r") as text_file:
            lines0 = text_file.readlines()

class Form(StatesGroup):
    Prompt = State()
    PromptC = State()
    DenStr = State()
    Resolution = State()
    ADetailer = State()
    Colorize = State()
    Caption = State()
    Style = State()
    StyleStr = State()


@form_router.message(Command("start"))
async def command_start(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hey, <b>{message.from_user.full_name}!</b>, this is a bot for style your image")
    await message.answer(start_answer)
    ref = FSInputFile(r"ref.png")
    mem = FSInputFile(r"mem.png")
    await message.answer_photo(ref)
    await message.answer_photo(mem)
    await message.answer(f"if the bot doen't generate a picture update it with the command /start. Or the bot is off)")
    
    date = date0 + '/img/' + message.from_user.full_name + '/'
    if not os.path.exists(date):
        os.mkdir(date)
    prompt = date + message.from_user.full_name + '.txt'
    lines = lines0
    with open(prompt, "w") as text_file:
            for  line in lines:
                text_file.write(line)
    


@form_router.message(Command("p"))
async def search(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.Prompt)
@form_router.message(Form.Prompt)
async def search(message: Message, state: FSMContext):
    await state.update_data(Prompt=message.text)
    date = date0 + '/img/' + message.from_user.full_name + '/' + message.from_user.full_name + '.txt'
    if message.text:
        comm = message.text
        commP(date, comm, 0)
    await message.answer(f'prompt recorded')
    await state.clear()
         
@form_router.message(Command("pc"))
async def search(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.PromptC)
@form_router.message(Form.PromptC)
async def search(message: Message, state: FSMContext):
    await state.update_data(PromptC=message.text)
    date = date0 + '/img/' + message.from_user.full_name + '/' + message.from_user.full_name + '.txt'
    if message.text:
        comm = message.text
        commP(date, comm, 1)
    await message.answer(f'promptC recorded')
    await state.clear()

@form_router.message(Command("ds"))
async def search(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.DenStr)
@form_router.message(Form.DenStr)
async def search(message: Message, state: FSMContext):
    await state.update_data(DenStr=message.text)
    date = date0 + '/img/' + message.from_user.full_name + '/' + message.from_user.full_name + '.txt'
    if message.text:
        comm = message.text
        commP(date, comm, 2)
    await message.answer(f'denoising strength recorded')
    await state.clear()

@form_router.message(Command("res"))
async def search(state: FSMContext) -> None:
    await state.set_state(Form.Resolution)
@form_router.message(Form.Resolution)
async def search(message: Message, state: FSMContext):
    await state.update_data(Resolution=message.text)
    date = date0 + '/img/' + message.from_user.full_name + '/' + message.from_user.full_name + '.txt'
    if message.text:
        comm = message.text
        commP(date, comm, 3)
    await message.answer(f'min res recorded')
    await state.clear()



@form_router.message(Command(commands=["ad"]))
async def search(message: types.Message, bot: Bot):
    await bot.send_chat_action(message.chat.id, action='typing')
    date = date0 + '/img/' + message.from_user.full_name + '/' + message.from_user.full_name + '.txt'
    line = commO(date, 4)
    if int(line) == 0:
        await message.answer(f'ADetailer off')
    else:
        await message.answer(f'ADetailer on')

@form_router.message(Command(commands=["col"]))
async def search(message: types.Message, bot: Bot):
    await bot.send_chat_action(message.chat.id, action='typing')
    date = date0 + '/img/' + message.from_user.full_name + '/' + message.from_user.full_name + '.txt'
    line = commO(date, 5)
    if int(line) == 0:
        await message.answer(f'Colorize off')
    else:
        await message.answer(f'Colorize on')

@form_router.message(Command(commands=["cap"]))
async def search(message: types.Message, bot: Bot):
    await bot.send_chat_action(message.chat.id, action='typing')
    date = date0 + '/img/' + message.from_user.full_name + '/' + message.from_user.full_name + '.txt'
    line = commO(date, 6)
    if int(line) == 0:
        await message.answer(f'Caption off')
    else:
        await message.answer(f'Caption on')


@form_router.message(Command("style"))
async def search(message: Message, state: FSMContext) -> None:
    await message.answer('choise style',reply_markup=builder.as_markup())
    await state.set_state(Form.Style)
    

@form_router.callback_query(Form.Style)
async def search(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(Style = callback.data)
    date = date0 + '/img/' + callback.from_user.full_name + '/' + callback.from_user.full_name + '.txt'
    if callback.data == 'none=, ':
        with open(date, "r") as text_file:
            lines = text_file.readlines()
        lines[7] = ' = '
        with open(date, "w") as text_file:
            text_file.writelines(lines)
        await callback.message.answer(f'Style: none',)
        await callback.answer()
        await state.clear()
    else:
        await callback.message.answer('set Lora strength',reply_markup=builderStr.as_markup())
        await state.set_state(Form.StyleStr)
        await callback.answer()

@form_router.callback_query(Form.StyleStr)
async def search(callback: types.CallbackQuery, state: FSMContext):
    stystr = callback.data
    await state.update_data(StyleStr = stystr)
    data = await state.get_data()
    style = data['Style']
    date = date0 + '/img/' + callback.from_user.full_name + '/' + callback.from_user.full_name + '.txt'
    with open(date, "r") as text_file:
        lines = text_file.readlines()
    lines[7] = style + stystr + '>' + '\n'
    with open(date, "w") as text_file:
        text_file.writelines(lines)
    await callback.message.answer(f'Style: ' + lines[7].split('=')[0] + '(' + stystr + ')')
    await callback.answer()
    await state.clear()



import os
from typing import Any, Dict

from aiogram import Bot, Dispatcher, F, Router, html, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    Message,
    FSInputFile,
)

date0 = os.getcwd()

form_router = Router()

start_answer = (
        f"write requests after the command" + '\n'
        f"to set a command to its default state send d" + '\n' + '\n' + '\n'
        f"Commands:" + '\n' + '\n'
        f"/p - Prompt.   Write a prompt." + '\n' + "Default: (masterpiece, best quality:1.4), (flat color:1.4),(colorful:1.4), eye contact, solo,floating colorful water,(2D:1.4),beautiful eyes,eyes detailed" + '\n' + '\n'
        f"/pc - Prompt Colorize.   Write a prompt to lineart." + '\n' + "Default: a ginger girl, red eyes" + '\n' + '\n'
        f"/ds - Denoising strength [0..1].   To control a creativity of AI." + '\n' + "Default: 0.5" + '\n' + '\n'
        f"/res - Smallest side resolution [0..768].   Must be divisible by 8. 512, 640, 768 are useful in most cases." + '\n' + "Default: 512" + '\n' + '\n'
        f"/ad - ADetailer [off or on].   If the face in the image is small, set the value to On." + '\n' + "Default: On" + '\n' + '\n'
        f"/col - Colorize [off or on].   To colorize lineart or manga." + '\n' + "Default: Off" + '\n' + '\n'
        f"/cap - Caption [off or on].   Add a caption with your settings to generated photo." + '\n' + "Default: On" + '\n' + '\n'
    )

class Form(StatesGroup):
    Prompt = State()
    PromptC = State()
    DenStr = State()
    Resolution = State()
    ADetailer = State()
    Colorize = State()
    Caption = State()


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
    lines = [
            '(masterpiece, best quality:1.4), (flat color:1.4),(colorful:1.4), eye contact, solo,floating colorful water,(2D:1.4),beautiful eyes,eyes detailed, closed mouth',
            'a ginger girl, red eyes',
            '0.5',
            '512', 
            '1', 
            '0', 
            '1',
    ]
    with open(prompt, "w") as text_file:
            for  line in lines:
                text_file.write(line + '\n')


@form_router.message(Command("p"))
async def search(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.Prompt)
@form_router.message(Form.Prompt)
async def search(message: Message, state: FSMContext) -> None:
    await state.update_data(Prompt=message.text)
    date = date0 + '/img/' + message.from_user.full_name + '/'
    prompt = date + message.from_user.full_name + '.txt'
    if message.text:
        res0 = message.text
        with open(prompt, "r") as text_file:
            lines = text_file.readlines()
        if res0 == 'd':
            lines[0] = '(masterpiece, best quality:1.4), (flat color:1.4),(colorful:1.4), eye contact, solo,floating colorful water,(2D:1.4),beautiful eyes,eyes detailed, closed mouth' + '\n'
        else:
            lines[0] = res0 + '\n'
        with open(prompt, "w") as text_file:
            text_file.writelines(lines)
        await message.answer(f'prompt recorded')
        await state.clear()



@form_router.message(Command("pc"))
async def search(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.PromptC)
@form_router.message(Form.PromptC)
async def search(message: Message, state: FSMContext) -> None:
    await state.update_data(PromptC=message.text)
    date = date0 + '/img/' + message.from_user.full_name + '/'
    prompt = date + message.from_user.full_name + '.txt'
    if message.text:
        res0 = message.text
        with open(prompt, "r") as text_file:
            lines = text_file.readlines()
        if res0 == 'd':
            lines[1] = 'a ginger girl, red eyes' + '\n'
        else:
            lines[1] = res0 + '\n'
        with open(prompt, "w") as text_file:
            text_file.writelines(lines)
        await message.answer(f'prompt recorded')
        await state.clear()


@form_router.message(Command("ds"))
async def search(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.DenStr)
@form_router.message(Form.DenStr)
async def search(message: Message, state: FSMContext) -> None:
    await state.update_data(DenStr=message.text)
    date = date0 + '/img/' + message.from_user.full_name + '/'
    prompt = date + message.from_user.full_name + '.txt'
    if message.text:
        res0 = message.text
        with open(prompt, "r") as text_file:
            lines = text_file.readlines()
        if res0 == 'd':
            lines[2] = '0.5' + '\n'
        else:
            lines[2] = res0 + '\n'
        with open(prompt, "w") as text_file:
            text_file.writelines(lines)
        await message.answer(f'denoising strength recorded')
        await state.clear()


@form_router.message(Command("res"))
async def search(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.Resolution)
@form_router.message(Form.Resolution)
async def search(message: Message, state: FSMContext) -> None:
    await state.update_data(Resolution=message.text)
    date = date0 + '/img/' + message.from_user.full_name + '/'
    prompt = date + message.from_user.full_name + '.txt'
    if message.text:
        res0 = message.text
        with open(prompt, "r") as text_file:
            lines = text_file.readlines()
        if res0 == 'd':
            lines[3] = '512' + '\n'
        else:
            lines[3] = res0 + '\n'
        with open(prompt, "w") as text_file:
            text_file.writelines(lines)
        await message.answer(f'min res recorded')
        await state.clear()



@form_router.message(Command(commands=["ad"]))
async def search(message: types.Message, bot: Bot):
    await bot.send_chat_action(message.chat.id, action='typing')
    date = date0 + '/img/' + message.from_user.full_name + '/'
    prompt = date + message.from_user.full_name + '.txt'
    with open(prompt, "r") as text_file:
        lines = text_file.readlines()
    if int(lines[4]) == 0:
        lines[4] = '1' + '\n'
    else:
        lines[4] = '0' + '\n'
    with open(prompt, "w") as text_file:
        text_file.writelines(lines)
    if int(lines[4]) == 0:
        await message.answer(f'ADetailer off')
    else:
        await message.answer(f'ADetailer on')


@form_router.message(Command("col"))
async def search(message: types.Message, bot: Bot):
    await bot.send_chat_action(message.chat.id, action='typing')
    date = date0 + '/img/' + message.from_user.full_name + '/'
    prompt = date + message.from_user.full_name + '.txt'
    with open(prompt, "r") as text_file:
        lines = text_file.readlines()
    if int(lines[5]) == 0:
        lines[5] = '1' + '\n'
    else:
        lines[5] = '0' + '\n'
    with open(prompt, "w") as text_file:
        text_file.writelines(lines)
    if int(lines[5]) == 0:
        await message.answer(f'Colorize off')
    else:
        await message.answer(f'Colorize on')


@form_router.message(Command("cap"))
async def search(message: types.Message, bot: Bot):
    await bot.send_chat_action(message.chat.id, action='typing')
    date = date0 + '/img/' + message.from_user.full_name + '/'
    prompt = date + message.from_user.full_name + '.txt'
    with open(prompt, "r") as text_file:
        lines = text_file.readlines()
    if int(lines[6]) == 0:
        lines[6] = '1' + '\n'
    else:
        lines[6] = '0' + '\n'
    with open(prompt, "w") as text_file:
        text_file.writelines(lines)
    if int(lines[6]) == 0:
        await message.answer(f'Caption off')
    else:
        await message.answer(f'Caption on')
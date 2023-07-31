from aiogram.types import BotCommand
from handlers.common import bot


async def set_commands():
    from handlers.Commands.menu_strings import menu_data

    await bot.set_my_commands(
        commands=list(
            map(
                (lambda x: BotCommand(
                    command='/' + x,
                    description=menu_data.get(x) if menu_data.get(x) else f'No info for {x}'
                )
                 ), menu_data.keys())
        )
    )
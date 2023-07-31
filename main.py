import asyncio
import logging
import sys

from handlers.common import bot, dp
from handlers import Router_commands, Router_message
from handlers.Commands.SCommands import set_commands


async def main():

    dp.include_router(Router_commands.form_router)
    dp.include_router(Router_message.router)
    
    await set_commands()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
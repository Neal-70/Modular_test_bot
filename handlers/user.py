from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from lexicon.lexicon import LEXICON_RU

@dp.message(CommandStart()):
async def command_start(message: Message):
    await message.answer(text=LEXICON_RU["/start"])

@dp.message(Command(commands="help")):
async def command_help(message: Message):
    await message.answer(text=LEXICON_RU["/help"])
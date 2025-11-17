import asyncio
import logging

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import user, other


# конфигурация и запуск бота
async def main():
    # загрузка конфигурации
    config: Config = load_config()

    # базовая настройка логирования
    logging.basicConfig(
        level=logging.getLevelName(config.log.level),
        format=config.log.format
    )

    # инициализация бота и диспетчера
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    # регистрация роутеров
    dp.include_routers(user.router, other.router)

    # пропускаем накопившееся апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    # запускаем бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

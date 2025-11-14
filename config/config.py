from dataclasses import dataclass
from environs import Env
from pathlib import Path


@dataclass
class TgBot:
    token: str  # токен доступа к боту


@dataclass
class LogSettings:
    level: str  # уровень логирования
    format: str  # формат сообщений лога


@dataclass
class Config:
    bot: TgBot
    log: LogSettings


def load_config(path: Path | None = None):
    env = Env()
    env.read_env(path)
    bot_token = env.str("BOT_TOKEN")
    log_level = env.str("LOG_LEVEL")
    log_format = env.str("LOG_FORMAT")

    return Config(bot=TgBot(token=bot_token),
                  log=LogSettings(level=log_level, format=log_format)
                  )

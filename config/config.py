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
    bot = env.str("TOKEN_BOT")
    log_level = env.str("LOG_LEVEL")
    log_format = env.str("LOG_FORMAT")

    return Config(bot=bot, log=LogSettings(level=log_level, format=log_format))

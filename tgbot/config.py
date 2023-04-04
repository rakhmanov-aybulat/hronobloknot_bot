from os import environ
from dataclasses import dataclass


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    port: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_id: int


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig


def load_config():
    return Config(
        tg_bot=TgBot(
            token=environ['TGBOT_TOKEN'],
            admin_id=int(environ['TGBOT_ADMIN_ID']),
        ),
        db=DbConfig(
            host=environ['DB_HOST'],
            database=environ['DB_DATABASE'],
            user=environ['DB_USER'],
            port=environ['DB_PORT'],
            password=environ['DB_PASSWORD']
        )
    )

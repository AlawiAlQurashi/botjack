import os

from os import getenv

from dotenv import load_dotenv

load_dotenv()

admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")

BOT_TOKEN = getenv("BOT_TOKEN")

BOT_NAME = getenv("BOT_NAME")

API_ID = int(getenv("API_ID"))

API_HASH = getenv("API_HASH")

MONGODB_URL = getenv("MONGODB_URL")

OWNER_NAME = getenv("OWNER_NAME")

ALIVE_NAME = getenv("ALIVE_NAME")

BOT_PHOTO = getenv("BOT_PHOTO")

DEV_PHOTO = getenv("DEV_PHOTO")

DEV_NAME = getenv("DEV_NAME")

BOT_USERNAME = getenv("BOT_USERNAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO")

UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")

ASSISTANT_NAME = getenv("ASSISTANT_NAME")

GROUP_SUPPORT = getenv("GROUP_SUPPORT", "tx_it")

UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ALAWE1")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5719613462").split()))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ت م ا غ س ش ك S").split())

ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/18b88af791e36bf3c4259.jpg")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))

UPSTREAM_REPO = getenv("https://github.com/AlawiAlQurashi/botjack")

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")

IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")

IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")

IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")

IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png")


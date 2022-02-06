import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "𝐙 𝐀 𝐈 𝐃 🎼")
ALIVE_NAME = getenv("ALIVE_NAME", "𝐙 𝐀 𝐈 𝐃 🎼")
BOT_USERNAME = getenv("BOT_USERNAME", "DC6NOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MDDDI")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TVVLV")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "MQQQS")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c08a4c274f44b5e5c05bd.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/YDDDE/ForMe")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a211541d706fc3d6a18c7.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/0adbff696bd5650081778.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/79ece99c21dd302242a8f.jpg")

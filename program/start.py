from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""- **مرحبآ عزيزي「 {message.from_user.mention()} 」**\n
 **✶ أنا بوت [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **
** ✶ وظيفتي هي تشغيل الاغاني والفيديوهات في المكالمات الحماعية**
 **» اكتشف جميع أوامر البوت وكيفية عملها من خلال النقر على زر » الأوامر!**
 **» لمعرفة كيفية استخدام هذا البوت ، يرجى النقر فوق » زر دليل الاستخدام!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " اضفني الى مجموعتك 🧚🏻‍♀️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("✶ دليل الاستخدام", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("✶ الاوامر", callback_data="cbbasic"),
                    InlineKeyboardButton("✶ المطور", callback_data="cbcmds"),
                ],
                [
                    InlineKeyboardButton(
                        "𝐒𝐨𝐮𝐫𝐜𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "𝐃𝐞𝐯 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/E_B_3"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}","فحص"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url=f"https://t.me/{OWNER_NAME}"),
                InlineKeyboardButton(
                    "𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ", url=f"https://t.me/{UPDATES_CHANNEL}"
                ),
            ]
        ]
    )

    alive = f"**✶ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞  {message.from_user.mention()}, 𝐓𝐨 {BOT_NAME}**\n\n✶ 𝐌𝐚𝐝𝐚 𝐁𝐨𝐭 𝐢𝐬 𝐰𝐨𝐫𝐤𝐞𝐫 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 🧚‍♀\n\n» 𝐌𝐚𝐬𝐭𝐞𝐫 : [{ALIVE_NAME}](https://t.me/{OWNER_NAME})\n» 𝐁𝐨𝐭 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `v{__version__}`\n» 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{pyrover}`\n» 𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{__python_version__}`\n» 𝐏𝐲𝐓𝐠𝐂𝐚𝐥𝐥𝐬 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{pytover.__version__}`\n» 𝐔𝐩𝐭𝐢𝐦𝐞 : `{uptime}`\n\n**✶ شكراً لكم لإضافتي هنا في حال واجهتم اي مشاكل لاتترددو في التواصل مع المطور ** ♬⁩"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("**✶ جاري حساب سرعه البوت**")
    delta_ping = time() - start
    await m_reply.edit_text("**✶ سرعه البوت**\n" f"`{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        " 𝐌𝐚𝐝𝐚 𝐁𝐨𝐭 𝐢𝐬 𝐰𝐨𝐫𝐤𝐞𝐫 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 🧚‍♀:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )

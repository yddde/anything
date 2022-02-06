from cache.admins import admins
from driver.amort import call_py
from pyrogram import Client, filters
from driver.decorators import authorized_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL, BOT_NAME, ALIVE_NAME, OWNER_NAME
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


bttn = InlineKeyboardMarkup(
    [[InlineKeyboardButton("رجوع", callback_data="cbmenu")]]
)


bcl = InlineKeyboardMarkup(
    [[InlineKeyboardButton("اغلاق", callback_data="cls")]]
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}","تحديث"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "**🧚🏻‍♀️ تم تحديث قائمه المشرفين بنجاح. ** "
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "تخطي"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="لوحه التحكم", callback_data="cbmenu"
                ),
                InlineKeyboardButton(
                    text="إغلاق القائمه", callback_data="cls"
                ),
            ]
        ]
    )

    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("**✶ قائمة التشغيل فارغة**")
        elif op == 1:
            await m.reply("**✶ قائمة الانتظار فارغة « تم الخروج من المكالمه بنجاح ** ")
        elif op == 2:
            await m.reply("**✶ تم مسح قائمة الانتظار والخروج من المكالمة الصوتية** ")
        else:
            await m.reply_photo(
                photo=f"{IMG_3}",
                caption=f"⏭ **تم الخطي إلى المسار التالي**\n\n🏷 **الاسم:** [{op[0]}]({op[1]})\n💭 **المجموعة:** `{chat_id}`\n💡 **الحالة:** `Playing`\n🎧 **طلب بواسطة:** {m.from_user.mention()}\n\n[𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥♬⁩](t.me/JustForZaid)\n[𝐙𝐚𝐢𝐝 ⚚](t.me/OnIySad)",
                reply_markup=keyboard,
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**✶ تمت ازالة الاغنية من قائمة الانتظار**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "ايقاف"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("**✶ تم ايقاف التشغيل**")
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply(" **✶ قائمة التشغيل فارغه**")


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "مؤقت"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "**✶ تم ايقاف البث \n♬ لمتابعه التشغيل ارسل الأمر • /resume**"
            )
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply(" **✶ قائمة التشغيل فارغه**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "متابعه"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "️ **✶ تم استئناف التشغيل مؤقتاً**\n\n• **لايقاف البث موقتآ استخدم**\n» /pause الامر"
            )
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply(" **✶ قائمة التشغيل فارغه**")


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "كتم"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                " **✶ تم كتم الصوت**\n\n• **لرفع الكتم استخدم**\n» /unmute الامر"
            )
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply(" **✶ قائمة التشغيل فارغه**")


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "الغاء_كتم"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                " **✶ تم رفع الكتم**\n\n• **لكتم الصوت استخدم**\n» /mute الامر"
            )
        except Exception as e:
            await m.reply(f"🚫 **خطاء:**\n\n`{e}`")
    else:
        await m.reply("❌ **قائمة التشغيل فارغه**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ياحلو بس المشرفين الي معاهم صلاحيه ادارة مكالمات صوتية بيقدرو يستخدمو الزر", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.edit_message_text(
                "**✶ تم الإيقاف \n\n[𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥♬⁩](t.me/JustForZaid)\n[𝐙𝐚𝐢𝐝 ⚚](t.me/OnIySad)**", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("✶ مافي اغنيه ", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ياحلو بس المشرفين الي معاهم صلاحيه ادارة مكالمات صوتية بيقدرو يستخدمو الزر", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.edit_message_text(
                "**✶ تم استئناف التشغيل \n\n[𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥♬⁩](t.me/JustForZaid)\n[𝐙𝐚𝐢𝐝 ⚚](t.me/OnIySad)**", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("✶ مافي اغنيه", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ياحلو بس المشرفين الي معاهم صلاحيه ادارة مكالمات صوتية بيقدرو يستخدمو الزر", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text(" **✶ تم ايقاف التشغيل \n\n[𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥♬⁩](t.me/JustForZaid)\n[𝐙𝐚𝐢𝐝 ⚚](t.me/OnIySad)**", reply_markup=bcl)
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("✶ مافي اغنيه", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ياحلو بس المشرفين الي معاهم صلاحيه ادارة مكالمات صوتية بيقدرو يستخدمو الزر", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.edit_message_text(
                "**✶ تم ايقاف الصوت \n\n[𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥♬⁩](t.me/JustForZaid)\n[𝐙𝐚𝐢𝐝 ⚚](t.me/OnIySad)**", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("✶ مافي اغنيه", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ياحلو بس المشرفين الي معاهم صلاحيه ادارة مكالمات صوتية بيقدرو يستخدمو الزر", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.edit_message_text(
                "**✶ تم تشغيل الصوت\n\n[𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥♬⁩](t.me/JustForZaid)\n[𝐙𝐚𝐢𝐝 ⚚](t.me/OnIySad)**", reply_markup=bttn
            )
        except Exception as e:
            await query.edit_message_text(f"🚫 **خطأ:**\n\n`{e}`", reply_markup=bcl)
    else:
        await query.answer("✶ مافي اغنيه", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "الصوت"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f" ** ✶تم ضبط الصوت على** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **خطأ:**\n\n`{e}`")
    else:
        await m.reply(" **✶ قائمة التشغيل فارغه**")

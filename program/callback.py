# Copyright (C) 2021 By AmortMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""- **مرحبآ عزيزي↤「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」**\n
 **✶ أنا بوت [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **
** ✶ وظيفتي هي تشغيل الاغاني والفيديوهات في المكالمات الحماعية **
 **» اكتشف جميع أوامر البوت وكيفية عملها من خلال النقر على زر » الأوامر! **
 **» لمعرفة كيفية استخدام هذا البوت ، يرجى النقر فوق » زر دليل الاستخدام!**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- اضفني الى مجموعتك 🧚🏻‍♀️",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" ✶ دليل الاستخدام", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("✶ الاوامر", callback_data="cbbasic"),
                    InlineKeyboardButton("✶ المطور", callback_data="cbcmds"),
                ],
                [   
                    InlineKeyboardButton(
                        "✶ 𝐁𝐨𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "✶ 𝐃𝐞𝐯 𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/E_B_3"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" - طريقة تفعيل بوت مدى :

1 - اضفني الى مجموعتك
2 - قم برفعي مشرف في المجموعه
3 - قم بأرسال امر  /reload  في المجموعه ليتم تحديث الملفات
3 - اضف @{ASSISTANT_NAME} عن طريق كتابة /userbotjoin
4 - افتح المكالمه قبل تشغيل الاغاني او الفيديوهات
5 - اذا كان فيه تعليق ارسل - /reload

♪ -  اذا ما دخل الحساب المساعد تأكد ان المكالمه شغاله او ارسل /userbotleave ثم ارسل /userbotjoin
♪ -  اذا كان عندك مشكله او استفسار تفضل هنا: @{OWNER_NAME}

» Channel - @{UPDATES_CHANNEL}
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✶ رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**✶ مرحباً بك في قسم التواصل مع المطور\n\n ✶ فقط قم بالضغط على الزر الذي بالأسفل.  **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("✶ اضغط هنا للتواصل مع المطور", url=f"t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton("✶ رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✶ ها هي الأوامر الأساسية:
» /play 「اسم الأغنية / رابط」تشغيل الصوت mp3
» /vplay 「اسم / رابط الفيديو」 تشغيل الفيديو داخل المكالمة 
» /stream 「رابط 」تشغيل صوت
» /vstream 「رابط」 تشغيل فيديو مباشر من اليوتيوب
» /stop لايقاف التشغيل
» /resume استئناف التشغيل
» /skip تخطي الئ التالي
» /pause ايقاف التشغيل موقتآ
» /vmute لكتم البوت
» /vunmute لرفع الكتم عن البوت
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✶ الـتـالـي", callback_data="cbadmin")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""  » /playlist ↤ تظهر لك قائمة التشغيل
» /video + الاسم  تنزيل فيديو من youtube
» /song + الاسم تنزيل صوت من youtube
» /volume + الرقم لضبط مستوئ الصوت
» /reload لتحديث البوت و قائمة المشرفين
» /userbotjoin لاستدعاء حساب المساعد
» /userbotleave لطرد حساب المساعد 
» /ping - إظهار حالة البوت بينغ
» /alive  إظهار معلومات البوت  (في المجموعة)
 
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✶ رجوع", callback_data="cbstart")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ياحلو بس المشرفين الي معاهم صلاحيه ادارة مكالمات صوتية بيقدرو يستخدمو الزر", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"**✶ لوحة التحكم بقروب** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 اغلاق", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("✶ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("ياحلو بس المشرفين الي معاهم صلاحيه ادارة مكالمات صوتية بيقدرو يستخدمو الزر", show_alert=True)
    await query.message.delete()

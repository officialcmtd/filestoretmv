#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> Bot Creator :</b> <a href='https://ruban96.online'> ❤️‍🔥 𝘿𝙖𝙚𝙣𝙚𝙧𝙮𝙨 𝙏𝙖𝙧𝙜𝙖𝙧𝙮𝙚𝙣 ❤️‍🔥 </a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("🎬 MAIN CHANNEL 🎬", url="https://t.me/+gqpU_4qsYAFmY2U1"),
                     InlineKeyboardButton("🔒 CLOSE", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n○ Channel : @CodeXBotz\n○ Support Group : @CodeXBotzSupport</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "morefromus": 
        await query.message.edit_text(
            text = f"<b>❗JOIN OUR MORE CHANNELS TO DOWNLOAD MOVIES/SERIES FAST❕</b>",
            disable_web_page_preview = False,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("📽️NEW TAMIL MOVIES 1🎬", url=f"https://t.me/+jLLpz0jvWEw4Njll")
                    ],
                    [
                        InlineKeyboardButton("📽️NEW TAMIL MOVIES 2🎬", url=f"https://t.me/+abo3FyAP1hE5MTI9")
                    ],
                    [
                        InlineKeyboardButton("📽️ALL NEW SERIES🎬", url=f"https://t.me/+vuoYEhW__ZBiYzZl")
                    ],
                    [
                        InlineKeyboardButton("📽️HOLLYWOOD DUBBED MOVIES🎬", url=f"https://t.me/+ijiulHzq5s0zN2E1")
                    ],
                    [
                        InlineKeyboardButton("📽️MULTI LANGUAGE MOVIES🎬", url=f"https://t.me/+pHuPLagTQXM3Y2Y1")
                    ],
                    [
                        InlineKeyboardButton("🔉 DISCUSSION 🔉", url="https://t.me/+rucqp8Ao-soyMDU1"),
                        InlineKeyboardButton("🔒 CLOSE 🔒", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

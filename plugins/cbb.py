# (©)Codexbotz
# Recode By @mrismanaziz

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL1, CHANNEL2, GROUP1, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"• 𝗢𝗪𝗡𝗘𝗥: @{OWNER}\n• 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝟭: @{CHANNEL1}\n• 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝟮: @{CHANNEL2}\n• 𝗚𝗥𝗢𝗨𝗣: @{GROUP1}",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close"),
                    ]
                ]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

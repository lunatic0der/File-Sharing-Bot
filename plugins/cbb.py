# (Ā©)Codexbotz
# Recode By @mrismanaziz

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import CHANNEL1, CHANNEL2, GROUP1, OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"ā¢ š¢šŖš”šš„: @{OWNER}\nā¢ šššš”š”šš š­: @{CHANNEL1}\nā¢ šššš”š”šš š®: @{CHANNEL2}\nā¢ šš„š¢šØš£: @{GROUP1}",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("į“į“į“į“į“", callback_data="close"),
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

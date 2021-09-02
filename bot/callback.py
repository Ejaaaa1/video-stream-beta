from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""❓ HOW TO USE THIS BOT:
1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @tg_video_stream to your group.
4.) turn on the voice chat first before start to stream video.
⚡ __Maintained by Veez Project Team__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"**Hello, i'm a video stream bot, i've been created for streaming video on Group video chat.**\n\n**To know how to use me, click the help button below** 👇",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❔ HOW TO USE THIS BOT", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "👩🏻‍💻 Developer", url="https://t.me/dlwrml")
                       ],[
                          InlineKeyboardButton(
                             "💭 Group", url="https://t.me/VeezSupportGroup"),
                          InlineKeyboardButton(
                             "✨ Channel", url="https://t.me/levinachannel")
                       ]]
                    ))

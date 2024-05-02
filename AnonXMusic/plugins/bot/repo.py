from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app


start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

❅ ˹ʙᴜɢ ✘ ϻʊsɪx ˼

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ˹ʙᴜɢ ✘ ϻʊsɪx ˼ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Flames_xD"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/SH251204/BuGMusix"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/12c7e659adcd798aaeba0.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 

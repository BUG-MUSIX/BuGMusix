from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app
from config 

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
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/LOCO-PILOT/ROYMUSIC"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/33bc093c89898dcc318ae.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 

"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('kingmahip'))
async def upgrade(bot,update):
	text = """ **🖼️  ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ**

**⦿  yᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ꜱɪᴍᴩʟy ʙy ꜱᴇɴᴅɪɴɢ ᴀ ᴩʜᴏᴛᴏ ᴛᴏ ᴍᴇ....**

**⦿ /viewthumb - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ**
**⦿ /delthumb - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴀᴍᴍᴏɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ yᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳 ᴜᴩɢʀᴀᴅᴇ",callback_data = "upgrade")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "settings")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["kingmahip"]))
async def upgradecm(bot,message):
	text = """ **🖼️  ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ**

**⦿  yᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ꜱɪᴍᴩʟy ʙy ꜱᴇɴᴅɪɴɢ ᴀ ᴩʜᴏᴛᴏ ᴛᴏ ᴍᴇ....**

**⦿ /viewthumb - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ**
**⦿ /delthumb - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴀᴍᴍᴏɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ yᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳 ᴜᴩɢʀᴀᴅᴇ",callback_data = "upgrade")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "settings")  ]])
	await message.reply_text(text = text,reply_markup = keybord)

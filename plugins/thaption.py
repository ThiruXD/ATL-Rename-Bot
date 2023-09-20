"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters
from config import *

@Client.on_callback_query(filters.regex('kingppt'))
async def upgrade(bot,update):
	text = """ **📝  ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ**

**⦿ /set_caption - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ**
**⦿ /see_caption - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ**
**⦿ /del_caption - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴀᴍᴍᴏɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ**
**⦿ EX :-** ```/set_caption 
📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}```"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳 ᴜᴩɢʀᴀᴅᴇ",callback_data = "upgrade")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "settings")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["kingppt"]))
async def upgradecm(bot,message):
	text = """ **📝  ᴄᴜꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ**

**⦿ /set_caption - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ**
**⦿ /see_caption - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ꜱᴇᴇ yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ**
**⦿ /del_caption - ᴜꜱᴇ ᴛʜɪꜱ ᴄᴀᴍᴍᴏɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ**
**⦿ EX :-** ```/set_caption 
📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}```"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳 ᴜᴩɢʀᴀᴅᴇ",callback_data = "upgrade")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "settings")  ]])
	await message.reply_text(text = text,reply_markup = keybord)

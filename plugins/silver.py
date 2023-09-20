"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters
from config import *

@Client.on_callback_query(filters.regex('zdogrocky'))
async def upgrade(bot,update):
	text = """ **🏷 ᴘʟᴀɴ** :- ```Silver 🥈```

**⌾ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ** :- ```10.0 GB```
**⌾ ᴛɪᴍᴇ ɢᴀᴘ** :- ```0 minutes```
**⌾ 4ɢʙ sᴜᴘᴘᴏʀᴛ** :- ```False```
**⌾ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss** :- ```3```
**⌾ ᴠᴀʟɪᴅɪᴛʏ** :- ```30 Days```

**💰 ᴘʀɪᴄᴇ 59₹ ᴘᴇʀ ᴍᴏɴᴛʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳  ᴜᴩɢʀᴀᴅᴇ",callback_data = "kingmsaa")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["zdogrocky"]))
async def upgradecm(bot,message):
	text = """ **🏷 ᴘʟᴀɴ** :- ```Silver 🥈```

**⌾ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ** :- ```10.0 GB```
**⌾ ᴛɪᴍᴇ ɢᴀᴘ** :- ```0 minutes```
**⌾ 4ɢʙ sᴜᴘᴘᴏʀᴛ** :- ```False```
**⌾ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss** :- ```3```
**⌾ ᴠᴀʟɪᴅɪᴛʏ** :- ```30 Days```

**💰 ᴘʀɪᴄᴇ 59₹ ᴘᴇʀ ᴍᴏɴᴛʜ**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("💳  ᴜᴩɢʀᴀᴅᴇ",callback_data = "kingmsaa")], 
        			[InlineKeyboardButton("• ʙᴀᴄᴋ •",callback_data = "upgrade")  ]])
	await message.reply_text(text = text,reply_markup = keybord)

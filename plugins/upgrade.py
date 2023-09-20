"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters
from config import *

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """ **🏷 ᴄᴜʀʀᴇɴᴛ ᴘʟᴀɴ** :- ```Free```

**⌾ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ** :- ```Upgrade```
**⌾ ᴛɪᴍᴇ ɢᴀᴘ** :- ```5 minutes```
**⌾ 4ɢʙ sᴜᴘᴘᴏʀᴛ** :- ```False```
**⌾ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss** :- ```1```
**⌾ ᴠᴀʟɪᴅɪᴛʏ** :- ```Life Time```"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("🏆 ɢᴏʟᴅ",callback_data = "21k1"),
        			InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """ **🏷 ᴄᴜʀʀᴇɴᴛ ᴘʟᴀɴ** :- ```Free```

**⌾ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ** :- ```Upgrade```
**⌾ ᴛɪᴍᴇ ɢᴀᴘ** :- ```5 minutes```
**⌾ 4ɢʙ sᴜᴘᴘᴏʀᴛ** :- ```False```
**⌾ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss** :- ```1```
**⌾ ᴠᴀʟɪᴅɪᴛʏ** :- ```Life Time```"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ",callback_data = "zdogrocky")], 
        			[InlineKeyboardButton("🏆 ɢᴏʟᴅ",callback_data = "21k1"),
        			InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ",callback_data = "king5461")],[InlineKeyboardButton("• ᴄʟᴏꜱᴇ •",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)

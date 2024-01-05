"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters
from config import *

@Client.on_callback_query(filters.regex('kingmsaa'))
async def upgrade(bot,update):
	text = f"""**ᴩᴀyᴍᴇɴᴛ ᴅɪᴛᴇʟꜱ **

**Silver 🥈 :- 59₹**
**Gold 🏆 :- 99₹**
**Diamond 💎 :- 159₹**

**⌾  My Nᴀᴍᴇ - Narayan purohit**

**⌾  Pʜᴏɴᴇ Pᴀy - Uᴩɪ :-** ```narayankpurohit@ibl```

**🇳  🇴 🇹 🇪   :- ᴀꜰᴛᴇʀ ᴩᴀyᴍᴇɴᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴ ꜱʜᴏᴛ'ꜱ ᴏꜰ ᴩᴀyᴍᴇɴᴛ ᴛᴏ ᴍᴇ - @{OWNER_USERNAME}**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("📸 Sᴇɴᴅ Mᴇ Sᴄʀᴇᴇɴꜱʜᴏᴛ 📸", url=f'https://t.me/{OWNER_USERNAME}')],[InlineKeyboardButton('°• Bᴀᴄᴋ •°', callback_data='upgrade')  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["kingmsaa"]))
async def upgradecm(bot,message):
	text = f"""**ᴩᴀyᴍᴇɴᴛ ᴅɪᴛᴇʟꜱ **

**Silver 🥈 :- 59₹**
**Gold 🏆 :- 99₹**
**Diamond 💎 :- 159₹**

**⌾  My Nᴀᴍᴇ - Thiruselvan**

**⌾  Pʜᴏɴᴇ Pᴀy - Uᴩɪ :-** ```ThiruXD@ibl```

**🇳  🇴 🇹 🇪   :- ᴀꜰᴛᴇʀ ᴩᴀyᴍᴇɴᴛ ꜱᴇɴᴅ ꜱᴄʀᴇᴇɴ ꜱʜᴏᴛ'ꜱ ᴏꜰ ᴩᴀyᴍᴇɴᴛ ᴛᴏ ᴍᴇ - @{OWNER_USERNAME}**"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("📸 Sᴇɴᴅ Mᴇ Sᴄʀᴇᴇɴꜱʜᴏᴛ 📸", url=f'https://t.me/{OWNER_USERNAME}')],[InlineKeyboardButton('°• Bᴀᴄᴋ •°', callback_data='upgrade')  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

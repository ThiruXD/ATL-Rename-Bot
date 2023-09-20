import os 
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup)
from config import *
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes

botid = TOKEN_ONE.split(':')[0]

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["users"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	

	await message.reply_text(f"**⚡️ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ** :- {total_user()}\n\n**⚡️ ᴛᴏᴛᴀʟ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇꜱ**:- {total_rename}\n**⚡ ᴛᴏᴛᴇʟ ʀᴇɴᴀᴍᴇᴅ ꜱɪᴢᴇ** :- {humanbytes(int(total_size))}",quote=True,
                             reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton("• ᴄʟᴏꜱᴇ ᴍᴇɴᴜ •", callback_data="cancel")]]) 
                             )

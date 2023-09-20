from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre
from config import *


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["admin"]))
async def buypremium(bot, message):
	await message.reply_text("**📚 ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ : \n➢ /users - ᴛᴏ ᴠɪᴇᴡ ʟɪꜱᴛ ᴏꜰ ᴜꜱᴇʀꜱ \n➢ /broadcast - ᴍᴇꜱꜱᴀɢᴇ ʙʀᴏᴀᴅᴄᴀꜱᴛ \n➢ /ceasepower - ᴛᴏ ᴄᴇᴀꜱᴇ (ᴅᴏᴡɴɢʀᴀᴅᴇ) ʀᴇɴᴀᴍɪɴɢ ᴄᴀᴩᴀᴄɪᴛy \n➢ /resetpower - ᴛᴏ ʀᴇꜱᴇᴛ ʀᴇɴᴀᴍɪɴɢ ᴄᴀᴩᴀᴄɪᴛy \n➢ /addpremium - ᴛᴏ ᴜᴩɢʀᴀᴅᴇ ᴜꜱᴇʀ ᴩʟᴀɴ**", quote=True, reply_markup=InlineKeyboardMarkup([
		           [
				   InlineKeyboardButton("• ᴄʟᴏꜱᴇ •", callback_data="cancel")
					]]))


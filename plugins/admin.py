from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
import os, sys, time, asyncio
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre
from config import *

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("⊚ ꜱᴇʟᴇᴄᴛ ᴩʟᴀɴ ᴛᴏ ᴜᴩɢʀᴀᴅᴇ...", quote=True, reply_markup=InlineKeyboardMarkup([
		           [
				   InlineKeyboardButton("🥈 ꜱɪʟᴠᴇʀ", callback_data="vip1")
				   ], [
					InlineKeyboardButton("🏆 ɢᴏʟᴅ", callback_data="vip2")
				   ], [
					InlineKeyboardButton("💎 ᴅɪᴀᴍᴏɴᴅ", callback_data="vip3")
					]]))


@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["ceasepower"]))
async def ceasepremium(bot, message):
	await message.reply_text("⊚ ᴩᴏᴡᴇʀ ᴄᴇᴀꜱᴇ ᴍᴏᴅᴇ", quote=True, reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("• ʟɪᴍɪᴛ 500ᴍʙ •", callback_data="cp1"),
				    InlineKeyboardButton("• ʟɪᴍɪᴛ 100ᴍʙ •", callback_data="cp2")
				   ], [
				    InlineKeyboardButton("• ᴄᴇᴀꜱᴇ ᴀʟʟ ᴩᴏᴡᴇʀ •", callback_data="cp3")
				    ]]))


@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["resetpower"]))
async def resetpower(bot, message):
	    await message.reply_text(text=f"⊚ ᴅᴏ yᴏᴜ ʀᴇᴀʟʟy ᴡᴀɴᴛ ᴛᴏ ʀᴇꜱᴇᴛ ᴅᴀɪʟy ʟɪᴍɪᴛ ᴛᴏ ᴅᴇꜰᴀᴜʟᴛ ᴅᴀᴛᴀ ʟɪᴍɪᴛ 2.0ɢʙ ?",quote=True,reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("• yᴇꜱ ! ꜱᴇᴛ ᴀꜱ ᴅᴇꜰᴀᴜʟᴛ •",callback_data = "dft")],
				   [InlineKeyboardButton("❌ ᴄᴀɴᴄᴇʟ",callback_data = "cancel")]
				   ]))

        			
@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 10737418240
	uploadlimit(int(user_id),10737418240)
	usertype(int(user_id),"🥈 **ꜱɪʟᴠᴇʀ**")
	addpre(int(user_id))
	await update.message.edit("ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy ᴛᴏ ᴩʀᴇᴍɪᴜᴍ ᴜᴩʟᴏᴀᴅ ʟɪᴍɪᴛ 10ɢʙ")
	await bot.send_message(user_id,"ʜᴇy yᴏᴜ ᴀʀᴇ ᴜᴩɢʀᴀᴅᴇᴅ ᴛᴏ ꜱɪʟᴠᴇʀ.  ᴄʜᴇᴄᴋ yᴏᴜʀ ᴩʟᴀɴ ʜᴇʀᴇ /myplan")
	await bot.send_message(LOG_CHANNEL,f"⚡️ ᴩʟᴀɴ ᴜᴩɢʀᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy 💥\n\nʜᴇy yᴏᴜ ᴀʀᴇ ᴜᴩɢʀᴀᴅᴇᴅ ᴛᴏ ꜱɪʟᴠᴇʀ. ᴄʜᴇᴄᴋ yᴏᴜʀ ᴩʟᴀɴ ʜᴇʀᴇ /myplan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 53687091200
	uploadlimit(int(user_id), 53687091200)
	usertype(int(user_id),"🏆 **ɢᴏʟᴅ**")
	addpre(int(user_id))
	await update.message.edit("ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy ᴛᴏ ᴩʀᴇᴍɪᴜᴍ ᴜᴩʟᴏᴀᴅ ʟɪᴍɪᴛ 50ɢʙ")
	await bot.send_message(user_id,"ʜᴇy yᴏᴜ ᴀʀᴇ ᴜᴩɢʀᴀᴅᴇᴅ ᴛᴏ ɢᴏʟᴅ.  ᴄʜᴇᴄᴋ yᴏᴜʀ ᴩʟᴀɴ ʜᴇʀᴇ /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 107374182400
	uploadlimit(int(user_id), 107374182400)
	usertype(int(user_id),"💎 **ᴅɪᴀᴍᴏɴᴅ**")
	addpre(int(user_id))
	await update.message.edit("ᴀᴅᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy ᴛᴏ ᴩʀᴇᴍɪᴜᴍ ᴜᴩʟᴏᴀᴅ ʟɪᴍɪᴛ 100ɢʙ")
	await bot.send_message(user_id,"ʜᴇy yᴏᴜ ᴀʀᴇ ᴜᴩɢʀᴀᴅᴇᴅ ᴛᴏ ᴅɪᴀᴍᴏɴᴅ.  ᴄʜᴇᴄᴋ yᴏᴜʀ ᴩʟᴀɴ ʜᴇʀᴇ /myplan")

# CEASE POWER MODE @LAZYDEVELOPER

@Client.on_callback_query(filters.regex('cp1'))
async def cp1(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit  = 524288000
	uploadlimit(int(user_id),524288000)
	usertype(int(user_id),"**ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ**")
	addpre(int(user_id))
	await update.message.edit("ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ\nᴛʜᴇ ᴜꜱᴇʀ ᴄᴀɴ ᴏɴʟy ᴜꜱᴇ 100ᴍʙ/ᴅᴀy ꜰʀᴏᴍ ᴅᴀᴛᴀ qᴏᴛᴀ")
	await bot.send_message(user_id,"⚠️ ᴡᴀʀɴɪɴɢ⚠️\n\n- ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ\nyᴏᴜ ᴄᴀɴ ᴏɴʟy ᴜꜱᴇ 500ᴍʙ/ᴅᴀy ꜰʀᴏᴍ ᴅᴀᴛᴀ qᴏᴛᴀ.\nᴄʜᴇᴄᴋ yᴏᴜʀ ᴩʟᴀɴ ʜᴇʀᴇ - /myplan")

@Client.on_callback_query(filters.regex('cp2'))
async def cp2(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit = 104857600
	uploadlimit(int(user_id), 104857600)
	usertype(int(user_id),"**ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ ʟᴠ-2**")
	addpre(int(user_id))
	await update.message.edit("ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ ᴛᴏ ʟᴇᴠᴇʟ 2\nᴛʜᴇ ᴜꜱᴇʀ ᴄᴀɴ ᴏɴʟy ᴜꜱᴇ 100ᴍʙ/ᴅᴀy ꜰʀᴏᴍ ᴅᴀᴛᴀ qᴏᴛᴀ")
	await bot.send_message(user_id,"⛔️ ʟᴀꜱᴛ ᴡᴀʀɴɪɴɢ ⛔️\n\n- ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ ᴛᴏ ʟᴇᴠᴇʟ 2\nyᴏᴜ ᴄᴀɴ ᴏɴʟy ᴜꜱᴇ 100ᴍʙ/ᴅᴀy ꜰʀᴏᴍ ᴅᴀᴛᴀ qᴏᴛᴀ.\nᴄʜᴇᴄᴋ yᴏᴜʀ ᴩʟᴀɴ ʜᴇʀᴇ - /myplan")

@Client.on_callback_query(filters.regex('cp3'))
async def cp3(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit = 0
	uploadlimit(int(user_id), 0)
	usertype(int(user_id),"**ᴩᴏᴡᴇʀ ᴄᴇᴀꜱᴇᴅ !**")
	addpre(int(user_id))
	await update.message.edit("ᴀʟʟ ᴩᴏᴡᴇʀ ᴄᴇᴀꜱᴇᴅ ꜰʀᴏᴍ ᴛʜᴇ ᴜꜱᴇʀ.\nᴛʜɪꜱ ᴀᴄᴄᴏᴜɴᴛ ʜᴀꜱ 0 ᴍʙ ʀᴇɴᴀᴍɪɴɢ ᴄᴀᴩᴀᴄɪᴛy")
	await bot.send_message(user_id,"🚫 ᴀʟʟ ᴩᴏᴡᴇʀ ᴄᴇᴀꜱᴇᴅ 🚫\n\n- ᴀʟʟ ᴩᴏᴡᴇʀ ʜᴀꜱ ʙᴇᴇɴ ᴄᴇᴀꜱᴇᴅ ꜰʀᴏᴍ yᴏᴜ \nꜰʀᴏᴍ ɴᴏᴡ yᴏᴜ ᴄᴀɴ'ᴛ ʀᴇɴᴀᴍ ꜰɪʟᴇꜱ ᴜꜱɪɴɢ ᴍᴇ\nᴄʜᴇᴄᴋ yᴏᴜʀ ᴩʟᴀɴ ʜᴇʀᴇ - /myplan")

@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 10
	uploadlimit(int(user_id), 10)
	usertype(int(user_id),"**ꜰʀᴇᴇ**")
	addpre(int(user_id))
	await update.message.edit(" ᴅᴀɪʟy ᴅᴀᴛᴀ ʟɪᴍɪᴛ ʜᴀꜱ ʙᴇᴇɴ ʀᴇꜱᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy.\nᴛʜɪꜱ ᴀᴄᴄᴏᴜɴᴛ ʜᴀꜱ ᴅᴇꜰᴀᴜʟᴛ 10B ʀᴇɴᴀᴍɪɴɢ ᴄᴀᴩᴀᴄɪᴛy ")
	await bot.send_message(user_id,"yᴏᴜʀ ᴅᴀɪʟy ᴅᴀᴛᴀ ʟɪᴍɪᴛ ʜᴀꜱ ʙᴇᴇɴ ʀᴇꜱᴇᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy.\n\nᴄʜᴇᴄᴋ yᴏᴜʀ ᴩʟᴀɴ ʜᴇʀᴇ - /myplan")

#Restart to cancell all process 
@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["restart"]))
async def restart_bot(b, m):
    await m.reply_text("🔄__Rᴇꜱᴛᴀʀᴛɪɴɢ.....__")
    os.execl(sys.executable, sys.executable, *sys.argv)

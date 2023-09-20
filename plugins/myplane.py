import time
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)
from helper.database import find_one, used_limit
from helper.database import daily as daily_
import datetime
from datetime import timedelta, date, datetime
from datetime import date as date_
from helper.progress import humanbytes
from helper.database import daily as daily_
from helper.date import check_expi
from helper.database import uploadlimit, usertype
from config import *


@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client, message):
    used_ = find_one(message.from_user.id)
    daily = used_["daily"]
    expi = daily - \
        int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
    if expi != 0:
        today = date_.today()
        pattern = '%Y-%m-%d'
        epcho = int(time.mktime(time.strptime(str(today), pattern)))
        daily_(message.from_user.id, epcho)
        used_limit(message.from_user.id, 0)
    _newus = find_one(message.from_user.id)
    used = _newus["used_limit"]
    limit = _newus["uploadlimit"]
    remain = int(limit) - int(used)
    user = _newus["usertype"]
    ends = _newus["prexdate"]
    if ends:
        pre_check = check_expi(ends)
        if pre_check == False:
            uploadlimit(message.from_user.id, 10)
            usertype(message.from_user.id, "Free")
    if ends == None:
        text = f"**ᴜꜱᴇʀ ɪᴅ**:- ```{message.from_user.id}```\n**ᴩʟᴀɴ** :- {user}\n**ᴅᴀɪʟy ᴜᴩʟᴏᴀᴅ ʟɪᴍɪᴛ** :- {humanbytes(limit)}\n**ᴛᴏᴅᴀy ᴜꜱᴇᴅ** :- {humanbytes(used)}\n**ʀᴇᴍᴀɪɴ** :- {humanbytes(remain)}"
    else:
        normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
        text = f"**ᴜꜱᴇʀ ɪᴅ** :- ```{message.from_user.id}```\n**ᴩʟᴀɴ** :- {user}\n**ᴅᴀɪʟy ᴜᴩʟᴏᴀᴅ ʟɪᴍɪᴛ** :- {humanbytes(limit)}\n**ᴛᴏᴅᴀy ᴜꜱᴇᴅ** :- {humanbytes(used)}\n**ʀᴇᴍᴀɪɴ** :- {humanbytes(remain)}\n\n**yᴏᴜʀ ᴩʟᴀɴ ᴇɴᴅꜱ ᴏɴ** :- {normal_date}"

    if user == "Free":
        await message.reply(text, quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 ᴜᴩɢʀᴀᴅᴇ", callback_data="upgrade"), InlineKeyboardButton("Cancel ✖️ ", callback_data="cancel")]]))
    else:
        await message.reply(text, quote=True)

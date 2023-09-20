import asyncio
from pyrogram import Client, compose,idle
import os
from aiohttp import web
from route import web_server
from config import *
from plugins.cb_data import app as Client2

bot = Client(

           "Renamerone",

           bot_token=TOKEN_ONE,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))


if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()

else:
    bot.run()


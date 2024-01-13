import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "13323016")
API_HASH = os.environ.get("API_HASH", "68e791e616100248b0a53ae86a661a12")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "6956569466:AAFIrV5A3LXdVcFJgBHvuFAs2aBpLd3Ivko") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "")

CHANNEL = os.environ.get("CHANNEL", "hd_telegram_movies") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","MxmoderRename_bot") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","hd_telegram_movies") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","hd_telegram_movies") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","mxmode")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","Cluster0")     
DB_URL = os.environ.get("DB_URL","mongodb+srv://anshk2354:simransh@cluster0.fxqprvk.mongodb.net/?retryWrites=true&w=majority")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "https://telegra.ph/file/f9a36fe45636448dccce8.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1083324269').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002141964124"))

import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
#BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
TOKEN_ONE = os.environ.get("TOKEN_ONE", "")

CHANNEL = os.environ.get("CHANNEL", "ATL_Univers") # username without '@'
BOT_USERNAME = os.environ.get("BOT_USERNAME","") # username without '@'
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP","BYNF_TamilChat") # username without '@'
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL","ATL_Univers") # username without '@'
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","HMF_Owner_1")
STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","renameone")     
DB_URL = os.environ.get("DB_URL","")

FLOOD = int(os.environ.get("FLOOD", "90"))
LAZY_PIC = os.environ.get("LAZY_PIC", "")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1989750989').split()]
PORT = os.environ.get('PORT', '8080')
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001230390281"))

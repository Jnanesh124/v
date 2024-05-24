# Thanks @Codeflix_Bots

import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "api.shareus.io")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/How_to_Download_7x/32")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>hey {first}\n\n ɪ ᴀᴍ ᴛᴏᴋᴇɴ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ , ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ » @ROCKERSBACKUP</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6852649461").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Join Below 👇 All Channel  After Click “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” button....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐇𝐃 𝐌𝐨𝐯𝐢𝐞𝐬 
👉 https://t.me/+4Fxg05W56SVkOTY1

𝐊𝐚𝐧𝐧𝐚𝐝𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐌𝐨𝐯𝐢𝐞𝐬 
👉 https://t.me/+5MMPfVCCiAU5MjU1

Bollywood Hindi HD MOVIES 
👉 https://t.me/+sIUMbwiAsIo4Mjll

Tamil Telugu Malayalam Movies 🎥
👉 https://t.me/+hJLWDbymVZsyOTk1

Hollywood action movie 
👉 https://t.me/+zHXxf4Y5ve03YThl

18+ Baned Movies A Rated movie Only 🔞
👉 https://t.me/+GwoURlq-hr1hOTc9

𝐓𝐫𝐞𝐧𝐝𝐢𝐧𝐠 𝐌𝐨𝐯𝐢𝐞𝐬 𝐇𝐃 
👉 https://t.me/+EVHwFEL-OWdlMjM1

Sex Video porn video 
👉 https://t.me/+P-wgbt_2dlU3MTM1

Movies 🎥
👉https://t.me/+LpVX0gNfgEM5ZjE1

©️@ROCKERSBACKUP</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @codeflix_bots"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "codeflixbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ BOT Commands 
 ├ /start - Start The Bot
 ├ /about - About This Bot
 ├ /help - Get Sum Help
 ├ /ping - BOT Ping
 └ /uptime - BOT Uptime
 
 ❏ Commands for Admins
 ├ /logs - Fuckin Logs
 ├ /setvar - Dunno the use
 ├ /delvar - Never Used, not useful 
 ├ /getvar - Useless AF
 ├ /users - Number of Users
 ├ /batch - Batch
 ├ /speedtest - Useless 
 └ /broadcast - The Annoying Comand for Subs

👨‍💻 Develoved by </b><a href='https://t.me/Bhargav_Gadekar'>@Bhargav_Gadekar</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>About This Bot:

@{} Billo Bagge Biliyan Da Ki Karegi, Bagga Bagge Billiyan Da Ki Karegi.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Source Code: <a href='https://t.me/Entertainment_District/4'>Repo Here</a>

👨‍💻 Develoved by Owners of </b><a href='https://t.me/The_Otaku_Federation/86'>@The_Otaku_Federation</a>
"""

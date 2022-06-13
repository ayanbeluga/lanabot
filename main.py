import asyncio
from pyrogram import Client
from pyrogram import filters

from log import log


apiid = 11237542
apihash = "dde43840a010d433a77a6a02221ba554"
bottoken = "5589854998:AAF1YDKkmH9ihgrIdCU7MdlQ6lW5RM6oGI0" #bot token here


client = Client(
    'lana',
    apiid,
    api_hash= apihash,
    bot_token = bottoken,
    plugins=dict(root="plugins"),
    
)


client.run()

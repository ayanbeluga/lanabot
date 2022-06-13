import asyncio
from pyrogram import Client
from pyrogram import filters

from log import log


#apiid = 11237542
#apihash = "dde43840a010d433a77a6a02221ba554"
#bottoken = "5589854998:AAF1YDKkmH9ihgrIdCU7MdlQ6lW5RM6oGI0" #bot token here


bot = Client(
    'bot',
    api_id= 11237542, #get it from https://my.telegram.org/auth
    api_hash="dde43840a010d433a77a6a02221ba554", #get it from https://my.telegram.org/auth
    bot_token="5589854998:AAF1YDKkmH9ihgrIdCU7MdlQ6lW5RM6oGI0", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)

from pyrogram import Client,idle
from pyrogram import filters
import asyncio


app = Client(
    "reverse_bot",
    api_id = 11674810,
    api_hash="9a64eb6bf7a4e8ba17dfa06efe6f2c6c",
    bot_token="6141435415:AAE4HkjvE-BzwrfNMsNqYX-9mH87ca87qHg"
)


@app.on_message(filters.command("start"))
async def _start(_,msg):
    await msg.reply("hey there")

async def main():
    await app.start()
    print("bot started")
    await idle()
    print("bot stopped")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

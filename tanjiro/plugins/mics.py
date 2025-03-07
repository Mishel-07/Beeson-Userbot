from tanjiro import app

@app.on_message(filters.command("alive") & filters.me)
async def alive(me, message):
    await message.reply("I'm alive")


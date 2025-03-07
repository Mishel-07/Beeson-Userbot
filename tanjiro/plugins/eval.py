from tanjiro import app
from pyrogram import filters 

async def aexec(code, client, message):
    exec(
        "async def __evall(client, message): "
        + "p=print"
        + "r=message.reply_to_message"     
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__evall"](client, message)


@app.on_message(filters.command(["eval", "e"]) & filters.me)
async def evalrun(client, message):
    code = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not code:
        await message.edit("<b><emoji id=5210952531676504517>❌</emoji> No code provided.")
        return
    out = await aexec(code, client, message)
    print(out)
    await message.edit(f"{out}")
   
      
	

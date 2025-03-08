from tanjiro import app
from pyrogram import filters
import traceback
import io
import sys
import contextlib

async def aexec(code, client, message):
    exec(
        "async def __evall(client, message):\n"
        + " p = print\n"
        + " m = message\n"
        + " r = m.reply_to_message\n"   
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        result = await locals()["__evall"](client, message)
    output = buffer.getvalue()
    return output
    
@app.on_message(filters.command(["eval", "e"]) & filters.me)
async def evalrun(client, message):
    if len(message.text.split()) <= 1:
        await message.edit("<b><emoji id=5210952531676504517>❌</emoji> No code provided.</b>")
        return
    code = message.text.split(" ", 1)[1]
    output = await aexec(code, client, message)
    mes = f""":<b><emoji id=5260480440971570446>💻</emoji> Language:
`python`

<emoji id=5253742260054409879>✉️</emoji> Code:
<pre>
{code}

<emoji id=525374226005>✉️</emoji> Code:
<pre> Result:
    """
    await message.edit(output)

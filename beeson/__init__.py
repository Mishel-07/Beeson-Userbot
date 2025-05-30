from pyrogram import Client, idle
import os

API_ID = int(os.environ.get('API_ID', ''))  
API_HASH = os.environ.get('API_HASH', '')  
SESSION = os.environ.get('SESSION', '')  


app = Client(
        "beeson",
        session_string=SESSION,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=dict(root="beeson") 
)

async def start_bot():
    await app.start()
    await idle()

from pyrogram import Client, idle
import os
import asyncio

API_ID = int(os.environ.get('API_ID', ''))  
API_HASH = os.environ.get('API_HASH', '')  
SESSION = os.environ.get('SESSION', '')  


app = Client(
        "mishal",
        session_string=SESSION,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=dict(root="plugins") 
)

async def start_bot():
    await app.start()
    await idle()

if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())

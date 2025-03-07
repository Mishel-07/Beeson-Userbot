from pyrogram import Client
import os

API_ID = int(os.environ.get('API_ID', ''))  
API_HASH = os.environ.get('API_HASH', '')  
SESSION = os.environ.get('SESSION', '')  


app = Client(
        "tanjiro-userbot",
        session_string=SESSION,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=dict(root="tanjiro") 
)

    

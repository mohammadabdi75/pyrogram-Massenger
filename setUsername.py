import asyncio
from pyrogram import Client, filters
from telegram import Bot
import os
from faker import Faker

# Codes for API_ID and CHANNEL should be without " "
API_ID= "Your API_ID"
API_HASH= "Your API_HASH"
TOKEN= "Your TOKEN"
CHANNEL= "Your CHANNEL"
fake = Faker()

async def main():
    for s in os.listdir("sessions"):
        if s.endswith("session"):
            async with Client("sessions/" + s.replace(".session", "")) as client:
                su = False
                while not su:
                    # Change FAVORITE_NAME to you special name
                    USERNAME = "FAVORITE_NAME"+fake.user_name()
                    print("Setting username", USERNAME, "for", s)
                    try:
                        await client.set_username(USERNAME)
                        su = True
                        text = f"Username is set for\nt.me/{s.replace('.session', '')}\nUsername is: @{USERNAME}"
                        await Bot(TOKEN).send_message(CHANNEL, text)
                    except Exception as e:
                        print(e)
                        await asyncio.sleep(5)
asyncio.run(main())
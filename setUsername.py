import asyncio
from pyrogram import Client
import os
from faker import Faker

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
                    USERNAME = fake.user_name()
                    print("Setting username", USERNAME, "for", s)
                    try:
                        await client.set_username(USERNAME)
                        su = True
                    except Exception as e:
                        print(e)
                        await asyncio.sleep(5)
asyncio.run(main())
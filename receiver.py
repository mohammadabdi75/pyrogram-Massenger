import asyncio
from pyrogram import Client, filters
from telegram import Bot
from multiprocessing import Process
import os
import time


API_ID= "Your API_ID"
API_HASH= "Your API_HASH"
TOKEN= "Your TOKEN"
CHANNEL= "Your CHANNEL"

def receiver(session):
    print("Staring receiver for", session)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = Client("sessions/" + session)
    @app.on_message(filters.chat(777000))
    async def fwd(client, message):
        text = f"Got new TG Message:\nt.me/{session}\n{message.text}"
        await Bot(TOKEN).send_message(CHANNEL, text)
    app.run()

def main():
    ps = []
    for s in os.listdir("sessions"):
        if s.endswith("session"):
            p = Process(target=receiver, args=[s.split(".session")[0]])
            ps.append(p)
            p.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            for p in ps:
                p.terminate()
                p.join()
            break

if __name__ == "__main__":
    main()

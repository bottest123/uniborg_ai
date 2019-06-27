from telethon import TelegramClient, events
import time

@borg.on(events.NewMessage(outgoing=True))
async def type(e):
    print("typer")
    print(e.raw_text)
    if e.raw_text.startswith(":"):
        mtext = e.raw_text.replace(":", "")
        result = ""
        for i in range(len(mtext)):
            result = result + mtext[i]
            if i < (len(mtext) - 1):
                await e.edit("```{}|```".format(result))
            else:
                await e.edit("```{}```".format(result))
            time.sleep(0.2)

import asyncio
from telethon import *
from uniborg import *
@borg.on(events.NewMessage(outgoing=True, pattern='.spam'))
@borg.on(events.MessageEdited(outgoing=True, pattern='.spam'))
async def spammer(e):
    message= e.text
    counter=int(message[6:8])
    spam_message=str(e.text[8:])
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    await e.delete()
    await event.send_message(LOGGER_GROUP,"Spam was executed successfully")
@borg.on(events.NewMessage(outgoing=True, pattern='.bigspam'))
@borg.on(events.MessageEdited(outgoing=True, pattern='.bigspam'))
async def bigspam(e):
    message = e.text
    counter=int(message[9:13])
    spam_message=str(e.text[13:])
    for i in range (1,counter):
       await e.respond(spam_message)
    await e.delete()
    await event.send_message(LOGGER_GROUP,"bigspam was executed successfully")
@borg.on(events.NewMessage(outgoing=True, pattern='.picspam'))
@borg.on(events.MessageEdited(outgoing=True, pattern='.picspam'))
async def tiny_pic_spam(e):
    message= e.text
    TEXT=message.split()
    counter=int(TEXT[1])
    LINK=str(TEXT[2])
    for i in range (1,counter):
       await bot.send_file(e.chat_id,LINK)
    await e.delete()
    await event.send_message(LOGGER_GROUP,"PicSpam was executed successfully")

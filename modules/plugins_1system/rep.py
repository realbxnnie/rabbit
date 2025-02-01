from pyrogram import Client, filters, types, enums
from modules.plugins_1system.settings.main_settings import module_list, file_list, Config
from time import *
from glob import glob

import json
import os
import requests
import modules.plugins_1system.settings.main_settings 

def totext(text: str):
    return text.replace(f'{Config.prefix}{moduleName}', '')

def count(dict):
    i = 0
    for j in dict:
        i += 1

    return i

def unpack(dict):
    result = ""
    for i in dict:
        result = result + f"<b>{Config.showlinks == "True" and f'<a href={type(i)==int and f"tg://openmessage?user_id={i}" or f"https://t.me/{i}"}>{i}</a>' or i}</b>: {dict[i]}%\n"
    
    return result
moduleName = 'rep'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def rep(client: Client, message: types.Message):
   replist = json.loads(open("config/replist.json", "r").read())
   print(replist, type(replist))
   if Config.reputation == "True":
        if count(message.text.split()) >= 2:
                if message.text.split()[1] == "+":
                    user = ""
                    if message.reply_to_message.from_user.username == None:
                        user = int(message.reply_to_message.from_user.id)
                    else:
                        user = message.reply_to_message.from_user.username
                    if message.reply_to_message.from_user.id == message.from_user.id:
                        await message.edit("❌ <b>Вы не можете повысить репутацию себе!</b>")
                    else:
                        if user not in replist:
                            replist[user] = 0
                        replist[user] += int(message.text.split()[2])
                        json.dump(replist, open("config/replist.json", "w"))
                        await message.edit(f"➕ <b>Репутация пользователя {user} повышена на {message.text.split()[2]}%!</b>")
                elif message.text.split()[1] == "-":
                    user = ""
                    if message.reply_to_message.from_user.username == None:
                        user = int(message.reply_to_message.from_user.id)
                    else:
                        user = message.reply_to_message.from_user.username
                    if message.reply_to_message.from_user.id == message.from_user.id:
                        await message.edit("❌ <b>Вы не можете понизить репутацию себе!</b>")
                    else:
                        if user not in replist:
                            replist[user] = 0
                        replist[user] -= int(message.text.split()[2])
                        json.dump(replist, open("config/replist.json", "w"))
                        await message.edit(f"➖ <b>Репутация пользователя {user} понижена на {message.text.split()[2]}%!</b>")
                elif message.text.split()[1] == "r":
                    del replist[user]
                    json.dump(replist, open("config/replist.json", "w"))
                    await message.edit(f"✅ <b>Репутация пользователя {user} удалена!</b>")
                elif message.text.split()[1] == "c":
                    replist.clear()
                    json.dump(replist, open("config/replist.json", "w"))
                    await message.edit(f"✅ <b>Таблица репутации очищена!</b>")
        else:
            await message.edit(f"""
🌟 <b>Таблица репутации</b>:
{unpack(replist)}
                               """)
   else:
        await message.edit("❌ <b>Режим репутации выключен! Включите режим репутации и попробуйте снова.</b>")



module_list['Reputation'] = f'{Config.prefix}{moduleName} [+/-/r/c] [%]'
file_list['Reputation'] = f'{moduleName}.py'

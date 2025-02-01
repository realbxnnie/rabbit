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

moduleName = 'rmmod'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def rmmod(client: Client, message: types.Message):
    await message.edit(f"🌐 <b>Получение модуля...</b>")
    module = requests.get(message.text.split()[1])
    if module:
        await message.edit(f"⚙️ <b>Удаление модуля...</b>")
        custommodules = glob("modules/plugins_2custom/*C.py")
        for i in custommodules:
            if open(i, "r").read() == module.text and i.endswith("C.py"):
                os.remove(i) 
                await message.edit(f"✅ <b>Модуль был успешно удален!</b>")
                Config.restart_userbot()
                break
            else:
                await message.edit(f"❌ <b>Вы не можете удалить системный модуль!</b>")
    


    print(module)
    #await message.edit(f"✅ <b>Чат был очищен от сообщений юзербота</b>")

module_list['Remove Module'] = f'{Config.prefix}{moduleName} [ raw source link ]'
file_list['Remove Module'] = f'{moduleName}.py'

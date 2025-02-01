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

moduleName = 'loadmod'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def loadmod(client: Client, message: types.Message):
    await message.edit(f"🌐 <b>Получение модуля...</b>")
    module = requests.get(message.text.split()[1])
    if module:
        await message.edit(f"⚙️ <b>Установка модуля...</b>")
        cmn = 0
        while True:
            if os.path.exists(f"modules/plugins_2custom/module{cmn}C.py"):
                cmn = cmn + 1
            else:
                custommodules = glob("modules/plugins_2custom/*C.py")
                alreadyInstalled = False
                for i in custommodules:
                    if open(i, "r").read() == module.text:
                       alreadyInstalled = True
                       await message.edit(f"❌ <b>Модуль уже установлен!</b>")
                       break
                if not alreadyInstalled:
                        os.system(f"curl -L -o modules/plugins_2custom/module{cmn}C.py {message.text.split()[1]}")
                        await message.edit(f"✅ <b>Модуль был успешно установлен!</b>")
                        Config.restart_userbot()
                break
            sleep(0.1)
    

    print(module)
    #await message.edit(f"✅ <b>Чат был очищен от сообщений юзербота</b>")

module_list['Load Module'] = f'{Config.prefix}{moduleName} [raw source link]'
file_list['Load Module'] = f'{moduleName}.py'

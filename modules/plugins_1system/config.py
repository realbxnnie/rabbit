from pyrogram import Client, filters, types
from modules.plugins_1system.settings.main_settings import module_list, file_list, Config
from time import *

import json
import modules.plugins_1system.settings.main_settings 

def totext(text: str):
    return text.replace(f'{Config.prefix}{moduleName}', '')

def count(dict):
    i = 0
    for j in dict:
        i += 1

    return i

moduleName = 'config'  
@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def config(client: Client, message: types.Message):
    modulesd = ""
    Config.botmessages.append(message)
    async def links():
        if message.text.split()[2] == "off":
            Config.setlinks("False")
            await message.edit(f"✅ <b>Ссылки отправленные юзерботом будут скрываться</b>")
            Config.restart_userbot()
        else:
            Config.setlinks("True")
            await message.edit(f"✅ <b>Ссылки отправленные юзерботом будут показываться</b>")
            Config.restart_userbot()

        
    async def cmd():
        if message.text.split()[2] == "all":
            Config.setcmd("all")
            await message.edit(f"✅ <b>Выполнять команды теперь могут все</b>")
            Config.restart_userbot()
        else:
            Config.setcmd("me")
            await message.edit(f"✅ <b>Выполнять команды теперь можете только вы</b>")
            Config.restart_userbot()

    async def reputation():
        if message.text.split()[2] == "off":
            Config.setrep("False")
            await message.edit(f"✅ <b>Режим репутации выключен</b>")
            Config.restart_userbot()
        else:
            Config.setrep("True")
            await message.edit(f"✅ <b>Режим репутации включен</b>")
            Config.restart_userbot()
    
    async def prefix():
            Config.setprefix(message.text.split()[2])
            await message.edit(f"✅ <b>Префикс успешно изменен на {message.text.split()[2]}</b>")
            Config.restart_userbot()

    async def reset():
            await message.edit(f"⚙️ <b>Сброс настроек...</b>")
            Config.setprefix(".")
            Config.setrep("False")
            Config.setlinks("False")
            await message.edit(f"✅ <b>Настройки успешно были сброшены!</b>")
            Config.restart_userbot()

    setf = {
        "links": links,
        "prefix": prefix,
        "reset": reset,
        "reputation": reputation,

    }
    if count(message.text.split()) == 1:
        for i in module_list:
            if file_list[i].endswith("C.py"):
                modulesd = modulesd + f"\n⬛ {i} | {module_list[i]} | Посторонний модуль"
            else:
                modulesd = modulesd + f"\n🟩 {i} | {module_list[i]} | Системный модуль"
        await message.edit(f"""
⚙️ <b>Настройки</b>
                           
<b>Загруженные модули</b>: 
                    <code>{modulesd}</code>

<b>Префикс</b>: <code>{Config.prefix}</code>

<b>Показывание ссылок</b>: <code>{Config.showlinks == "True" and "Включено" or "Выключено"}</code>

<b>Режим репутации</b>: <code>{Config.reputation == "True" and "Включен" or "Выключен"}</code>

    """)
    else:
            if setf.get(message.text.split()[1]):
                await setf.get(message.text.split()[1])()
            else:
                await message.edit("❌ <b>Функция не найдена</b>")
module_list['Config'] = f'{Config.prefix}{moduleName} [index] [value]'
file_list['Config'] = f'{moduleName}.py'

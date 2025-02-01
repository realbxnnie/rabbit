from pyrogram import Client, filters, types, enums
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

moduleName = 'info'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def info(client: Client, message: types.Message):
    info_dict = {}
    chatid = message.chat.id
    Config.botmessages.append(message)
    await message.edit(f"🌐 <b>Получение информации...</b>")
    info_dict["ubv"] = Config.version
    info_dict["pgv"] = Client.APP_VERSION.replace('Pyrogram', '')
    info_dict["pf"] = Config.prefix
    info_dict["md"] = count(module_list)
    info_dict["rc"] = Config.showlinks == True and "https://t.me/rabbit_userbot" or "null://"
    await message.edit(f"""
🐇 <b>Версия Rabbit</b>: {info_dict["ubv"]}
🥧 <b>Версия Pyrogram</b>: {info_dict["pgv"]}
🔤 <b>Префикс</b>: {info_dict["pf"]}
📖 <b>Модули</b>: {info_dict["md"]}

🐇 <b><a href={info_dict["rc"]}>Официальный канал Rabbit {Config.showlinks == True and ' ' or '(скрыто)'}</a></b>
""")

module_list['Info'] = f'{Config.prefix}{moduleName}'
file_list['Info'] = f'{moduleName}.py'

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

moduleName = 'purge'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def purge(client: Client, message: types.Message):
    await message.edit(f"🧹 <b>Очистка...</b>")
    for i in Config.botmessages:
        await client.delete_messages(i.chat.id, i.id)
        sleep(0.1)
        Config.botmessages.remove(i)
    await message.edit(f"✅ <b>Чат был очищен от сообщений юзербота</b>")

module_list['Purge'] = f'{Config.prefix}{moduleName}'
file_list['Purge'] = f'{moduleName}.py'

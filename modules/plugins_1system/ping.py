from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import file_list, module_list, Config

from time import perf_counter

import json

def totext(text: str):
    return text.replace(f'{Config.prefix}{moduleName}', '')

def count(dict):
    i = 0
    for j in dict:
        i += 1

    return i

moduleName = 'ping'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def ping(client, message):
    Config.botmessages.append(message)
    start = perf_counter()
    await message.edit("<b>🚀 П</b>")
    await message.edit("<b>🚀 По</b>")
    await message.edit("<b>🚀 Пон</b>")
    await message.edit("<b>🚀 Понг!</b>")
    end = perf_counter()

    pinges = ((end - start) / 4)
    ping = pinges * 1000

    if 0 <= ping <= 199:
        connect = "🟢 Хорошо"
    if 199 <= ping <= 400:
        connect = "🟠 Стабильно"
    if 400 <= ping <= 600:
        connect = "🔴 Нестабильно"
    if 600 <= ping:
        connect = "⚫ Ужасно"
    await message.edit(f"<b>🚀 Понг!\n</b>⌛ {round(ping)} ms | {connect}")

module_list['Ping'] = f'{Config.prefix}{moduleName}'
file_list['Ping'] = f'{moduleName}.py'

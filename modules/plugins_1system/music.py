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

moduleName = 'music'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def music(client: Client, message: types.Message):
    await message.edit(f"🌐 <b>Получение песни...</b>")
    song = message.text.replace(" ", "%20").split()[0].replace("%20", " ").replace(f'{Config.prefix}{moduleName} ', '')
    bot_results = await client.get_inline_bot_results("Buddy_musicbot", song)

    #await message.delete()
    await message.reply_inline_bot_result(
            bot_results.query_id,
            bot_results.results[0].id
    )

module_list['Music'] = f'{Config.prefix}{moduleName} [author] [song name]'
file_list['Music'] = f'{moduleName}.py'

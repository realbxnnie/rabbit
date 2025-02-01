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

moduleName = 'restart'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def restart(client: Client, message: types.Message):
    await message.edit(f"✅ <b>Юзербот был успешно перезапущен!</b>")
    Config.restart_userbot()


module_list['Restart'] = f'{Config.prefix}{moduleName}'
file_list['Restart'] = f'{moduleName}.py'

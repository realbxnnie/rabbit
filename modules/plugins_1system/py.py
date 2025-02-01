from pyrogram import Client, filters, types, enums
from modules.plugins_1system.settings.main_settings import module_list, file_list, Config
from time import *
from glob import glob
from io import StringIO
from shlex import split

import sys
import json
import os
import requests
import modules.plugins_1system.settings.main_settings 

def count(dict):
    i = 0
    for j in dict:
        i += 1

    return i

moduleName = 'py'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def py(client: Client, message: types.Message):

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    returned = eval(message.text.replace(f'{Config.prefix}{moduleName} ',''))

    sys.stdout = old_stdout 

    await message.edit(f"👨🏻‍💻 <b>Результат</b>:\n<code>{mystdout.getvalue()}</code>\n📩 <b>Код вернул</b>:\n<code>{returned}</code>")
    

module_list['Python'] = f'{Config.prefix}{moduleName} [code]'
file_list['Python'] = f'{moduleName}.py'

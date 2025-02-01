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
import webbrowser

from selenium import webdriver

def count(dict):
    i = 0
    for j in dict:
        i += 1

    return i

moduleName = 'quit'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def quit(client: Client, message: types.Message):
    await message.edit(f"✅ <b>Юзербот был успешно выключен</b>")
    exit()
    

module_list['Quit'] = f'{Config.prefix}{moduleName}'
file_list['Quit'] = f'{moduleName}.py'

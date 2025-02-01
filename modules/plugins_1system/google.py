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

moduleName = 'google'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def web(client: Client, message: types.Message):
    if Config.showlinks == "True":
        print(message.text)
        await message.edit(f"🌐 <b><a href=google.com/search?q={message.text.replace(' ', '%20').replace(f'{Config.prefix}{moduleName}', '')}>Найдено в Google</a></b>")
    else:
        await message.edit(f"❌ <b>Ссылки выключены! Включите ссылки и попробуйте снова.</b>")
    

module_list['Google'] = f'{Config.prefix}{moduleName} [request]'
file_list['Google'] = f'{moduleName}.py'

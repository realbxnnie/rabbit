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

moduleName = 'web'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def web(client: Client, message: types.Message):
    driver = None
    if webbrowser.get().basename == "firefox":
        driver = webdriver.Firefox()
    elif webbrowser.get().basename == "chrome" or webbrowser.get().basename == "google" or webbrowser.get().basename == "google chrome":
        driver = webdriver.Chrome()
    elif webbrowser.get().basename == "edge":
        driver = webdriver.Edge()
    elif webbrowser.get().basename == "ie":
        driver = webdriver.Ie()
    elif webbrowser.get().basename == "safari":
        driver = webdriver.Safari()

    driver.get(message.text.split()[1])

    sleep(2)
    
    driver.save_screenshot("tmp/web.png")

    await client.delete_messages(message.chat.id, [message.id])
    await client.send_photo(message.chat.id, "tmp/web.png", f"🌐 <b>{Config.showlinks == "True" and message.text.split()[1] or '(скрыто)'}</b>")
    
    driver.close()
    

module_list['Web'] = f'{Config.prefix}{moduleName} [web link]'
file_list['Web'] = f'{moduleName}.py'

from pyrogram import Client, filters, types, enums
from modules.plugins_1system.settings.main_settings import module_list, file_list, Config
from time import *
from glob import glob

from pathlib import Path

from wand.image import Image

import json
import os
import requests
import modules.plugins_1system.settings.main_settings 

import qrcode
import qrcode.image.svg

def totext(text: str):
    return text.replace(f'{Config.prefix}{moduleName}', '')

def count(dict):
    i = 0
    for j in dict:
        i += 1

    return i

moduleName = 'qrcode'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & (Config.cmdrights == "all" and filters.all or filters.me ))
async def qrcode(client: Client, message: types.Message):
    if Config.showlinks == "True":
        await message.edit(f"🌐 <b>Генерация QR-Кода...</b>")
        img = qrcode.make(message.text.split()[1], image_factory=qrcode.image.svg.SvgImage)
        if not os.path.exists("tmp/qr.svg"): 
            Path.touch("tmp/qr.svg")
        with open('tmp/qr.svg', 'wb') as qr:
            img.save(qr)

        with Image( blob=bytes(open('tmp/qr.svg', 'r').read().encode('utf-8')), format="svg" ) as image:
            png_image = image.make_blob("png")
            if not os.path.exists("tmp/qr.png"):
                Path.touch('tmp/qr.png')
            
            open('tmp/qr.png', 'wb').write(png_image)

        os.remove('tmp/qr.svg')

        await message.delete()
        await client.send_photo(chat_id=message.chat.id, photo='tmp/qr.png', caption='⌨️ <b>QR-Code</b>')
    else:
        await message.edit(f"❌ <b>Ссылки выключены! Включите ссылки и попробуйте снова.</b>")

module_list['Qrcode'] = f'{Config.prefix}{moduleName} [web link]'
file_list['Qrcode'] = f'{moduleName}.py'

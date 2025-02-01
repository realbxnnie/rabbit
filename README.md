# 🐇 Rabbit
Fast as light.

## Rabbit is a powerful userbot for Telegram.

[?] Does my os supports Rabbit?
| Operating System  | Support |
| ------------- | ------------- |
| Linux  | ✅ Yes |
| Windows  | ✅ Yes |
| macOS    | ✅ Yes  |

[?] What i need to install Rabbit?\
**• Python 3.xx**\
**• python-pyrogram**\
**• Telegram Account API_ID & API_HASH**\
**• Telegram Account Username / Userid & Telegram Account Phone Number**

[?] Where can i download Rabbit?\
**• [Here.](https://github.com/realbxnnie/rabbit/releases/latest)**

[?] How do i make custom module?\
**• Edit this template and upload it somewhere as a raw text:**
```python
from pyrogram import Client, filters, types, enums
from modules.plugins_1system.settings.main_settings import module_list, file_list, Config

moduleName = 'example'

@Client.on_message(filters.command(moduleName, prefixes=Config.prefix) & filters.me)
async def example(client: Client, message: types.Message):
    await message.edit(f"<b>This is an example module!</b>")
    exit()
    

module_list['Example'] = f'{Config.prefix}{moduleName}'
file_list['Example'] = f'{moduleName}.py'
```
>[!NOTE]
> [Join our Telegram Channel!](rabbit_userbot.t.me)

Inspired by Hikka & FoxUserbot.
Uses FoxUserbot's Module System.

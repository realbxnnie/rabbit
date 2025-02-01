from pyrogram import Client, filters
from modules.plugins_1system.settings.main_settings import module_list, file_list




@Client.on_message(filters.command("test", prefixes=".") & filters.me)
async def example_edit(client, message):
    await message.edit("<b>ok</b>")


module_list['Test'] = f'.test'
file_list['Test'] = 'exampleC.py'

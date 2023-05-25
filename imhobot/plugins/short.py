import requests
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("short", prefixes=prefix) & filters.me)
async def shorten_link_command(client, message):
    try:
        await message.edit("Shorting...")
        if message.reply_to_message:
            link = message.reply_to_message.text
        else:
            link = message.command[1]

        token = "6c2ac1846a1c1A2d5f88A3E5fbf0e14fcf96d7d0"
        get_short_url = requests.post("https://api.waa.ai/v2/links", json={"url": link},
                                      headers={"Authorization": f"API-Key {token}"}).json()["data"]
        await message.edit(f"Short URL: {get_short_url['link']}")
    except Exception as error:
        message.edit(f"Error: {error}")


module_list['ShortURL'] = f'{prefix}short [Reply | link]'
file_list['ShortURL'] = 'short.py'

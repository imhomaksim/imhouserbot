from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('support', prefixes=prefix) & filters.me)
async def support(client, message):
    await message.delete()
    await client.send_photo(
        chat_id=message.chat.id,
        photo="https://raw.githubusercontent.com/imhomaksim/imhouserbot/7f2351c8954db8521a82d5a3e7d74481bc45f985/imhobot/logo.png?token=GHSAT0AAAAAACCB3V466WROUWYM2OVR66B6ZDRZ24Q",
        caption="Support: @imhomaksim"
    )


module_list['Support'] = f'{prefix}support'
file_list['Support'] = 'support.py'

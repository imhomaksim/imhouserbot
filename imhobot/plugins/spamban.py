from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import asyncio

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("spamban", prefixes=prefix) & filters.me)
async def spamban(client, message):
    await message.edit("Checking your account for Spamban...")
    await client.unblock_user("spambot")
    await client.send_message("spambot", "/start")
    async for iii in client.get_chat_history("spambot", limit=1):
        await message.edit(iii.text)


module_list['SpamBan'] = f'{prefix}spamban'
file_list['SpamBan'] = 'spamban.py'

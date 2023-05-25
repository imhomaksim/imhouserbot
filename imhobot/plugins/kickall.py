import asyncio
import re
from datetime import datetime, timedelta
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('kickall', prefixes=prefix) & filters.me)
async def kickall(client, message):
    await message.edit("kick all chat members!")
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass


@Client.on_message(filters.command('kickall_hide', prefixes=prefix) & filters.me)
async def kickall_hide(client, message):
    await message.delete()
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass


@Client.on_message(filters.command("kickall_withbot", prefixes=prefix) & filters.me)
async def tagall(client, message):
    await message.delete()
    chat_id = message.chat.id
    icm = client.get_chat_members(chat_id)
    async for member in icm:
        string = f"/ban {member.user.mention}\n"
        await client.send_message(chat_id, text=string)


@Client.on_message(filters.command('kickdeleted', prefixes=prefix) & filters.me)
async def kickall(client, message):
    await message.edit("kick all deleted account from members!")
    member = client.get_chat_members(message.chat.id)
    deleted = 0
    async for alls in member:
        try:
            l = alls.user.first_name
            if alls.user.first_name == None:
                await client.ban_chat_member(message.chat.id, alls.user.id, datetime.now() + timedelta(days=1))
                deleted += 1
        except:
            pass
    await message.edit(f"Completed!\nI kicked {deleted} deleted accounts!")

module_list['KickAllSubs'] = f'{prefix}kickall | {prefix}kickall_withbot | {prefix}kickdeleted'
file_list['KickAllSubs'] = 'kickall.py'
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from plugins.restarter import restart
import os

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('unloadmod', prefixes=prefix) & filters.me)
async def unloadmod(client, message):
    try:
        module_name = message.text.replace(f'{prefix}unloadmod', '')
        params = module_name.split()
        module_name = params[0]
        del module_list[module_name]
        file = file_list[module_name]
        os.remove(f'plugins/{file}')
        await message.edit("**The module has been successfully unloaded.**\nRestart...")
        await restart(message, restart_type="restart")
    except Exception as error:
        await message.edit(f"**An error has occurred.**\nLog: not found {error}")


module_list['Unloadmod'] = f'{prefix}unloadmod [module name]'

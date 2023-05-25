from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
import secrets
import string

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('gen_password', prefixes=prefix) & filters.me)
async def gen_pass(client, message):
    char = message.command[1]
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(int(char)))
    await message.edit(f"**Generated password:** ```{password}```")


module_list['GeneratePassword'] = f'{prefix}gen_password [password length]'
file_list['GeneratePassword'] = 'gen_pass.py'

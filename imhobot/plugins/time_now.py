from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from datetime import datetime
from dateutil import tz

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("time") & filters.me)
async def time(client, message):
    format_string = message.text.split(maxsplit=1)[1].strip() or "%d/%m/%Y %H:%M:%S"
    now = datetime.datetime.now()
    await message.reply_text(f"Сейчас {now.strftime(format_string)}")


module_list['TimeNow'] = f'{prefix}time'
file_list['TimeNow'] = 'time_now.py'

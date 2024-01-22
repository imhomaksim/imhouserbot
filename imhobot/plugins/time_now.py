from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list
from datetime import datetime
from dateutil import tz

from prefix import my_prefix
prefix = my_prefix()

SUPPORTED_LOCALES = {"en": "%d/%m/%Y\n%H:%M:%S", "ru": "%d.%m.%Y\n%H:%M:%S"}

@Client.on_message(filters.command("time", prefixes=prefix) & filters.me)
async def time(client, message):
    locale = message.from_user.language_code or "en"
    format_string = SUPPORTED_LOCALES.get(locale)

    tz_name = message.text.split(maxsplit=1)[1].strip() or None
    if tz_name:
        try:
            tz_obj = tz.gettz(tz_name)
        except ZoneNotFoundError:
            await message.reply_text(f"Invalid timezone: {tz_name}")
            return

    now = datetime.now(tz.UTC)
    if tz_obj:
        now = now.astimezone(tz_obj)

    await message.edit(now.strftime(format_string))

module_list['TimeNow'] = f'{prefix}time'
file_list['TimeNow'] = 'time_now.py'

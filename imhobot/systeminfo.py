import platform
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("systeminfo", prefixes=prefix) & filters.me)
async def sysinfo(client, message):
    system_info = platform.uname()
    kernel_info = platform.release()
    await message.reply_text(f"🖥System: {system_info.system}\n🎩Name: {system_info.node}\n💎Version: {system_info.version}\n⛩Machine: {system_info.machine}\n📼Processor: {system_info.processor}\n🧨Kernel Version: {kernel_info}")


module_list['systeminfo'] = f'{prefix}infosystem'
file_list['systeminfo'] = 'systeminfo.py'

import platform
import psutil
from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("systeminfo", prefixes=prefix) & filters.me)
async def sysinfo(client, message):
    system_info = platform.uname()
    kernel_info = platform.release()

    # Получаем информацию о памяти
    ram = psutil.virtual_memory()
    ram_total = f"{ram.total / (1024 ** 3):.2f} GB"
    ram_used = f"{ram.used / (1024 ** 3):.2f} GB"
    ram_free = f"{ram.free / (1024 ** 3):.2f} GB"

    # Получаем информацию о диске
    disk = psutil.disk_usage("/")
    disk_total = f"{disk.total / (1024 ** 3):.2f} GB"
    disk_used = f"{disk.used / (1024 ** 3):.2f} GB"
    disk_free = f"{disk.free / (1024 ** 3):.2f} GB"

    # Форматируем сообщение с информацией
    info_message = (
        f"🖥System: {system_info.system}\n"
        f"🎩Name: {system_info.node}\n"
        f"💎Version: {system_info.version}\n"
        f"⛩Machine: {system_info.machine}\n"
        f"📼Processor: {system_info.processor}\n"
        f"🧨Kernel Version: {kernel_info}\n\n"
        f"💾Memory:\n"
        f"    Total: {ram_total}\n"
        f"    Used: {ram_used}\n"
        f"    Free: {ram_free}\n\n"
        f"💿Disk Space:\n"
        f"    Total: {disk_total}\n"
        f"    Used: {disk_used}\n"
        f"    Free: {disk_free}"
    )

    await message.reply_text(info_message)
    await message.delete() 

module_list['systeminfo'] = f'{prefix}infosystem'
file_list['systeminfo'] = 'systeminfo.py'

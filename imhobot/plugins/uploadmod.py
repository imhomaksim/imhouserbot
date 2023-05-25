from pyrogram import Client, filters
from plugins.settings.main_settings import module_list, file_list

from prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command('uploadmod', prefixes=prefix) & filters.me)
async def uploadmod(client, message):
    try:
        module_name = message.text.replace(f'{prefix}uploadmod', '')
        params = module_name.split()
        module_name = params[0]
        file = file_list[module_name]
        await client.send_document(
            message.chat.id,
            f"plugins/{file}",
            caption=f"Module `{module_name}`\nfor FoxUserbot 🦊"
        )
        await message.delete()
    except Exception as error:
        await message.edit(f"**An error has occurred.**\nLog: {error}")


module_list['Uploadmod'] = f'{prefix}uploadmod [module name]'

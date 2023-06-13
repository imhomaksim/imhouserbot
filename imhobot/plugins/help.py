from pyrogram import Client, filters, __version__
from plugins.settings.main_settings import module_list, version
from platform import python_version

from prefix import my_prefix
prefix = my_prefix()

gif_url = 'https://media.tenor.com/1Hrns1iY5R4AAAAC/bojack-horseman.gif'
logo_url = 'https://raw.githubusercontent.com/imhomaksim/imhouserbot/main/imhobot/logo.png'

@Client.on_message(filters.command('help', prefixes=prefix) & filters.me)
async def helps(client, message):
    await message.edit('Loading the help menu. Please, wait...')
    lists = []
    for k, v in module_list.items():
        lists.append(f'➣ {k}: {v}<br>')
    a = " "
    for i in lists:
        a = a.lstrip() + f'{i}'
    helpes = f"""
{len(module_list)} available modules.<br>
<br>
{a}
"""
    # добавляем гифку и логотип в сообщение
    logo = f'<a href="{logo_url}">&#8205;</a>'
    await message.edit(f"""
<b>{logo}💫 | ImhoUserbot RUNNING</b>
<b>♻ | Version userbot: {version}</b>
<b>🐍 | Python: {python_version()}</b>
<b>🥧 | Pyrogram: {__version__}</b>
<b>💼 | Modules: {len(module_list)}</b>

❤️ | Thanks for using imhoUserbot.
❤️ | для связи пишите мне в телеграм @imhomaksim.

<img src="{gif_url}" alt="gif">
""")
    # добавляем логотип в качестве фото к сообщению
    await message.reply_photo(photo=logo_url, caption=helpes, parse_mode=None)
    
module_list['Help'] = f'{prefix}help'



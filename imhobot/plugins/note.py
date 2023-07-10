import os
from pyrogram import Client, filters
from pyrogram.types import Message
from plugins.settings.main_settings import module_list, file_list
from prefix import my_prefix

prefix = my_prefix()

@Client.on_message(filters.command("save", prefixes=prefix) & filters.me)
async def save_note_command(client, message: Message):
    if not message.reply_to_message:
        await message.edit("<code>Ответьте на сообщение, чтобы сохранить его как заметку.</code>")
        return
    
    note_name = message.text.split(" ", 1)[1]
    content = message.reply_to_message.text
    
    note_path = f'notes/{note_name}.txt'
    
    with open(note_path, 'w') as file:
        file.write(content)
    
    await message.edit(f"<code>Заметка '{note_name}' успешно сохранена.</code>")

@Client.on_message(filters.command("get", prefixes=prefix) & filters.me)
async def get_note_command(client, message: Message):
    note_name = message.text.split(" ", 1)[1]
    note_path = f'notes/{note_name}.txt'
    
    if not os.path.exists(note_path):
        await message.edit(f"<code>Заметка '{note_name}' не найдена.</code>")
        return
    
    with open(note_path, 'r') as file:
        content = file.read()
    
    await message.edit(f"<b>Заметка: {note_name}</b>\n\n{content}")

@Client.on_message(filters.command("delete", prefixes=prefix) & filters.me)
async def delete_note_command(client, message: Message):
    note_name = message.text.split(" ", 1)[1]
    note_path = f'notes/{note_name}.txt'
    
    if not os.path.exists(note_path):
        await message.edit(f"<code>Заметка '{note_name}' не найдена.</code>")
        return
    
    os.remove(note_path)
    
    await message.edit(f"<code>Заметка '{note_name}' успешно удалена.</code>")

module_list['Note'] = f'{prefix}note'
file_list['Note'] = 'note.py'
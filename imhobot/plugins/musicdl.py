from plugins.settings.main_settings import module_list, file_list
from prefix import my_prefix
prefix = my_prefix()
import utils


@Client.on_message(filters.command("mdl", prefixes=prefix) & filters.me)
async def mdl(client, message):
    args = utils.get_args_raw(message)
    if not args:
        await utils.answer(message, utils.strings("args"))
        return

    message = await utils.answer(message, utils.strings("loading"))
    result = await self.musicdl.dl(args, only_document=True)

    if not result:
        await utils.answer(message, utils.strings("404").format(args))
        return

    await message.reply_document(
        result,
        caption=f"🎧 {utils.ascii_face()}",
        reply_to=getattr(message, "reply_to_msg_id", None),
    )
    if message.out:
        await message.delete()


module_list['MusicDL'] = f'{prefix}mdl'
file_list['MusicDL'] = 'musicdl.py'


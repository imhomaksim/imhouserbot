import os
from rich import print
from plugins.settings.main_settings import version

from prefix import my_prefix
prefix = my_prefix()

os.system("cls" if os.name == "nt" else "clear")
print(f"""[red]
imhobot started
[/red][green]
Channel: @shahimatb
Version: [red]{version}[/red]
Prefix: [[red]{prefix}[/red]]

Client [red]Started[/red]
Type [red]{prefix}ping[/red] to check Userbot works
[/green]""")

# For @LionHelp
"""Check if your userbot is working."""
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from Lion import ALIVE_NAME, CMD_HELP, lionver
from Lion.__init__ import StartTime
from Lion.LionConfig import Config, Var

# ======CONSTANTS=========#
CUSTOM_ALIVE = (
    Var.CUSTOM_ALIVE
    if Var.CUSTOM_ALIVE
    else "𝚈𝙾𝙾!! 𝚈𝙾𝚄𝚁 𝙻𝙸𝙾𝙽 𝚄𝙱 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴"
)
ALV_PIC = Var.ALIVE_PIC if Var.ALIVE_PIC else None
lionmoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**✘**"
if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# ======CONSTANTS=========#


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time



FUKING_USER = str(ALIVE_NAME) if ALIVE_NAME else "ℓιση υsεявσт"

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet😁😁"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet😁😁"

SHASHANKXD = VAR.ALIVEPOTO if ALIVEPOTO else "https://telegra.ph/file/9c919ae0a8f31d70a8dfe.jpg"

from Lion import CMD_LIST

theshashankk = "**Lɪᴏɴ ᴜsᴇʀʙᴏᴛ Is ᴀʟɪᴠᴇ**\n\n"
theshashankk += f"**му ρєяσ мαѕтєя**          : {FUKING_USER}\n"
theshashankk += f"🚑 𝚂𝚄𝙿𝙿𝙾𝚁 𝙶𝚁𝙾𝚄𝙿 🚑 : [Lion Support](telegram.dog/LionXsupport)\n"  
theshashankk += f"ℹ️ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: "
theshashankk += f"`𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽`       : {lionver}\n"
theshashankk += "`𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽`           : 3.9.0\n\n"
theshashankk += "`✨ 𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈 `          : [ᴊᴏɪɴ](https://t.me/blacklightningot)\n"
theshashankk += "`𝚈𝙾𝚄𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 👾`            : [ᴊᴏɪɴ](https://t.me/lightningsupport)\n"
theshashankk += "`𝙈𝙔 𝘿𝙀𝙑 👇👇`\n"
theshashankk += "[𝐌𝐃 𝐍𝐎𝐎𝐑•DEV](t.me/SimpleBoy786)\n"
theshashankk += " [𝐒𝐇𝐀𝐒𝐇𝐀𝐍𝐊•DEV](telegram.dog/shashankxD)"

@Lion.on(admin_cmd(outgoing=True, pattern="alive"))
@Lion.on(admin_cmd(outgoing=True, pattern="alive"), allow_sudo=True))
async def shashankxD(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, SHASHANKXD, caption=theshashank)
    await alive.delete()


CMD_HELP.update({"alive": "➟ `.alive`\nUse - Check if your bot is working."})

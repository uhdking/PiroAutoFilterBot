import time
import random
from pyrogram import Client, filters

CMD = ["/"]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("š”šš½š½š šØšŗš š šššš¾ :) š§šš /start \n\nš§šš /help š„šš š§š¾šš ;)\n\n\nš§šš /ping š³š š¢šš¾š¼š š”šš šÆššš š")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("š§šš /movie š„šš š¬šššš¾ š²š¾šŗšš¼š š±ššš¾š š\n\nš§šš /series š„šš š²š¾ššš¾š š²š¾šŗšš¼š š±ššš¾š š")


@Client.on_message(filters.command("movie", CMD))
async def movie(_, message):
    await message.reply_text("ā ļøāļø š š¼šš¶š² š„š²š¾šš²šš šš¼šæšŗš®š āļøā ļø\n\nš š¬šššš¾ š­šŗšš¾, šøš¾šŗš,(šØšæ ššš šŖššš) š¶ššš š¢šššš¾š¼š š²šš¾ššššš š\n\nš£ šØšæ šØš šš šŗ š„ššš š²š¾ššš¾š. š±š¾ššš¾šš š®šš¾ š”š š®šš¾ š¶ššš šÆšššš¾š š­šŗšš¾ š§ \n\nššš±šš¦š©š„š:\n\nā¢ Robin Hood ā\nā¢ Avatar 2009 ā\nā¢ Kurup 2021 Kan ā\n\nš„± š„šš š«šŗššššŗšš¾ š šš½ššš - šŖšŗš šæšš šŖšŗšššŗš½šŗ, š¬šŗš - š¬šŗššŗššŗššŗš, š³šŗš - š³šŗššš\n\nš š“šš¾ š„šššš 3 š«š¾ššš¾šš š®šæ š«šŗššššŗšš¾ š„šš š šš½ššš [šŖšŗš š³šŗš š³š¾š š¬šŗš š§šš š²ššŗ š¤šš šŖšš š¾šš¼...]\n\nā [šš¼š»š šØšš² šš¼šæš±š šš¶šøš² šššÆšÆš²š±/š š¼šš¶š²š/š¦š²š»š±/šš , . : - š²šš°] ā")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("ā ļøāļø š¦š²šæš¶š²š š„š²š¾šš²šš šš¼šæšŗš®š āļøā ļø\n\nš£ š²š¾ššš¾š š­šŗšš¾,š²š¾šŗššš (š¶ššš¼š š²š¾šŗššš ššš ššŗšš) š§ \n\nššš±šš¦š©š„š: \n\nā¢ Game Of Thrones S03š¤02 720š ā\nā¢ Sex Education S02 720p ā \nā¢ Breaking Bad S01E05 ā \nā¢ Prison Break 1080p ā \nā¢ Witcher S02 ā\n\nš„± š„šš š²š¾šŗššš š¬š¾ššššš š š š²01 š„šš š²š¾šŗššš 1, š²02 š„šš š²š¾šŗššš 2 š¾šš¼ [š²03,š²04 ,š²06,š²10,š²17] š¦šš¾š š«ššš¾ š³ššŗš\n\nš š„šš š¤ššššš½š¾ š¬š¾ššššš š š š¤š01 š„šš š¤ššššš½š¾ 1, š¤š02 š„šš š¤ššššš½š¾ 2 š¾šš¼ [š¤š03,š¤š07,š¤š17,š¤š21] š¦š'š š«ššš¾ š³ššŗš \n\nā [šš¼š»š šØšš² šš¼šæš±š šš¶šøš² š¦š²š®šš¼š»/šš½š¶šš¼š±š²/š¦š²šæš¶š²š , . : - š²šš°] ā")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"šÆššš!\n{time_taken_s:.3f} ms")

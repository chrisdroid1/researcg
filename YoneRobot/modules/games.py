from telethon.tl.types import InputMediaDice

from YoneRobot.events import register


@register(pattern="^/dice(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice(""))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("hey nigga use number 1 to 6 only")


@register(pattern="^/dart(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("ð¯"))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("hey nigga use number 1 to 6 only")


@register(pattern="^/ball(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("ð"))
    input_int = int(input_str)
    if input_int > 5:
        await event.reply("hey nigga use number 1 to 6 only")


__help__ = """
 *Play Game With Emojis:*
  
  â® /dice ÏÑ /dice 1 ÑÏ 6 Î±Î·Ñ Î½Î±âÏÑ
 
  â® /ball ÏÑ /ball 1 ÑÏ 5 Î±Î·Ñ Î½Î±âÏÑ

  â® /dart ÏÑ /dart 1 ÑÏ 6 Î±Î·Ñ Î½Î±âÏÑ
       `ððððð: ðððððð ðððð ð ððððð.`

  `â ï¸á´¡á´ÊÉ´ÉªÉ´É¢: Êá´á´ á´¡á´á´Êá´ Êá´ ÉªÉ´ á´Êá´á´ÊÊá´ Éªê° Êá´á´ ÉªÉ´á´á´á´ á´É´Ê á´á´Êá´Ê á´ á´Êá´á´ á´Êá´É´ á´á´É´á´Éªá´É´á´á´.`
"""

__mod_name__ = "Gá´á´á´ê±ð®"

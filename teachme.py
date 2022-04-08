import time

from nonebot.typing import State_T
from hoshino import Service, priv
from hoshino.typing import CQEvent
from collections import defaultdict
import base64, os, re, asyncio, json, traceback
from io import BytesIO
from PIL import Image

sv = Service('teachme', help_='''
等会再写
'''.strip())

teach_path = os.path.join(os.path.dirname(__file__), 'teach.jpg')
module_path = os.path.split(os.path.dirname(__file__))[0]

mai_res = os.path.join(module_path, 'maimaiDX/static/mai/cover')#maimai资源目录
#mai_res = 'C:/Users/Administrator/Desktop/bot/HoshinoBot/hoshino/modules/maimaiDX/static/mai/cover/'

arc_res = os.path.join(module_path, 'Arcaea/img/song')#arcaea资源目录
#arc_res = 'C:/Users/Administrator/Desktop/bot/HoshinoBot/hoshino/modules/Arcaea/img/song/'

def image_to_base64(img, format='PNG'):
    output_buffer = BytesIO()
    img.save(output_buffer, format)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str

@sv.on_rex(r'^教教\s?id\s?([0-9]+)')
async def teach_me(bot, ev: CQEvent):
    match = ev['match']
    base_img = Image.open(teach_path)
    name = match.group(1)
    jpgPath = os.path.join(mai_res, f'{name}.jpg')
    pngPath = os.path.join(mai_res, f'{name}.png')
    try:
        tmp_img = Image.open(jpgPath)
        box = (184,327,335,478)
        region = tmp_img
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        base_img.paste(region, (184,327))
        await bot.send(ev, f'[CQ:image,file=base64://{image_to_base64(base_img).decode()}]')
    except:
        try:
            tmp_img = Image.open(pngPath)
            box = (184,327,335,478)
            region = tmp_img
            region = region.resize((box[2] - box[0], box[3] - box[1]))
            base_img.paste(region, (184,327))
            await bot.send(ev, f'[CQ:image,file=base64://{image_to_base64(base_img).decode()}]')
        except:
            await bot.send(ev, '教不了教不了', at_sender=True)
        
        
@sv.on_rex(r'^教教\s?([a-z]+)$')
async def teach_me(bot, ev: CQEvent):
    match = ev['match']
    base_img = Image.open(teach_path)
    name = match.group(1)
    pngPath = os.path.join(arc_res, f'{name}/base.jpg')
    try:
        tmp_img = Image.open(pngPath)
        box = (184,327,335,478)
        region = tmp_img
        region = region.resize((box[2] - box[0], box[3] - box[1]))
        base_img.paste(region, (184,327))
        await bot.send(ev, f'[CQ:image,file=base64://{image_to_base64(base_img).decode()}]')
    except:
        await bot.send(ev, '教不了教不了', at_sender=True)
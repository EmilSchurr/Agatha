import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
import os
import asyncio
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random

bot = commands.Bot(command_prefix='!', description='Agatha', intents=discord.Intents.all())
@bot.event
async def on_ready(): 
    print('Agatha is at your service')
@bot.command()
async def play(ctx, command_name: str):
    file_path = f"files/dir{command_name}.mp3"
    if os.path.isfile(file_path):
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()
        source = FFmpegPCMAudio(file_path)
        voice_client.play(source)
        while voice_client.is_playing():
            await asyncio.sleep(1)
        await voice_client.disconnect()
    else:
        await ctx.send(f"Der Oger wurde Betrogen und konnte {command_name} nicht finden")
@bot.command()
async def load(ctx):
    await ctx.send("Scanning for new files...")
    await ctx.send("Deepfrying audio files...")
    for filename in os.listdir('upload/dir'):
                os.system('ffmpeg-normalize upload/dir'+filename+' -o files/dir'+filename+' -c:a mp3')
                os.system('rm -f upload/dir'+filename)
    await ctx.channel.purge(limit=2)
    await ctx.send('Done')
@bot.command()
async def commands(ctx):
    logo = Image.open('/var/www/html/assets/hyper_logo.png')
    image_width = 1280
    image_height = 800
    font_size = 24
    image = Image.new(mode='RGBA', size=(1300, 820), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/var/www/html/assets/Rubik-Regular.ttf', font_size)
    number = str(random.randint(1000000000, 9999999999))#create a random number so discord renders the image with new commands
    text = number
    filenames = os.listdir('/home/emil_schurr/normalized')
    commands_str = ", ".join([os.path.splitext(filename)[0] for filename in filenames])
    lines = []
    current_line = ""
    for name in commands_str.split(", "):
        new_line = current_line + ", " + name if current_line else name
        text_width, _ = font.getsize(new_line)
        if text_width > image_width:
            lines.append(current_line)
            current_line = name
        else:
            current_line = new_line
    if current_line:
        lines.append(current_line)
    line_height = font_size + 10
    x = 10
    y = 10
    for line in lines:
        draw.text((x, y), line, font=font, fill=(255, 255, 255))
        y += line_height
    #hyper-important hyper-logo
    logo_size = (int(image.width * 0.1), int(image.height * 0.11))
    logo_x = image.width - logo_size[0]
    logo_y = image.height - logo_size[1]
    logo = logo.resize(logo_size)
    image.paste(logo, (logo_x, logo_y))
    image.save('/var/www/html/bot/commands/'+number+'.png')

    await ctx.send("https://emilano.de/bot/commands/"+number+".png")
bot.run('SECRET')

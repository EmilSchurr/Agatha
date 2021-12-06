import discord
import asyncio
import time
#import youtube_dl
import functools
import itertools
import math
import random
from discord.ext import commands
from async_timeout import timeout
import os
from os import listdir
from os.path import isfile, join
import mysql.connector


print('Agetha is under the water and needs your help, so come by her office to discuss the details')

command_prefix = "!"
client = discord.Client(command_prefix = '!')

@client.event
async def on_ready(): 
    print('Agatha is at your service')
    #print('Agetha is under the water and needs your help, so come by her office to discuss the details')
    # nötig?
    # jaaa??!

@client.event
async def on_message(message):
    #Check if the author is the bot
    if message.author.bot:
        return
    #split the message and store in agrment array  
    argument = message.content[1:].lower().split()

    if message.content.startswith(command_prefix):
        
        #here should follow a help command
        #now there is a hlep command
        if argument[0] == "help":
            files = [f for f in listdir("/home/emil_schurr/discord_bots/agatha/normalized") if isfile(join("/home/emil_schurr/discord_bots/agatha/normalized", f))]
            await message.channel.send(str(files)+ " clear, leave, ping, load")

        #ping    
        if argument[0] == "ping":
            await message.channel.send('My ping is ' + str(round(client.latency * 1000)) + ' ms, how about yours?')

        #disconnect
        if argument[0] == "leave":
            await voicechannel.disconnect()
        
        #purge
        if argument[0] == "clear":
            amount = int(argument[1])+1
            deleted = await message.channel.purge(limit=amount)
            await message.channel.send('Deleted {} message(s)'.format(len(deleted)-1))
            await asyncio.sleep(5)
            await message.channel.purge(limit=1)

        #normalize
        if argument[0] == "load":
            await message.channel.send('Copying files...')
            await message.channel.send('Applying earrape protection...')
            for filename in os.listdir('/home/emil_schurr/discord_bots/agatha/mp3'):
                os.system('ffmpeg-normalize /home/emil_schurr/discord_bots/agatha/mp3/' +filename)
            await message.channel.purge(limit=2)
            await message.channel.send('Done')

        if argument[0] == "restart":
            await message.channel.send('Restarting... This may take a while')
            os.system('/home/emil_schurr/discord_bots/agatha/agatha.sh')
            exit()

        #play filename    
        else:
            channel = message.author.voice.channel
            voicechannel = await channel.connect()
            voicechannel.play(discord.FFmpegPCMAudio('/home/emil_schurr/discord_bots/agatha/normalized/' + argument[0] + '.mkv',)) 
            while voicechannel.is_playing():
                if argument[0] == "leave":
                    await voicechannel.disconnect()
                else:
                    time.sleep(2)
            else:
                await voicechannel.disconnect()
            #for scoreboard
            mydb = mysql.connector.connect(
                host="localhost",
                user="emil_schurr",
                password="SchnupfGurgel1",
                database="agatha"
            )
            mycursor = mydb.cursor()
            arg = str("'" + argument[0] + "'")
            sql = str("SELECT `counter` FROM `counter` WHERE `command`= " +arg)
            val = (arg)
            mycursor.execute(sql)
            c = mycursor.fetchone()
            print(c)
            if c == None:
                sql = "INSERT INTO counter (command, counter, uploaded, nr) VALUES (%s, %s, %s, %s)"
                val = (argument[0], "1", "hyperabstrakt", "1")
                mycursor.execute(sql, val)
                mydb.commit()
            else:
                cn = int(str(c)[1:-2])
                sql = str("UPDATE `counter` SET `counter`=" + str(cn+1) +  " WHERE `command`= " +arg)
                val = (cn+1, arg)
                print(cn+1)
                print(sql)
                mycursor.execute(sql)
                mydb.commit()
   
client.run('NzgyMzgxNzc2ODkzOTAyOTIw.X8LXzw.9TFGQBr62u7BQW-ufiN6I-pFFQw')

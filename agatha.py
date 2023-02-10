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
            await message.channel.send("Management Commands: clear [number of messages], leave, ping, load, top [number of rows]")
            await message.channel.send("https://emilano.de/assets/commands.png")
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
            for filename in os.listdir('/discord_bots/agatha/mp3/'):
                os.system('ffmpeg-normalize /discord_bots/agatha/mp3/'+filename+' -o normalized/'+filename+' -c:a mp3')
            await message.channel.purge(limit=2)
            await message.channel.send('Done')
        #restart
        if argument[0] == "restart":
            await message.channel.send('Restarting... This may take a while')
            os.system('/discord_bots/agatha/agatha.sh')
            exit()
        #scoreboard in discord
        if argument[0] == "top":
            cnx = mysql.connector.connect(host="*****", user="*****", password="*****", database="*****")
            cursor = cnx.cursor()
            sql = str('SELECT `command`, `counter` FROM `counter` ORDER BY `counter` DESC LIMIT '+ argument[1])
            cursor.execute(sql)
            for row in cursor:
                await message.channel.send(row)
            cursor.close()
            cnx.close()
        #play filename    
        else:
            channel = message.author.voice.channel
            voicechannel = await channel.connect()
            voicechannel.play(discord.FFmpegPCMAudio(normalized/' + argument[0] + '.mp3',)) 
            while voicechannel.is_playing():
                if argument[0] == "leave":
                    await voicechannel.disconnect()
                else:
                    time.sleep(2)
            else:
                await voicechannel.disconnect()
            #for scoreboard
            cnx = mysql.connector.connect(host="*****", user="*****", password="*****", database="*****")
            cursor = cnx.cursor()
            arg = str("'" + argument[0] + "'")
            sql = str("SELECT `counter` FROM `counter` WHERE `command`= " +arg)
            val = (arg)
            cursor.execute(sql)
            c = cursor.fetchone()
            print(c)
            if c == None:
                with cnx.cursor() as cursor:
                    sql = "INSERT INTO counter (command, counter, uploaded, nr) VALUES (%s, %s, %s, %s)"
                    val = (argument[0], "1", "hyperabstrakt", "1")
                    cursor.execute(sql, val)
                    cnx.commit()
                cursor.close()
            else:
                with cnx.cursor() as cursor:
                    cn = int(str(c)[1:-2])
                    sql = str("UPDATE `counter` SET `counter`=" + str(cn+1) +  " WHERE `command`= " +arg)
                    val = (cn+1, arg)
                    print(cn+1)
                    print(sql)
                    cursor.execute(sql)
                    cnx.commit()
                cursor.close()
client.run('*****')  


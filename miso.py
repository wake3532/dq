import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time


client = discord.Client()

owner = ['724769557759393837']
@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))


@client.event
async def on_member_join(member):
    try:
        sysc = member.guild.system_channel
        embed = discord.Embed(title=":4114110118_pandaclipartemojipand: 익명님이 입장하셧습니다. 환영해요!")
        embed.set_image(url="https://media.discordapp.net/attachments/760040615781072946/803580701819142184/banner.gif%22")
        await sysc.send(embed=embed)
    except:
        pass


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

import sys
import discord
import json
from collections import OrderedDict
import pprint
import re
import bot_token

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as', file=sys.stderr)
    print(client.user.name, file=sys.stderr)
    print(client.user.id, file=sys.stderr)
    print('------', file=sys.stderr)
    
@client.event



async def on_message(message):
    # 送り主がBotだった場合反応したくないので
    if message.author.bot:
        return
    # 「図鑑」で始まるか調べる
    if message.content == 'ざこやまの図鑑':
        message_send = "このbotの作成者ロト！" + "\n" + "不具合はtwitterで連絡するロト！"+ "\n" + "https://twitter.com/zakoyama_com"
        
    elif re.match('.+の図鑑$', message.content):
        json_open = open('pokedex_zen.json', 'r')
        json_load = json.load(json_open)    
        # メッセージを書きます
        m = message.content[0:len(message.content)-3]
        
        # メッセージが送られてきたチャンネルへメッセージを送ります
        if m in json_load:
            message_send = "```"
            for key, value in json_load[m].items():
                if key == 'No':
                    message_send = message_send + '%s.%s'%(key, value) + ' '
                elif key == 'ポケモン名':
                    message_send = message_send + '%s'%(value) + " \n"  + ' HP 攻撃 防御 特攻 特防 素早 合計\n'
                elif key == 'HP' :    
                    message_send = message_send + '%3d'%(int(value))
                else:    
                    message_send = message_send + '%4d'%(int(value))
                    
            message_send = message_send + "```"
            print('0 ' + m)
        else:
            message_send = "ポケモンがみつからないロト！"
            print('1 ' + m)
            
    await message.channel.send(message_send)
    
client.run(bot_token.TOKEN)

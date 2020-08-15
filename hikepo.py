# -----------------------------------------------------------------------------
# package dependencies
# -----------------------------------------------------------------------------

import discord
import os
import urllib.request

# -----------------------------------------------------------------------------
# bot client
# -----------------------------------------------------------------------------

BOT_ACCESS_TOKEN = os.environ['DISCORD_BOT_ACCESS_TOKEN']
client = discord.Client()

# -----------------------------------------------------------------------------
# message handlers
# -----------------------------------------------------------------------------

@client.event
async def on_ready():
    """
    bot サーバー起動ハンドラ
    """
    print('on_ready')
    print('I am hikepo')

@client.event
async def on_message(message):
    """
    メッセージハンドラ
    """
    # bot の発言は無視
    if message.author.bot:
        return
    # 生存確認用
    if message.content == '/hike':
        await message.channel.send('わかる')
        return
    # terraria サーバー起動
    if message.content == '/terraria':
        await message.channel.send('terraria サーバーを起動するめう')
        response = urllib.request.urlopen('https://asia-northeast1-terraria-280314.cloudfunctions.net/startInstance')
        if response.getcode() != 200:
            await message.channnel.send('HTTP status code: ' + resopnse.getcode())
            return
        await message.channel.send('terraria サーバーが立ち上がっためう！')
        await message.channel.send(response.read().decode('utf-8'))
        await message.channel.send('terraria を起動して Multiplayer --> Join via IP でワールドに入れるめうね')
        return

# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------

if __name__=='__main__':
    client.run(BOT_ACCESS_TOKEN)

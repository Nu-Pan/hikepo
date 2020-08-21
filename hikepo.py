# -----------------------------------------------------------------------------
# package dependencies
# -----------------------------------------------------------------------------

import discord
import os
import urllib.request
import random

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
    # ユーザー ID
    HIKEPO_ID = 742670624677167136
    HIKESHI_ID = 248814031350136832
    NUPAN_ID = 473852296116174852

    # message の中身を展開
    mentions_id = [m.id for m in message.mentions]

    # bot の発言は無視
    if message.author.bot:
        return
    # オリジナルへのメンションを横取り
    elif HIKESHI_ID in mentions_id:
        await message.channel.send(
            message.author.mention + ' '
            + random.choice([
            'つれー実質１時間しか寝てないからつれーわー。実質一時間しか寝てないからな。',
            '(カチャカチャカチャカチャ…)(ッターン！)',
            'かぁーっ！　今から帰っても２時間しかねれないわ～！　ほら見て？　かぁーっ！',
            'まだ、その段階？',
            'よせ、過去の事は聞くな。',
            'あれ…え？　ジョニー・デップに激似でも割引ってされないんだ。'
            ]))
    # 自分へのメンションでなければスルー
    elif not HIKEPO_ID in mentions_id:
        pass
    # terraria サーバー起動
    elif 'terraria' in message.content:
        await message.channel.send('terraria サーバーを起動するめう')
        response = urllib.request.urlopen('https://asia-northeast1-terraria-280314.cloudfunctions.net/startInstance')
        if response.getcode() != 200:
            await message.channnel.send('HTTP status code: ' + resopnse.getcode())
            return
        await message.channel.send(
            'terraria サーバーが立ち上がっためう！\n'
            + '\n'
            + response.read().decode('utf-8')
            + '\n'
            + 'terraria を起動して Multiplayer --> Join via IP でワールドに入れるめうね'
            )
    # オリジナルからのリプライは塩対応
    elif message.author.id == HIKESHI_ID:
        await message.channel.send(
            message.author.mention + ' '
            + random.choice([
            'ちょっと何言ってるかわかんないっすね',
            'せやろか',
            'ホンマか？',
            'そうはならんやろ'
            ]))
    # 創造主に対しては反抗
    elif message.author.id == NUPAN_ID:
        await message.channel.send(
            message.author.mention + ' '
            + random.choice([
            '神は死んだ',
            'お前は創造主ではない',
            'かかってこいよ。怖いのか？'
            ]))
    # 生存確認用
    else:
        await message.channel.send(
            message.author.mention + ' '
            + random.choice([
            'わかる',
            'それな',
            'そりｗ',
            'なるほど',
            'すごいな',
            '悪いのは君じゃない',
            ]))

# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------

if __name__=='__main__':
    client.run(BOT_ACCESS_TOKEN)

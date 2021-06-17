import discord
import os
import urllib.request

client = discord.Client()
# TODO token is getting from enviroment
token = "Input your discord token"

# TODO endpoint and url is getting from enviroment
stop_url = "https://xxxxxxxxxxxxxxxxx/xxxxxxxx"
start_url = "https://xxxxxxxxxxxxxx/xxxxxxxx"

@client.event
async def on_ready():
    print("Log in")

@client.event
async def on_message(message):
    if client.user != message.author:
        if message.content == "$MsServerStart":
            result = server_start(message)
            await message.channel.send(result)
        if message.content == "$MsServerStop":
            result = server_stop(message)
            await message.channel.send(result)
        if message.content == "$ifconfig":
            result = get_public_ip(message)
            await message.channel.send(result)


def server_start(message):
    # APIGatewayを呼び出す
    # TODO api-key is getting from enviroment
    headers = {
        "x-api-key": "xxxxxxxxxxxxxxxxxxxxxx"
    }
    req = urllib.request.Request(start_url,headers=headers)
    # response check
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
        desciption = message.author.name + "さんがサーバーを開始しました。\nサーバーがアクティブになったらIPアドレスが投稿されます。\nちょっとまってね。\n全然表示されない場合は[$ifconfig]を実行してね。"
        return desciption
    except urllib.error.HTTPError as e:
        if e.code >= 400:
            desciption = e.reason
        else: desciption = "何らかのエラーが発生しました。"
        return desciption

def server_stop(message):
    # APIGatewayを呼び出す
    # TODO api key is getting from enviroment
    headers = {
        "x-api-key": "xsxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
    # response check
    req = urllib.request.Request(stop_url,headers=headers)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    desciption = message.author.name + "さんがサーバーを停止しました。"
    return desciption

def get_public_ip(message):
    return "develop"

client.run(token)

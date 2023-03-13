#Server Invite URL
#https://discord.com/api/oauth2/authorize?client_id=1071265737022382150&permissions=8&scope=bot
import os
import discord
import discord.app_commands
import requests
import json
try:
	from discordtoken import token
except ImportError:
	token = os.getenv('DISCORD_TOKEN_NEKOGLOBALCHAT')  #Your TOKEN
from server import keep_alive

global_channel_name = "neko-global-chat"  #設定したいチャンネル名を入力
intents=discord.Intents.default()

client = discord.Client(intents=intents)  #接続に必要なオブジェクトを生成
tree = discord.app_commands.CommandTree(client)  #←ココ

@tree.command(
	name="nowstage3_regular",  #コマンド名
	description="Splatoon3の現在のナワバリバトルの情報を取得します。"  #コマンドの説明
)
async def nowstage3_regular(ctx: discord.Interaction):
	response = requests.get("https://spla3.yuu26.com/api/regular/now")
	json_response = json.loads(response.text)
	stage1 = json_response['results'][0]['stages'][0]
	stage2 = json_response['results'][0]['stages'][1]
	is_fest = json_response['results'][0]['is_fest']
	embed=discord.Embed(title="ナワバリバトル ステージ情報", description="is_fest:{}".format(is_fest), color=0x9B95C9)
	embed2=discord.Embed(title="ステージ①", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed2.add_field(name=stage1['name'], value="Stage id:{}".format(stage1['id']))
	embed2.set_image(url=stage1['image'])
	embed3=discord.Embed(title="ステージ②", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed3.add_field(name=stage2['name'], value="Stage id:{}".format(stage1['id']))
	embed3.set_image(url=stage2['image'])
	await ctx.response.send_message(embeds=[embed, embed2, embed3]) #メッセージを送信

@tree.command(
	name="nowstage3_anarchy_challenge",  #コマンド名
	description="Splatoon3の現在のバンカラマッチ(チャレンジ)の情報を取得します。"  #コマンドの説明
)
async def nowstage3_anarchy_challenge(ctx: discord.Interaction):
	response = requests.get("https://spla3.yuu26.com/api/bankara-challenge/now")
	json_response = json.loads(response.text)
	stage1 = json_response['results'][0]['stages'][0]
	stage2 = json_response['results'][0]['stages'][1]
	is_fest = json_response['results'][0]['is_fest']
	rule = json_response['results'][0]['rule']['name']
	embed=discord.Embed(title="バンカラマッチ(チャレンジ) ステージ情報", description="ルール:{}\nis_fest:{}".format(rule,is_fest), color=0x9B95C9)
	embed2=discord.Embed(title="ステージ①", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed2.add_field(name=stage1['name'], value="Stage id:{}".format(stage1['id']))
	embed2.set_image(url=stage1['image'])
	embed3=discord.Embed(title="ステージ②", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed3.add_field(name=stage2['name'], value="Stage id:{}".format(stage1['id']))
	embed3.set_image(url=stage2['image'])
	await ctx.response.send_message(embeds=[embed, embed2, embed3]) #メッセージを送信

@tree.command(
	name="nowstage3_anarchy_open",  #コマンド名
	description="Splatoon3の現在のバンカラマッチ(オープン)の情報を取得します。"  #コマンドの説明
)
async def nowstage3_anarchy_open(ctx: discord.Interaction):
	response = requests.get("https://spla3.yuu26.com/api/bankara-open/now")
	json_response = json.loads(response.text)
	stage1 = json_response['results'][0]['stages'][0]
	stage2 = json_response['results'][0]['stages'][1]
	is_fest = json_response['results'][0]['is_fest']
	rule = json_response['results'][0]['rule']['name']
	embed=discord.Embed(title="バンカラマッチ(オープン) ステージ情報", description="ルール:{}\nis_fest:{}".format(rule,is_fest), color=0x9B95C9)
	embed2=discord.Embed(title="ステージ①", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed2.add_field(name=stage1['name'], value="Stage id:{}".format(stage1['id']))
	embed2.set_image(url=stage1['image'])
	embed3=discord.Embed(title="ステージ②", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed3.add_field(name=stage2['name'], value="Stage id:{}".format(stage1['id']))
	embed3.set_image(url=stage2['image'])
	await ctx.response.send_message(embeds=[embed, embed2, embed3]) #メッセージを送信

@tree.command(
	name="nowstage3_x",  #コマンド名
	description="Splatoon3の現在のXマッチの情報を取得します。"  #コマンドの説明
)
async def nowstage3_x(ctx: discord.Interaction):
	response = requests.get("https://spla3.yuu26.com/api/x/now")
	json_response = json.loads(response.text)
	stage1 = json_response['results'][0]['stages'][0]
	stage2 = json_response['results'][0]['stages'][1]
	is_fest = json_response['results'][0]['is_fest']
	rule = json_response['results'][0]['rule']['name']
	embed=discord.Embed(title="Xマッチ ステージ情報", description="ルール:{}\nis_fest:{}".format(rule,is_fest), color=0x9B95C9)
	embed2=discord.Embed(title="ステージ①", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed2.add_field(name=stage1['name'], value="Stage id:{}".format(stage1['id']))
	embed2.set_image(url=stage1['image'])
	embed3=discord.Embed(title="ステージ②", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed3.add_field(name=stage2['name'], value="Stage id:{}".format(stage1['id']))
	embed3.set_image(url=stage2['image'])
	await ctx.response.send_message(embeds=[embed, embed2, embed3]) #メッセージを送信

@tree.command(
	name="salmon_run_indeed3",  #コマンド名
	description="Splatoon3の現在のサーモンランのバイト情報を取得します。"  #コマンドの説明
)
async def salmon_run_indeed3(ctx: discord.Interaction):
	response = requests.get("https://spla3.yuu26.com/api/coop-grouping/now")
	json_response = json.loads(response.text)
	stage = json_response['results'][0]['stage']
	weapons = json_response['results'][0]['weapons']
	is_big_run = json_response['results'][0]['is_big_run']
	embed=discord.Embed(title="サーモンラン バイト情報", description="is_big_run:{}".format(is_big_run), color=0x9B95C9)
	embed2=discord.Embed(title="ステージ", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed2.add_field(name=stage['name'], value="Stage id:{}".format(stage['id']))
	embed2.set_image(url=stage['image'])
	embed3=discord.Embed(title="ブキ①", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed3.add_field(name=weapons[0]['name'], value="")
	embed3.set_image(url=weapons[0]['image'])
	embed4=discord.Embed(title="ブキ②", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed4.add_field(name=weapons[1]['name'], value="")
	embed4.set_image(url=weapons[1]['image'])
	embed5=discord.Embed(title="ブキ③", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed5.add_field(name=weapons[2]['name'], value="")
	embed5.set_image(url=weapons[2]['image'])
	embed6=discord.Embed(title="ブキ④", color=0x9B95C9) #埋め込みの説明に、メッセージを挿入し、埋め込みのカラーを紫`#9B95C9`に設定
	embed6.add_field(name=weapons[3]['name'], value="")
	embed6.set_image(url=weapons[3]['image'])
	await ctx.response.send_message(embeds=[embed, embed2, embed3, embed4, embed5, embed6]) #メッセージを送信

@client.event
async def on_ready():
	await tree.sync()

keep_alive()
client.run(token)
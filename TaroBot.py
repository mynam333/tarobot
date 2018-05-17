import asyncio
import discord
from discord.ext import commands
import random

client = discord.Client()

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "NDQ2MjcwNTk4NTE2MzEwMDE3.Dd2mxw.G1OvwFgktdxKuQut24P-2P-lGJs"

logging.basicConfig(level=logging.INFO)
client = discord.Client()
mysql_username = "mynam333"
mysql_password = "mt83891595"
mysql_hostname = "db_inventory"
mysql_db_name = "inventory"
discord_pass = None

# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(client.user.name)
    print(client.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="!타로", type=1))

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!타로'):
        messages = ["The Fool (광대, 바보) 정방향. 『모험, 무지(無知)』", "The Fool (광대, 바보) 역방향. 『경솔, 어리석음』", "The Magician (마술사, 마법사, 기술사) 정방향. 『창조, 수완』", "The Magician (마술사, 마법사, 기술사) 역방향. 『겁많음, 기만』", "The High Priestess (여교황) 정방향. 『지식, 총명』", "The High Priestess (여교황) 역방향. 『잔혹, 무례함』", "The Empress (여제, 여황제) 정방향. 『풍양, 모성』", "The Empress (여제, 여황제) 역방향. 『과잉, 허영』", "The Emperor (황제) 정방향. 『책임, 부성(父性)』", "The Emperor (황제) 역방향. 『오만, 존대』", "The Hierophant (교황) 정방향. 『가르침, 관대함』", "The Hierophant (교황) 역방향. 『협량, 나태』", "The Lovers (연인, 연애) 정방향. 『연애, 쾌락』", "The Lovers (연인, 연애) 역방향. 『질투, 배신』", "The Chariot (전차, 정복자) 정방향. 『전진, 승리』", "The Chariot (전차, 정복자) 역방향. 『폭주, 좌절』", "Strength (힘) 정방향. 『힘, 용기』", "Strength (힘) 역방향. 『본성, 자만』", "The Hermit (은둔자) 정방향. 『탐색, 사려깊음』", "The Hermit (은둔자) 역방향. 『음습, 폐쇄적, 탐욕』", "Wheel of Fortune (운명의 수레바퀴, 운명) 정방향. 『기회, 일시적인 행운』", "Wheel of Fortune (운명의 수레바퀴, 운명) 역방향. 『오산, 불운』", "Justice (정의, 재판의 여신) 정방향. 『균형, 정당함』", "Justice (정의, 재판의 여신) 역방향. 『편견, 부정』", "The Hanged Man (매달린 사람, 매달린 남자) 정방향. 『자기희생, 인내』", "The Hanged Man (매달린 사람, 매달린 남자) 역방향. 『무의미한 희생, 맹목』", "Death (죽음, 사신) 정방향. 『격변, 이별』", "Death (죽음, 사신) 역방향. 『변화의 유보, 고착』", "Temperance (절제) 정방향. 『조화, 견실』", "Temperance (절제) 역방향. 『낭비, 불안정』", "The Devil (악마) 정방향. 『사심, 속박, 타락』", "The Devil (악마) 역방향. 『악순환으로부터의 각성』", "The Tower (탑, 신의 집) 정방향. 『파괴, 파멸』", "The Tower (탑, 신의 집) 역방향. 『필요로 하는 파괴』", "The Star (별) 정방향. 『희망, 동경』", "The Star (별) 역방향. 『환멸, 비애』", "The Moon (달) 정방향. 『불안, 애매함, 혼돈』", "The Moon (달) 역방향. 『불안 해소, 명료함, 혼돈의 끝』", "The Sun (태양) 정방향. 『밝은 미래, 만족』", "The Sun (태양) 역방향. 『연기(延期), 실패』", "Judgement (심판, 영겁) 정방향. 『부활, 개선』", "Judgement (심판, 영겁) 역방향. 『재기불능, 후회』", "The World (세계, 우주) 정방향. 『완성, 완전』", "The World (세계, 우주) 역방향. 『미완성, 어중간함』"]
        await client.send_message(message.channel, "<@"+id+">님의 오늘의 운세입니다.")
        await client.send_message(message.channel, random.choice(messages))
        

client.run(token)

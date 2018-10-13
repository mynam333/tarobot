#!/usr/local/bin/python
# coding:utf-8

import asyncio
import discord
import random
import subprocess

client = discord.Client()

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "NDQ2MjcwNTk4NTE2MzEwMDE3.Dd2mxw.G1OvwFgktdxKuQut24P-2P-lGJs"

# 봇이 구동되었을 때 동작되는 코드입니다.
@client.event
async def on_ready():
    print("Logged in as ") #화면에 봇의 아이디, 닉네임이 출력됩니다.
    print((client.user.name))
    print((client.user.id))
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    await client.change_presence(game=discord.Game(name="!목록", type=1))

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.
    
    
    if message.content.startswith('!타로'):
       messages = ["The Fool (광대, 바보) 정방향. 『모험, 무지(無知)』", "The Fool (광대, 바보) 역방향. 『경솔, 어리석음』", "The Magician (마술사, 마법사, 기술사) 정방향. 『창조, 수완』", "The Magician (마술사, 마법사, 기술사) 역방향. 『겁많음, 기만』", "The High Priestess (여교황) 정방향. 『지식, 총명』", "The High Priestess (여교황) 역방향. 『잔혹, 무례함』", "The Empress (여제, 여황제) 정방향. 『풍양, 모성』", "The Empress (여제, 여황제) 역방향. 『과잉, 허영』", "The Emperor (황제) 정방향. 『책임, 부성(父性)』", "The Emperor (황제) 역방향. 『오만, 존대』", "The Hierophant (교황) 정방향. 『가르침, 관대함』", "The Hierophant (교황) 역방향. 『협량, 나태』", "The Lovers (연인, 연애) 정방향. 『연애, 쾌락』", "The Lovers (연인, 연애) 역방향. 『질투, 배신』", "The Chariot (전차, 정복자) 정방향. 『전진, 승리』", "The Chariot (전차, 정복자) 역방향. 『폭주, 좌절』", "Strength (힘) 정방향. 『힘, 용기』", "Strength (힘) 역방향. 『본성, 자만』", "The Hermit (은둔자) 정방향. 『탐색, 사려깊음』", "The Hermit (은둔자) 역방향. 『음습, 폐쇄적, 탐욕』", "Wheel of Fortune (운명의 수레바퀴, 운명) 정방향. 『기회, 일시적인 행운』", "Wheel of Fortune (운명의 수레바퀴, 운명) 역방향. 『오산, 불운』", "Justice (정의, 재판의 여신) 정방향. 『균형, 정당함』", "Justice (정의, 재판의 여신) 역방향. 『편견, 부정』", "The Hanged Man (매달린 사람, 매달린 남자) 정방향. 『자기희생, 인내』", "The Hanged Man (매달린 사람, 매달린 남자) 역방향. 『무의미한 희생, 맹목』", "Death (죽음, 사신) 정방향. 『격변, 이별』", "Death (죽음, 사신) 역방향. 『변화의 유보, 고착』", "Temperance (절제) 정방향. 『조화, 견실』", "Temperance (절제) 역방향. 『낭비, 불안정』", "The Devil (악마) 정방향. 『사심, 속박, 타락』", "The Devil (악마) 역방향. 『악순환으로부터의 각성』", "The Tower (탑, 신의 집) 정방향. 『파괴, 파멸』", "The Tower (탑, 신의 집) 역방향. 『필요로 하는 파괴』", "The Star (별) 정방향. 『희망, 동경』", "The Star (별) 역방향. 『환멸, 비애』", "The Moon (달) 정방향. 『불안, 애매함, 혼돈』", "The Moon (달) 역방향. 『불안 해소, 명료함, 혼돈의 끝』", "The Sun (태양) 정방향. 『밝은 미래, 만족』", "The Sun (태양) 역방향. 『연기(延期), 실패』", "Judgement (심판, 영겁) 정방향. 『부활, 개선』", "Judgement (심판, 영겁) 역방향. 『재기불능, 후회』", "The World (세계, 우주) 정방향. 『완성, 완전』", "The World (세계, 우주) 역방향. 『미완성, 어중간함』"]
       await client.send_message(message.channel, "<@"+id+">님의 오늘의 운세입니다.")
       await client.send_message(message.channel, random.choice(messages))

        


    elif message.content.startswith('!점괘'):
         messages = ["대길(大吉). 오늘 당신의 앞날에는 행운이 가득할겁니다.","길(吉). 오늘 당신에게 좋은 일이 계속 생길 것 같네요.","중길(中吉). 오늘 당신의 앞날은 창창합니다.","소길(小吉). 오늘은 작은 행운이 당신을 지켜줄듯 합니다..","반길(半吉). 오늘 작은 행운조각이 당신을 따라다닐것 같습니다.","말길(末吉). 오늘 행운의 끝자락이 당신에게 닿았습니다.","말소길(末小吉). 오늘 행운의 끝자락이 당신을 스쳐지나갑니다.","평(平). 오늘은 평범한 하루입니다. 행운과 불행이 당신을 덮치는군요.","흉(凶). 좋지 않습니다. 오늘 당신에게 무언가 좋지 않은 일 조금 생길지도 모르겠네요.","소흉(小凶). 오늘은 무언가 되지 않는 날이네요. 작은 실수들이 당신을 괴롭힙니다.","반흉(半凶). 오늘 작은 불행이 당신을 따라다닐것입니다.","말흉(末凶). 오늘 큰 불행이 당신을 따라다니며 괴롭힐 것입니다.","대흉(大凶). 펌블! 끔찍하군요. 오늘 당신의 하루는 최악으로 예견됩니다."]
         await client.send_message(message.channel, "<@"+id+">님의 오늘의 점괘입니다.")
         await client.send_message(message.channel, random.choice(messages))

            


    elif message.content.startswith('!목록'):
         embed=discord.Embed(title="운세봇 명령어 목록입니다.", description="!타로 (오늘의 운세를 타로카드로 알아봅니다.)\n!점괘 (오늘의 운세를 오미쿠지로 알아봅니다.)\n사용가능한 거미콘은 ';목록1'~';목록4' 으로 확인가능합니다.\n사용가능한 냥장콘은 '#목록1'~'#목록4' 으로 확인가능합니다.", color=0x0000ff)
         embed.set_footer(text="Made by ")
         await client.send_message(message.channel, embed=embed)
    
    # 이하 테스트용
    
    
    
    
    
    # 이하 디시거미콘

    
    
    elif message.content.startswith(';야호'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [야호]하셨습니다.")
         em.set_image(url="https://i.imgur.com/xXk8nVo.gif")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith(';삐짐'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [삐짐]하셨습니다.")
         em.set_image(url="https://i.imgur.com/64vOuO4.png")
         await client.send_message(message.channel, embed=em)
            
            
    elif message.content.startswith(';풋'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [풋]하셨습니다.")
         em.set_image(url="https://i.imgur.com/kQxjrQo.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';훗'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [훗]하셨습니다.")
         em.set_image(url="https://i.imgur.com/kQxjrQo.png")
         await client.send_message(message.channel, embed=em)
            
                        
    elif message.content.startswith(';디제잉'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [디제잉]하셨습니다.")
         em.set_image(url="https://i.imgur.com/QX50q2M.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';좌절'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [좌절]하셨습니다.")
         em.set_image(url="https://i.imgur.com/zzjWOiL.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';빡종'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [빡종]하셨습니다.")
         em.set_image(url="https://i.imgur.com/cEoTjwN.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';데헷'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [데헷]하셨습니다.")
         em.set_image(url="https://i.imgur.com/SWks24n.gif")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';유령'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [유령]하셨습니다.")
         em.set_image(url="https://i.imgur.com/Zacahw7.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';이불'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [이불]하셨습니다.")
         em.set_image(url="https://i.imgur.com/e8ziPto.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';우마루'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [우마루]하셨습니다.")
         em.set_image(url="https://i.imgur.com/Sxm55U6.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';경례'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [경례]하셨습니다.")
         em.set_image(url="https://i.imgur.com/lyrRk10.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';힐끔'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [힐끔]하셨습니다.")
         em.set_image(url="https://i.imgur.com/tUYvhqz.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';선글라스'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [선글라스]하셨습니다.")
         em.set_image(url="https://i.imgur.com/u9XNV2M.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';커피'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [커피]하셨습니다.")
         em.set_image(url="https://i.imgur.com/5JCZONu.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';히익'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [히익]하셨습니다.")
         em.set_image(url="https://i.imgur.com/FtRx5x3.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';메롱'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [메롱]하셨습니다.")
         em.set_image(url="https://i.imgur.com/G92wTAI.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';밥상'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [밥상]하셨습니다.")
         em.set_image(url="https://i.imgur.com/AdrQFFi.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';총'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [총]하셨습니다.")
         em.set_image(url="https://i.imgur.com/Qkc1h5B.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';고인'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [고인]하셨습니다.")
         em.set_image(url="https://i.imgur.com/wxLreLP.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';사형'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [사형]하셨습니다.")
         em.set_image(url="https://i.imgur.com/2nryb2B.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';칭찬'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [칭찬]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ZIJBzn3.png")
         await client.send_message(message.channel, embed=em)
            
            
    elif message.content.startswith(';레알?'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [레알?]하셨습니다.")
         em.set_image(url="https://i.imgur.com/0JzK9VP.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㄹㅇ?'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㄹㅇ?]하셨습니다.")
         em.set_image(url="https://i.imgur.com/0JzK9VP.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';갑분싸'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [갑분싸]하셨습니다.")
         em.set_image(url="https://i.imgur.com/L4JtAWo.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';충성'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [충성]하셨습니다.")
         em.set_image(url="https://i.imgur.com/2Ev5w2f.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';울먹'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [울먹]하셨습니다.")
         em.set_image(url="https://i.imgur.com/AQmIzxk.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';부끄'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [부끄]하셨습니다.")
         em.set_image(url="https://i.imgur.com/s7SaOnG.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';오와콘'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [오와콘]하셨습니다.")
         em.set_image(url="https://i.imgur.com/MBlLJ8v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';눈물'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [눈물]하셨습니다.")
         em.set_image(url="https://i.imgur.com/EgRU44E.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';스고이'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [스고이]하셨습니다.")
         em.set_image(url="https://i.imgur.com/TOG8qKf.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';쾅쾅'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [쾅쾅]하셨습니다.")
         em.set_image(url="https://i.imgur.com/YbAFnyb.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';빼액'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [빼액]하셨습니다.")
         em.set_image(url="https://i.imgur.com/2EBwi9n.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';팍씨'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [팍씨]하셨습니다.")
         em.set_image(url="https://i.imgur.com/1lB6Nrc.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';드르렁'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [드르렁]하셨습니다.")
         em.set_image(url="https://i.imgur.com/6eyIFsR.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';눈빔'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [눈빔]하셨습니다.")
         em.set_image(url="https://i.imgur.com/0F2CEaK.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';?'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [?]하셨습니다.")
         em.set_image(url="https://i.imgur.com/MmKffzi.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';뒤적'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [뒤적]하셨습니다.")
         em.set_image(url="https://i.imgur.com/zaoyKEq.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';좆까'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [좆까]하셨습니다.")
         em.set_image(url="https://i.imgur.com/jt7EdcH.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';혼란'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [혼란]하셨습니다.")
         em.set_image(url="https://i.imgur.com/Z8KDEWA.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';대신'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [대신]하셨습니다.")
         em.set_image(url="https://i.imgur.com/e0I15eD.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';엠창인생'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [엠창인생]하셨습니다.")
         em.set_image(url="https://i.imgur.com/sfrk72H.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';메가폰'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [메가폰]하셨습니다.")
         em.set_image(url="https://i.imgur.com/K89E9wt.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';그만'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [그만]하셨습니다.")
         em.set_image(url="https://i.imgur.com/rWpC8Hw.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';저기요'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [저기요]하셨습니다.")
         em.set_image(url="https://i.imgur.com/L5cX93M.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';띠용'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [띠용]하셨습니다.")
         em.set_image(url="https://i.imgur.com/cGjjiAq.png")
         await client.send_message(message.channel, embed=em)
            
            
    elif message.content.startswith(';병신'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [병신]하셨습니다.")
         em.set_image(url="https://i.imgur.com/fgqAk3q.png")
         await client.send_message(message.channel, embed=em)
        
                                   
    elif message.content.startswith(';븅신'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [븅신]하셨습니다.")
         em.set_image(url="https://i.imgur.com/fgqAk3q.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';별로'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [별로]하셨습니다.")
         em.set_image(url="https://i.imgur.com/0BoQgnF.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';안녕'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [안녕]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ylUgE7v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';안뇽'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [안뇽]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ylUgE7v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';하이'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [하이]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ylUgE7v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅎㅇ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅎㅇ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ylUgE7v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';한숨'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [한숨]하셨습니다.")
         em.set_image(url="https://i.imgur.com/fZ6JRhl.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';에휴'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [에휴]하셨습니다.")
         em.set_image(url="https://i.imgur.com/fZ6JRhl.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';친구비'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [친구비]하셨습니다.")
         em.set_image(url="https://i.imgur.com/SBRB8Lq.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';발그레'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [발그레]하셨습니다.")
         em.set_image(url="https://i.imgur.com/KzLeTh9.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';자살'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [자살]하셨습니다.")
         em.set_image(url="https://i.imgur.com/BBnFGvh.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';훌쩍'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [훌쩍]하셨습니다.")
         em.set_image(url="https://i.imgur.com/YZkpqLa.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';쿠궁'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [쿠궁]하셨습니다.")
         em.set_image(url="https://i.imgur.com/BoHgLR7.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';꽁꽁'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [꽁꽁]하셨습니다.")
         em.set_image(url="https://i.imgur.com/xcpgEDG.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';덜덜'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [덜덜]하셨습니다.")
         em.set_image(url="https://i.imgur.com/v8nrAUE.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㄷㄷ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㄷㄷ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/v8nrAUE.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';엄근진'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [엄근진]하셨습니다.")
         em.set_image(url="https://i.imgur.com/B5uAHMs.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';쏘우'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [쏘우]하셨습니다.")
         em.set_image(url="https://i.imgur.com/EsYap0a.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';웃음'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [웃음]하셨습니다.")
         em.set_image(url="https://i.imgur.com/6oF3nQ8.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅎㅎ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅎㅎ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/6oF3nQ8.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅋㅋ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅋㅋ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/6oF3nQ8.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';키야'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [키야]하셨습니다.")
         em.set_image(url="https://i.imgur.com/HPh6DXV.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';캬'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [캬]하셨습니다.")
         em.set_image(url="https://i.imgur.com/HPh6DXV.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';어쩔'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [어쩔]하셨습니다.")
         em.set_image(url="https://i.imgur.com/CkyVCOB.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';쯧쯧'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [쯧쯧]하셨습니다.")
         em.set_image(url="https://i.imgur.com/wQr1DUJ.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅉㅉ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅉㅉ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/wQr1DUJ.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';죽창'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [죽창]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ryqKjC1.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅂㄷ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅂㄷ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ryqKjC1.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';절레'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [절레]하셨습니다.")
         em.set_image(url="https://i.imgur.com/kTDKg5t.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';와'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [와]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8dWrgS6.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';우와'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [우와]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8dWrgS6.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';오아'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [오아]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8dWrgS6.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';억울'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [억울]하셨습니다.")
         em.set_image(url="https://i.imgur.com/DMYyapG.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';히익'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [히익]하셨습니다.")
         em.set_image(url="https://i.imgur.com/UlUikVd.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';흥칫뿡'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [흥칫뿡]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ibHZkpl.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅗ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅗ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/CQtldqK.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';엿'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [엿]하셨습니다.")
         em.set_image(url="https://i.imgur.com/CQtldqK.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';죽일까'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [죽일까]하셨습니다.")
         em.set_image(url="https://i.imgur.com/Q6tPMm2.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';아몰랑'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [아몰랑]하셨습니다.")
         em.set_image(url="https://i.imgur.com/G4jcNDk.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅍㅅㅍ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅍㅅㅍ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/7S539cB.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';비웃음'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [비웃음]하셨습니다.")
         em.set_image(url="https://i.imgur.com/3dhqyVq.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';피식'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [피식]하셨습니다.")
         em.set_image(url="https://i.imgur.com/3dhqyVq.png")
         await client.send_message(message.channel, embed=em)
            
            
    elif message.content.startswith(';빡침'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [빡침]하셨습니다.")
         em.set_image(url="https://i.imgur.com/5HCppyD.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';지랄'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [지랄]하셨습니다.")
         em.set_image(url="https://i.imgur.com/A7HG6Sf.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅈㄹ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅈㄹ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/A7HG6Sf.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';레알'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [레알]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8CmRp3H.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㄹㅇ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㄹㅇ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8CmRp3H.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';빼액'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [빼액]하셨습니다.")
         em.set_image(url="https://i.imgur.com/wi6UwCn.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';!?'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [?!]하셨습니다.")
         em.set_image(url="https://i.imgur.com/dvH1YFY.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';팝콘'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [팝콘]하셨습니다.")
         em.set_image(url="https://i.imgur.com/XwVApTH.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';팝그작'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [팝그작]하셨습니다.")
         em.set_image(url="https://i.imgur.com/XwVApTH.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';박수'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [박수]하셨습니다.")
         em.set_image(url="https://i.imgur.com/SG7T8bg.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';짝짝'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [짝짝]하셨습니다.")
         em.set_image(url="https://i.imgur.com/SG7T8bg.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';따봉'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [따봉]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8Jmtmwc.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';최고'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [최고]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8Jmtmwc.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';굿'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [굿]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8Jmtmwc.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';얍'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [얍]하셨습니다.")
         em.set_image(url="https://i.imgur.com/7ekHsen.png")
         await client.send_message(message.channel, embed=em)
            
            
    elif message.content.startswith(';설레여라얍'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [설레여라얍]하셨습니다.")
         em.set_image(url="https://i.imgur.com/bzUQfDX.gif")
         await client.send_message(message.channel, embed=em)
            
            
         
         
        
    elif message.content.startswith(';목록1'):
         embed=discord.Embed(title="`★거미콘 명령어 목록 [1/4] 페이지입니다.`", color=0xffff00)
         embed.add_field(name=";야호", value="https://i.imgur.com/xXk8nVo.gif")
         embed.add_field(name=";삐짐", value="https://i.imgur.com/64vOuO4.png")
         embed.add_field(name=";풋, ;훗", value="https://i.imgur.com/kQxjrQo.png")
         embed.add_field(name=";디제잉", value="https://i.imgur.com/QX50q2M.gif")
         embed.add_field(name=";좌절", value="https://i.imgur.com/zzjWOiL.png")
         embed.add_field(name=";빡종", value="https://i.imgur.com/cEoTjwN.png")
         embed.add_field(name=";데헷", value="https://i.imgur.com/SWks24n.gif")
         embed.add_field(name=";유령", value="https://i.imgur.com/Zacahw7.png")
         embed.add_field(name=";이불", value="https://i.imgur.com/e8ziPto.png")
         embed.add_field(name=";우마루", value="https://i.imgur.com/Sxm55U6.gif")
         embed.add_field(name=";경례", value="https://i.imgur.com/lyrRk10.png")
         embed.add_field(name=";힐끔", value="https://i.imgur.com/tUYvhqz.gif")
         embed.add_field(name=";선글라스", value="https://i.imgur.com/u9XNV2M.gif")
         embed.add_field(name=";커피", value="https://i.imgur.com/5JCZONu.png")
         embed.add_field(name=";히익", value="https://i.imgur.com/FtRx5x3.png")
         embed.add_field(name=";메롱", value="https://i.imgur.com/G92wTAI.gif")
         embed.add_field(name=";밥상", value="https://i.imgur.com/AdrQFFi.png")
         embed.add_field(name=";총", value="https://i.imgur.com/Qkc1h5B.gif")
         embed.add_field(name=";고인", value="https://i.imgur.com/wxLreLP.gif")
         embed.add_field(name=";사형", value="https://i.imgur.com/2nryb2B.png")
         embed.add_field(name=";칭찬", value="https://i.imgur.com/ZIJBzn3.png")
         embed.add_field(name=";레알?, ;ㄹㅇ?", value="https://i.imgur.com/0JzK9VP.png")
         embed.add_field(name=";갑분싸", value="https://i.imgur.com/L4JtAWo.png")
         embed.add_field(name=";충성", value="https://i.imgur.com/2Ev5w2f.png")
         embed.add_field(name=";울먹", value="https://i.imgur.com/AQmIzxk.png")
         embed.add_field(name=";부끄", value="https://i.imgur.com/s7SaOnG.png")
         embed.add_field(name=";오와콘", value="https://i.imgur.com/MBlLJ8v.png")
         embed.set_footer(text="Made by 여우혼")
         await client.send_message(message.channel, embed=embed)
        
        
    elif message.content.startswith(';목록2'):
         embed=discord.Embed(title="`★거미콘 명령어 목록 [2/4] 페이지입니다.`", color=0xffff00)
         embed.add_field(name=";눈물", value="https://i.imgur.com/EgRU44E.png")            
         embed.add_field(name=";부끄", value="https://i.imgur.com/s7SaOnG.png")
         embed.add_field(name=";오와콘", value="https://i.imgur.com/MBlLJ8v.png")
         embed.add_field(name=";눈물", value="https://i.imgur.com/EgRU44E.png")
         embed.add_field(name=";스고이", value="https://i.imgur.com/TOG8qKf.png")
         embed.add_field(name=";쾅쾅", value="https://i.imgur.com/YbAFnyb.png")
         embed.add_field(name=";빼액", value="https://i.imgur.com/2EBwi9n.png")
         embed.add_field(name=";팍씨", value="https://i.imgur.com/1lB6Nrc.png")
         embed.add_field(name=";드르렁", value="https://i.imgur.com/6eyIFsR.png")
         embed.add_field(name=";눈빔", value="https://i.imgur.com/0F2CEaK.png")
         embed.add_field(name=";?", value="https://i.imgur.com/MmKffzi.png")
         embed.add_field(name=";뒤적", value="https://i.imgur.com/zaoyKEq.png")
         embed.add_field(name=";좆까", value="https://i.imgur.com/jt7EdcH.png")
         embed.add_field(name=";혼란", value="https://i.imgur.com/Z8KDEWA.png")
         embed.add_field(name=";대신", value="https://i.imgur.com/e0I15eD.png")
         embed.add_field(name=";엠창인생", value="https://i.imgur.com/sfrk72H.png")
         embed.add_field(name=";메가폰", value="https://i.imgur.com/K89E9wt.png")
         embed.add_field(name=";그만", value="https://i.imgur.com/rWpC8Hw.png")
         embed.add_field(name=";저기요", value="https://i.imgur.com/L5cX93M.png")
         embed.add_field(name=";띠용", value="https://i.imgur.com/cGjjiAq.png")
         embed.add_field(name=";병신, ;븅신", value="https://i.imgur.com/fgqAk3q.png")
         embed.add_field(name=";별로", value="https://i.imgur.com/0BoQgnF.png")
         embed.add_field(name=";안녕, ;안뇽, ;하이, ;ㅎㅇ", value="https://i.imgur.com/ylUgE7v.png")
         embed.add_field(name=";한숨, ;에휴", value="https://i.imgur.com/fZ6JRhl.png")
         embed.add_field(name=";친구비", value="https://i.imgur.com/SBRB8Lq.png")
         embed.add_field(name=";발그레", value="https://i.imgur.com/KzLeTh9.png")
         embed.add_field(name=";자살", value="https://i.imgur.com/BBnFGvh.png")
         embed.add_field(name=";훌쩍", value="https://i.imgur.com/YZkpqLa.png")
         embed.add_field(name=";쿠궁", value="https://i.imgur.com/BoHgLR7.png")
         embed.add_field(name=";꽁꽁", value="https://i.imgur.com/xcpgEDG.png")
         embed.set_footer(text="Made by 여우혼")
         await client.send_message(message.channel, embed=embed)
        
        
    elif message.content.startswith(';목록3'):
         embed=discord.Embed(title="`★거미콘 명령어 목록 [3/4] 페이지입니다.`", color=0xffff00)
         embed.add_field(name=";덜덜, ;ㄷㄷ", value="https://i.imgur.com/v8nrAUE.png")
         embed.add_field(name=";엄근진", value="https://i.imgur.com/B5uAHMs.png") 
         embed.add_field(name=";자살", value="https://i.imgur.com/BBnFGvh.png")
         embed.add_field(name=";훌쩍", value="https://i.imgur.com/YZkpqLa.png")
         embed.add_field(name=";쿠궁", value="https://i.imgur.com/BoHgLR7.png")
         embed.add_field(name=";꽁꽁", value="https://i.imgur.com/xcpgEDG.png")
         embed.add_field(name=";덜덜, ;ㄷㄷ", value="https://i.imgur.com/v8nrAUE.png")
         embed.add_field(name=";엄근진", value="https://i.imgur.com/B5uAHMs.png")
         embed.add_field(name=";쏘우", value="https://i.imgur.com/EsYap0a.png")
         embed.add_field(name=";웃음, ;ㅎㅎ, ;ㅋㅋ", value="https://i.imgur.com/6oF3nQ8.png")
         embed.add_field(name=";키야, ;캬", value="https://i.imgur.com/HPh6DXV.png")
         embed.add_field(name=";어쩔", value="https://i.imgur.com/CkyVCOB.png")
         embed.add_field(name=";쯧쯧, ;ㅉㅉ", value="https://i.imgur.com/wQr1DUJ.png")
         embed.add_field(name=";죽창, ;ㅂㄷ", value="https://i.imgur.com/ryqKjC1.png")
         embed.add_field(name=";절레", value="https://i.imgur.com/kTDKg5t.png")
         embed.add_field(name=";와, ;우와, ;오아", value="https://i.imgur.com/8dWrgS6.png")
         embed.add_field(name=";억울", value="https://i.imgur.com/DMYyapG.png")
         embed.add_field(name=";히익", value="https://i.imgur.com/UlUikVd.png")
         embed.add_field(name=";흥칫뿡", value="https://i.imgur.com/ibHZkpl.png")
         embed.add_field(name=";ㅗ, ;엿", value="https://i.imgur.com/CQtldqK.png")
         embed.add_field(name=";죽일까", value="https://i.imgur.com/Q6tPMm2.png")
         embed.add_field(name=";아몰랑", value="https://i.imgur.com/G4jcNDk.png")
         embed.add_field(name=";ㅍㅍ", value="https://i.imgur.com/7S539cB.png")
         embed.add_field(name=";비웃음, ;피식", value="https://i.imgur.com/3dhqyVq.png")
         embed.set_footer(text="Made by 여우혼")
         await client.send_message(message.channel, embed=embed)


    elif message.content.startswith(';목록4'):
         embed=discord.Embed(title="`★거미콘 명령어 목록 [4/4] 페이지입니다.`", color=0xffff00)
         embed.add_field(name=";빡침", value="https://i.imgur.com/5HCppyD.png")
         embed.add_field(name=";지랄, ;ㅈㄹ", value="https://i.imgur.com/A7HG6Sf.png")
         embed.add_field(name=";레알, ;ㄹㅇ", value="https://i.imgur.com/8CmRp3H.png") 
         embed.add_field(name=";빼액", value="https://i.imgur.com/wi6UwCn.png")
         embed.add_field(name=";!?", value="https://i.imgur.com/dvH1YFY.png")
         embed.add_field(name=";팝콘, ;팝그작", value="https://i.imgur.com/XwVApTH.png")
         embed.add_field(name=";박수, ;짝짝", value="https://i.imgur.com/SG7T8bg.png")
         embed.add_field(name=";따봉, ;최고, ;굿", value="https://i.imgur.com/8Jmtmwc.png")
         embed.add_field(name=";설레여라얍", value="https://i.imgur.com/bzUQfDX.gif")
         embed.add_field(name=";얍", value="https://i.imgur.com/7ekHsen.png")
        
        
         
            
            
    #이하 냥장콘


    elif message.content.startswith('#냥하'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [냥하]하셨습니다.")
         em.set_image(url="https://i.imgur.com/XtIUffK.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#크으'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [크으]하셨습니다.")
         em.set_image(url="https://i.imgur.com/jTLBtAL.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#제법'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [제법]하셨습니다.")
         em.set_image(url="https://i.imgur.com/OH9e0q9.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#뭔솔'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [뭔솔]하셨습니다.")
         em.set_image(url="https://i.imgur.com/2cdmDJE.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#짜잔'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [짜잔]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8Mdu6ZS.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#집사콜'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 []하셨습니다.")
         em.set_image(url="https://i.imgur.com/jrVCYss.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#묘기증'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [묘기증]하셨습니다.")
         em.set_image(url="https://i.imgur.com/j3HZkAB.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#인정'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [인정]하셨습니다.")
         em.set_image(url="https://i.imgur.com/koAO6mH.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#고평가'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [고평가]하셨습니다.")
         em.set_image(url="https://i.imgur.com/gtKRFZp.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#=ㅅ='):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [=ㅅ=]셨습니다.")
         em.set_image(url="https://i.imgur.com/YPlxwkV.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#구토'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [구토]하셨습니다.")
         em.set_image(url="https://i.imgur.com/PxnoXYE.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#안틀림'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [안틀림]하셨습니다.")
         em.set_image(url="https://i.imgur.com/i9r0YaR.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#이게뭐지'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [이게뭐지?]하셨습니다.")
         em.set_image(url="https://i.imgur.com/dSX7kqN.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#사죄'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [사죄]하셨습니다.")
         em.set_image(url="https://i.imgur.com/OsYQBIv.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#띠용'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [띠용]하셨습니다.")
         em.set_image(url="https://i.imgur.com/oYq1V9G.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#정도껏'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [정도껏]하셨습니다.")
         em.set_image(url="https://i.imgur.com/UfUhHI7.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#뭐죠'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [뭐죠?]하셨습니다.")
         em.set_image(url="https://i.imgur.com/RTjsxE0.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#어아니'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [어아니]하셨습니다.")
         em.set_image(url="https://i.imgur.com/vlg5SAh.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#팔불출'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [팔불출]하셨습니다.")
         em.set_image(url="https://i.imgur.com/T10Nqpx.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#아니다'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [아니다]하셨습니다.")
         em.set_image(url="https://i.imgur.com/lXXo75r.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#안해요'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [안해요]하셨습니다.")
         em.set_image(url="https://i.imgur.com/4ABOkYI.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#기분굿'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [기분굿]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ujhQpTo.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#냥냥'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [냥냥]하셨습니다.")
         em.set_image(url="https://i.imgur.com/wbGYhkF.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#어떻게'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [어떻게]하셨습니다.")
         em.set_image(url="https://i.imgur.com/E0bey5C.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#안다'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [안다]하셨습니다.")
         em.set_image(url="https://i.imgur.com/MEBvcct.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#무섭'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [무섭]하셨습니다.")
         em.set_image(url="https://i.imgur.com/dUDhiJ1.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#고함'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [고함]하셨습니다.")
         em.set_image(url="https://i.imgur.com/IpColS1.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#인성'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [인성]하셨습니다.")
         em.set_image(url="https://i.imgur.com/M3GH2Td.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#아니야'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [아니야]하셨습니다.")
         em.set_image(url="https://i.imgur.com/6voOh2s.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#그런거겠지'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [그런거겠지]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ONIw8XO.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#상상속에서'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [상상속]하셨습니다.")
         em.set_image(url="https://i.imgur.com/99Pz28U.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#하지말자'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [하지말자]하셨습니다.")
         em.set_image(url="https://i.imgur.com/grWyWW3.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#누물보'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [누물보]하셨습니다.")
         em.set_image(url="https://i.imgur.com/xFUitm3.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#감사'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [감사]하셨습니다.")
         em.set_image(url="https://i.imgur.com/i26WdpR.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#ㄳ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㄳ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/i26WdpR.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#엥'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [엥]하셨습니다.")
         em.set_image(url="https://i.imgur.com/yjOxnpB.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#개같아'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [개같아]하셨습니다.")
         em.set_image(url="https://i.imgur.com/9HIRkyw.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#머쓱'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [머쓱]하셨습니다.")
         em.set_image(url="https://i.imgur.com/ghvGWFP.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#탁월'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [탁월]하셨습니다.")
         em.set_image(url="https://i.imgur.com/g1G6rH0.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#그러네'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [그러네]하셨습니다.")
         em.set_image(url="https://i.imgur.com/Nm7Ic7l.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#알고싶던'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [알고싶던]하셨습니다.")
         em.set_image(url="https://i.imgur.com/Vmk23RW.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#냥권침해'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [냥권침해]하셨습니다.")
         em.set_image(url="https://i.imgur.com/8E9pYCC.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#감동'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [감동]하셨습니다.")
         em.set_image(url="https://i.imgur.com/OKIugXY.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#세상흉흉'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [세상흉흉]하셨습니다.")
         em.set_image(url="https://i.imgur.com/EwFzX0l.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#밑분동의'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [밑분동의]하셨습니다.")
         em.set_image(url="https://i.imgur.com/A6Tv8Pq.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#허어'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [허어]하셨습니다.")
         em.set_image(url="https://i.imgur.com/SNl4w2v.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#가지마'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [가지마]하셨습니다.")
         em.set_image(url="https://i.imgur.com/xR9hX2S.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#ㅎㅎ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅎㅎ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/2QgxSYc.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#지금간다'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [지금간다]하셨습니다.")
         em.set_image(url="https://i.imgur.com/qDU4Uwb.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#대단해'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [대단해]하셨습니다.")
         em.set_image(url="https://i.imgur.com/RD5H2iW.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#외모열일'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [외모열일]하셨습니다.")
         em.set_image(url="https://i.imgur.com/zTeE6Fb.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#혼모노'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [혼모노]하셨습니다.")
         em.set_image(url="https://i.imgur.com/okZPeKc.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#프로불편러'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [프로불편러]하셨습니다.")
         em.set_image(url="https://i.imgur.com/vD35vSx.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#헐'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [헐]하셨습니다.")
         em.set_image(url="https://i.imgur.com/pccUaxm.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#어그로'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [어그로]하셨습니다.")
         em.set_image(url="https://i.imgur.com/cWJrQCW.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#비밀친구'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [비밀친구]하셨습니다.")
         em.set_image(url="https://i.imgur.com/9ZlNfga.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#ㅋㅋ'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [ㅋㅋ]하셨습니다.")
         em.set_image(url="https://i.imgur.com/TM7hTGB.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#인간말종'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [인간말종]하셨습니다.")
         em.set_image(url="https://i.imgur.com/HvegoQy.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#무관심'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [무관심]하셨습니다.")
         em.set_image(url="https://i.imgur.com/7GguuLa.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#포기'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [포기]하셨습니다.")
         em.set_image(url="https://i.imgur.com/oA4E75R.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#한마디'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [한마디]하셨습니다.")
         em.set_image(url="https://i.imgur.com/2paIrtm.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#선시비'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [선시비]하셨습니다.")
         em.set_image(url="https://i.imgur.com/Uc3DFqM.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#몰카'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [몰카]하셨습니다.")
         em.set_image(url="https://i.imgur.com/HDmJ80P.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#놀아줄까'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [놀아줄까]하셨습니다.")
         em.set_image(url="https://i.imgur.com/7oAewmv.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#며용'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [며용]하셨습니다.")
         em.set_image(url="https://i.imgur.com/huhdTaV.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#띠용'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [띠용]하셨습니다.")
         em.set_image(url="https://i.imgur.com/huhdTaV.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#왜안돼'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [왜안돼]하셨습니다.")
         em.set_image(url="https://i.imgur.com/2V3KTbJ.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#속시원'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [속시원]하셨습니다.")
         em.set_image(url="https://i.imgur.com/H6b2geK.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#누울자리'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [누울자리]하셨습니다.")
         em.set_image(url="https://i.imgur.com/qIzR13I.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#뭐왜):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [뭐왜]하셨습니다.")
         em.set_image(url="https://i.imgur.com/sKN3rSA.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#뉴비'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [뉴비]하셨습니다.")
         em.set_image(url="https://i.imgur.com/GqyhhgM.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#굿아이디어'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [굿아이디어]하셨습니다.")
         em.set_image(url="https://i.imgur.com/M4GUR62.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#호에에'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [호에에]하셨습니다.")
         em.set_image(url="https://i.imgur.com/cxEwjLt.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#히익'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [히익]하셨습니다.")
         em.set_image(url="https://i.imgur.com/D8LRkUA.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#대만족'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [대만족]하셨습니다.")
         em.set_image(url="https://i.imgur.com/Zf96hqZ.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#쿵쾅'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [쿵쾅]하셨습니다.")
         em.set_image(url="https://i.imgur.com/zNmGAHk.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#핫산'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [핫산]하셨습니다.")
         em.set_image(url="https://i.imgur.com/XPiqCkC.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#극혐'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [극혐]하셨습니다.")
         em.set_image(url="https://i.imgur.com/bvtYVJe.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#관종'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [관종]하셨습니다.")
         em.set_image(url="https://i.imgur.com/23nxehM.png")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith('#핥'):
         em = discord.Embed()
         async for log in client.logs_from(message.channel, limit=1):            
             if log.author == message.author:
                 await client.delete_message(log)
         await client.send_message(message.channel, "<@"+id+">님이 [핥]하셨습니다.")
         em.set_image(url="https://i.imgur.com/aoWmKA4.png")
         await client.send_message(message.channel, embed=em)
    
                
    #elif message.content.startswith('#'):
         #em = discord.Embed()
         #async for log in client.logs_from(message.channel, limit=1):            
             #if log.author == message.author:
                 #await client.delete_message(log)
         #await client.send_message(message.channel, "<@"+id+">님이 []하셨습니다.")
         #em.set_image(url="")
         #await client.send_message(message.channel, embed=em)

                
    elif message.content.startswith('#목록1'):
         embed=discord.Embed(title="`★냥장콘 명령어 목록 [1/4] 페이지입니다.`", color=0xffff00)
         embed.add_field(name="#냥하", value="https://i.imgur.com/XtIUffK.png")
         embed.add_field(name="#크으", value="https://i.imgur.com/jTLBtAL.png")
         embed.add_field(name="#제법", value="https://i.imgur.com/OH9e0q9.png")
         embed.add_field(name="#뭔솔", value="https://i.imgur.com/2cdmDJE.png")
         embed.add_field(name="#짜잔", value="https://i.imgur.com/8Mdu6ZS.png")
         embed.add_field(name="#집사콜", value="https://i.imgur.com/jrVCYss.png")
         embed.add_field(name="#묘기증", value="https://i.imgur.com/j3HZkAB.png")
         embed.add_field(name="#인정", value="https://i.imgur.com/koAO6mH.png")
         embed.add_field(name="#고평가", value="https://i.imgur.com/gtKRFZp.png")
         embed.add_field(name="#=ㅅ=", value="https://i.imgur.com/YPlxwkV.png")
         embed.add_field(name="#구토", value="https://i.imgur.com/PxnoXYE.png")
         embed.add_field(name="#안들림", value="https://i.imgur.com/i9r0YaR.png")
         embed.add_field(name="#이게뭐지", value="https://i.imgur.com/dSX7kqN.png")
         embed.add_field(name="#사죄", value="https://i.imgur.com/OsYQBIv.png")
         embed.add_field(name="#띠용", value="https://i.imgur.com/oYq1V9G.png")
         embed.add_field(name="#정도껏", value="https://i.imgur.com/UfUhHI7.png")
         embed.add_field(name="#뭐죠", value="https://i.imgur.com/RTjsxE0.png")
         embed.add_field(name="#어아니", value="https://i.imgur.com/vlg5SAh.png")
         embed.add_field(name="#팔불출", value="https://i.imgur.com/T10Nqpx.png")
         embed.add_field(name="#아니다", value="https://i.imgur.com/lXXo75r.png")
         embed.add_field(name="#안해요", value="https://i.imgur.com/4ABOkYI.png")
         embed.add_field(name="#기분굿", value="https://i.imgur.com/ujhQpTo.png")
         embed.add_field(name="#냥냥", value="https://i.imgur.com/wbGYhkF.png")
         embed.add_field(name="#어떻게", value="https://i.imgur.com/E0bey5C.png")
         embed.set_footer(text="Made by 여우혼")
         await client.send_message(message.channel, embed=embed)
        
                                    
    elif message.content.startswith('#목록2'):
         embed=discord.Embed(title="`★냥장콘 명령어 목록 [2/4] 페이지입니다.`", color=0xffff00)
         embed.add_field(name="#안다", value="https://i.imgur.com/MEBvcct.png")  
         embed.add_field(name="#무섭", value="https://i.imgur.com/dUDhiJ1.png")
         embed.add_field(name="#고함", value="https://i.imgur.com/IpColS1.png")
         embed.add_field(name="#인성", value="https://i.imgur.com/M3GH2Td.png")     
         embed.add_field(name="#아니야", value="https://i.imgur.com/6voOh2s.png")
         embed.add_field(name="#그런거겠지", value="https://i.imgur.com/ONIw8XO.png")
         embed.add_field(name="#상상속에서", value="https://i.imgur.com/99Pz28U.png")
         embed.add_field(name="#하지말자", value="https://i.imgur.com/grWyWW3.png")
         embed.add_field(name="#누물보", value="https://i.imgur.com/xFUitm3.png")
         embed.add_field(name="#감사, #ㄳ", value="https://i.imgur.com/i26WdpR.png")
         embed.add_field(name="#엥", value="https://i.imgur.com/yjOxnpB.png")
         embed.add_field(name="#개같아", value="https://i.imgur.com/9HIRkyw.png")
         embed.add_field(name="#머쓱", value="https://i.imgur.com/ghvGWFP.png")
         embed.add_field(name="#탁월", value="https://i.imgur.com/g1G6rH0.png")
         embed.add_field(name="#그러네", value="https://i.imgur.com/Nm7Ic7l.png")
         embed.add_field(name="#알고싶던", value="https://i.imgur.com/Vmk23RW.png")
         embed.add_field(name="#냥권침해", value="https://i.imgur.com/8E9pYCC.png")
         embed.add_field(name="#감동", value="https://i.imgur.com/OKIugXY.png")
         embed.add_field(name="#세상흉흉", value="https://i.imgur.com/EwFzX0l.png")
         embed.add_field(name="#밑분동의", value="https://i.imgur.com/A6Tv8Pq.png")
         embed.add_field(name="#허어", value="https://i.imgur.com/SNl4w2v.png")
         embed.add_field(name="#가지마", value="https://i.imgur.com/xR9hX2S.png")
         embed.add_field(name="#ㅎㅎ", value="https://i.imgur.com/2QgxSYc.png")
         embed.add_field(name="#지금간다", value="https://i.imgur.com/qDU4Uwb.png")
         embed.set_footer(text="Made by 여우혼")
         await client.send_message(message.channel, embed=embed)
        
        
    elif message.content.startswith('#목록3'):
         embed=discord.Embed(title="`★냥장콘 명령어 목록 [3/4] 페이지입니다.`", color=0xffff00)
         embed.add_field(name="#대단해", value="https://i.imgur.com/RD5H2iW.png")
         embed.add_field(name="#외모열일", value="https://i.imgur.com/zTeE6Fb.png") 
         embed.add_field(name="#혼모노", value="https://i.imgur.com/okZPeKc.png")
         embed.add_field(name="#프로불편러", value="https://i.imgur.com/vD35vSx.png")
         embed.add_field(name="#헐", value="https://i.imgur.com/pccUaxm.png")
         embed.add_field(name="#어그로", value="https://i.imgur.com/cWJrQCW.png")
         embed.add_field(name="#비밀친구", value="https://i.imgur.com/9ZlNfga.png")
         embed.add_field(name="#ㅋㅋ", value="https://i.imgur.com/TM7hTGB.png")            
         embed.add_field(name="#인간말종", value="https://i.imgur.com/HvegoQy.png")
         embed.add_field(name="#무관심", value="https://i.imgur.com/7GguuLa.png")
         embed.add_field(name="#포기", value="https://i.imgur.com/oA4E75R.png")
         embed.add_field(name="#한마디", value="https://i.imgur.com/2paIrtm.png")
         embed.add_field(name="#선시비", value="https://i.imgur.com/Uc3DFqM.png")
         embed.add_field(name="#몰카", value="https://i.imgur.com/HDmJ80P.png")
         embed.add_field(name="#놀아줄까", value="https://i.imgur.com/7oAewmv.png")
         embed.add_field(name="#며용, #띠용", value="https://i.imgur.com/huhdTaV.png")
         embed.add_field(name="#왜안돼", value="https://i.imgur.com/2V3KTbJ.png")
         embed.add_field(name="#속시원", value="https://i.imgur.com/H6b2geK.png")
         embed.add_field(name="#누울자리", value="https://i.imgur.com/qIzR13I.png")
         embed.add_field(name="#뭐왜", value="https://i.imgur.com/sKN3rSA.png")
         embed.add_field(name="#뉴비", value="https://i.imgur.com/GqyhhgM.png")
         embed.add_field(name="#굿아이디어", value="https://i.imgur.com/M4GUR62.png")
         embed.add_field(name="#호에에", value="https://i.imgur.com/cxEwjLt.png")
         embed.add_field(name="#히익", value="https://i.imgur.com/D8LRkUA.png")
         embed.set_footer(text="Made by 여우혼")
         await client.send_message(message.channel, embed=embed)
                
        
    elif message.content.startswith('#목록4'):
         embed=discord.Embed(title="`★냥장콘 명령어 목록 [4/4] 페이지입니다.`", color=0xffff00)
         embed.add_field(name="#대만족", value="https://i.imgur.com/Zf96hqZ.png")
         embed.add_field(name="#쿵쾅", value="https://i.imgur.com/zNmGAHk.png") 
         embed.add_field(name="#핫산", value="https://i.imgur.com/XPiqCkC.png")
         embed.add_field(name="#극혐", value="https://i.imgur.com/bvtYVJe.png")
         embed.add_field(name="#관종", value="https://i.imgur.com/23nxehM.png")
         embed.add_field(name="#핥", value="https://i.imgur.com/aoWmKA4.png")
         #embed.add_field(name="#", value="")
         embed.set_footer(text="Made by 여우혼")
         await client.send_message(message.channel, embed=embed)




client.run(token)

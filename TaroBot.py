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

    elif message.content.startswith('!속담'):
         messages = ["[가까운 길 마다하고 먼 길로 간다.]\n편하고 빠른 방법이 있는데도 구태여 어렵고 힘든 방법을 택한다는 뜻.", "[가까운 남이 먼 일가보다 낫다.]\n이웃과 서로 돕고 가까이 지내면 그것이 먼 곳에 있는 친척보다 더 친하고 다정하다는 말.", "[가난한 집에 자식 많다.]\n가난한 집에는 먹을 것, 입을 것이 늘 걱정인데 거기다가 자식까지 많다고 하여 이르는 말.", "[가는 손님 뒤꼭지가 예쁘다.]\n가난하여 손님 대접하기가 어려울 때는 일찍 돌아가는 손님이 고맙게 여겨진다는 말.", "[가는 정이 있어야 오는 정이 있다.]\n상대방이 잘해 주기를 바란다면 먼저 상대방에게 잘해 주어야 한다는 뜻.", "[가다 말면 안 가느니만 못하다.]\n어떤일을 하다가 도중에 그만 두려면, 처음부터 하지 않는 편이 낫다는 뜻.", "[가랑비에 옷 젖는 줄 모른다.]\n작은 일도 자주 당하게 되면 큰 결과를 가져오게 되므로 ,작은 일도 허술하게 생각해서는 안된다는 뜻.", "[가랑잎이 솔잎더러 바스락거린다고 한다.]\n제 허물이 큰 줄은 모르고 , 남의 작은 허물을 나무라는 어리석은 행동을 이르는 말.", "[가려운 곳 긁어 주듯.]\n불편한데가 없도록 여러 마음을 써 시중을 든다는 뜻.", "[가을 부채는 시세가 없다.]\n쓰는 시기가 지난 것은 값어치가 없다는 뜻.", "[개가 다 웃겠다.]\n너무 어처구니없는 일이라는 뜻.", "[개 팔자가 상팔자다.]\n주느 대로 먹고 자는 개가 부럽다는 뜻으로 ,일이 고생스러운 때 쓰는 말.", "[객지 생활 삼 년에 골이 빈다.]\n집을 나와 객지로 돌아다니게 되면 아무리 잘 해준다 해도 고생이 된다는 말.", "[거지끼리 동냥 바가지 깬다.]\n서로 도와 주고 동정해야 할 사람들이 서로 다투고 해친다는 말.", "[걱정도 팔자.]\n아무 관계도 없으면서도 남의 일에 참견하는 사람을 비웃는 말.", "[걱정이 반찬이면 상다리가 부러진다.]\n걱정을 하고자 들면 끝도 없는 것, 쓸데없이 하는 걱정에 못을 박기 위해 하는 말.", "[걸음아 나 살려라.]\n위험이 닥쳐 급하게 뛰어갈 때 쓰는 말.", "[검은 머리 파뿌리 되도록.]\n검은 머리가 파뿌리처럼 하얗게 된다 함이니 아주 늙도록까지라는 뜻.", "[게눈 감추듯 한다.]\n음식을 먹을 때 매우 빨리 먹어 치운다는 말.", "[겨울이 지나지 않고 봄이 오랴.]\n세상 일은 어떤 것이나 순서가 있는 것이니 급하다고하여 억지로 할 수 없다는 말", "[겨울 화롯불은 어머니보다 낫다.]\n추운 겨울에는 따듯한 것이 제일 좋다는 뜻.", "[경주 돌이면 다 옥돌인가?]\n경주에서 옥돌이 많이 난다고 해서 경주의 돌을 다 옥돌이라고 할 수는 없다는 뜻이니,좋은 것이 많은 가운데 나쁜 것도 섞여 있다는 말.", "[경 치고 포도청 간다.]\n죽을 욕을 보고도 또 포도청에 잡혀가 벌으 받는 것처럼 매우 혹독한 형벌을 거듭 당한다는 뜻.", "[계란이나 달걀이나.]\n이름만 다를 뿐 마찬가지라는 뜻.", "[고기는 씹어야 맛이고 말은 해야 맛이다.]\n속으로 끙끙거리지 말고 할 말은 시원하게 해야 일이 잘 처리된다는 말.", "[고래 싸움에 새우 등 터진다.]\n남의 싸움에 아무 관계 없는 사람이 해를 입거나 윗사람들 싸움 으로 아랫사람이 해를 입을 때 쓰는 말.", "[고생 끝에 낙이 온다.]\n어려운 일 괴로운 일을 겪고 나면 즐겁고 좋은 일이 찾아 온다는 말.", "[고양이 보고 반찬가게 지켜 달란다.]\n귀중한 것을 믿을 수 없는 사람에게 맡겨 오히려 잃게 된다는 말.", "[곧은 나무는 재목으로 쓰이고 ,굽은 나무는 화목으로 쓰인다.]\n모든 것은 그 재능에 따라 모두 쓰일 데가 있다는 뜻.", "[곧은 나무가 먼저 꺽인다.]\n곧은 나무는 재목으로 쓸 데가 많기 때문에 먼저 베이고, 사람도 잘난 사람이 일찍 죽는다는 말.", "[과부 사정은 과부가 안다.]\n남의 사정은 같은은 처지에 있는 사람이라야 알 수 있다는 말.", "[꼭두 새벽]\n무척 이른 아침을 뜻하는 말.", "[구렁이 담 넘어가듯 한다.]\n구렁이가 담을 넘어가듯 슬그머니 얼버무리고 지나가는 것을 말함.", "[굼벵이도 구르는 재주가 있다.]\n아무리 미련하고 보잘것없는 것일지라도 한 가지 재주는 있다는 말.", "[꿈이야, 생시야]\n믿기 어려운 일이 일어났을 때 쓰는 말.", "[그림의 호랑이]\n무섭게 보이기만 할 뿐 아무 힘도 없는 것이란 뜻.", "[그 아비에 그 자식이다.]\n아비가 못된 사람이면 자식도 못된 사람이 된다는 말.", "[금강산도 식후경이다.]\n아무리 졸고 즐거운 일이라도 배가 부르고 난 뒤에라야 제대로 느낄 수 있다는 말.", "[기생 오라비 같다.]\n반들반들하게 모양을 내고 다니는 남자를 놀리는 말.", "[기와 한 장 아끼려다 대들보 썩힌다.]\n조그마한 것을 아끼다가 오히려 믄 손해를 본다는 뜻.", "[김칫국부터 마신다.]\n남의 속도 모르고 제 짐작으로 지레 그렇게 될 것으로 믿고 행동한다는 뜻.", "[까불기는 촉새 같다.]\n경망하게 촐랑거리는 사람을 가리켜 하는 말.", "[깨진 그릇]\n다시 어떻게 수습할 수 없을 만큼 일이 그릇되었다는 말."]
         await client.send_message(message.channel, "<@"+id+">님의 오늘의 속담입니다.")
         await client.send_message(message.channel, random.choice(messages))

            


    elif message.content.startswith('!목록'):
         embed=discord.Embed(title="운세봇 명령어 목록입니다.", description="!타로 (오늘의 운세를 타로카드로 알아봅니다.)\n!점괘 (오늘의 운세를 오미쿠지로 알아봅니다.)\n사용가능한 거미콘은 ';목록'으로 확인가능합니다.", color=0x0000ff)
         embed.set_footer(text="Made by 유아루")
         await client.send_message(message.channel, embed=embed)
    
    
    # 이하 디시거미콘
    
    
    
    elif message.content.startswith(';야호'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/xXk8nVo.gif")
         await client.send_message(message.channel, embed=em)
    
                
    elif message.content.startswith(';삐짐'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/64vOuO4.png")
         await client.send_message(message.channel, embed=em)
            
            
    elif message.content.startswith(';풋'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/kQxjrQo.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';훗'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/kQxjrQo.png")
         await client.send_message(message.channel, embed=em)
            
                        
    elif message.content.startswith(';디제잉'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/QX50q2M.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';좌절'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/zzjWOiL.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';빡종'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/cEoTjwN.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';데헷'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/SWks24n.gif")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';유령'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/Zacahw7.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';이불'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/e8ziPto.png")
         await client.send_message(message.channel, embed=em)
            
                                               
    elif message.content.startswith(';우마루'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/Sxm55U6.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';경례'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/lyrRk10.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';힐끔'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/tUYvhqz.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';선글라스'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/u9XNV2M.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';커피'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/5JCZONu.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';히익'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/FtRx5x3.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';메롱'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/G92wTAI.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';밥상'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/AdrQFFi.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';총'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/Qkc1h5B.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';고인'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/wxLreLP.gif")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';사형'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/2nryb2B.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';칭찬'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/ZIJBzn3.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㄹㅇ?'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/0JzK9VP.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';갑분싸'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/L4JtAWo.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';충성'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/2Ev5w2f.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';울먹'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/AQmIzxk.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';부끄'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/s7SaOnG.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';오와콘'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/MBlLJ8v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';눈물'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/EgRU44E.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';스고이'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/TOG8qKf.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';쾅쾅'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/YbAFnyb.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';빼액'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/2EBwi9n.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';팍씨'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/1lB6Nrc.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';드르렁'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/6eyIFsR.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';눈빔'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/0F2CEaK.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';?'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/MmKffzi.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';뒤적'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/zaoyKEq.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';좆까'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/jt7EdcH.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';혼란'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/Z8KDEWA.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';대신'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/e0I15eD.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';엠창인생'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/sfrk72H.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';메가폰'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/K89E9wt.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';그만'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/rWpC8Hw.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';저기요'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/L5cX93M.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';띠용'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/cGjjiAq.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';븅신'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/fgqAk3q.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';별로'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/0BoQgnF.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';안녕'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/ylUgE7v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';안뇽'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/ylUgE7v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';하이'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/ylUgE7v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅎㅇ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/ylUgE7v.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';한숨'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/fZ6JRhl.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';에휴'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/fZ6JRhl.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';친구비'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/SBRB8Lq.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';발그레'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/KzLeTh9.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';자살'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/BBnFGvh.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';훌쩍'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/YZkpqLa.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';쿠궁'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/BoHgLR7.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';꽁꽁'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/xcpgEDG.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';덜덜'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/v8nrAUE.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㄷㄷ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/v8nrAUE.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';엄근진'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/B5uAHMs.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';쏘우'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/EsYap0a.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';웃음'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/6oF3nQ8.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅎㅎ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/6oF3nQ8.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅋㅋ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/6oF3nQ8.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';키야'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/HPh6DXV.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';캬'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/HPh6DXV.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';어쩔'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/CkyVCOB.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';쯧쯧'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/wQr1DUJ.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅉㅉ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/wQr1DUJ.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';죽창'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/ryqKjC1.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅂㄷ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/ryqKjC1.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';절레'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/kTDKg5t.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';와'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/8dWrgS6.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';우와'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/8dWrgS6.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';오아'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/8dWrgS6.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';억울'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/DMYyapG.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';히익'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/UlUikVd.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';흥칫뿡'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/ibHZkpl.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅗ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/CQtldqK.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';엿'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/CQtldqK.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';죽일까'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/Q6tPMm2.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';아몰랑'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/G4jcNDk.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅍㅍ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/7S539cB.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';비웃음'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/3dhqyVq.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';피식'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/3dhqyVq.png")
         await client.send_message(message.channel, embed=em)
            
            
    elif message.content.startswith(';빡침'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/5HCppyD.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';지랄'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/A7HG6Sf.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㅈㄹ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/A7HG6Sf.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';레알'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/8CmRp3H.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';ㄹㅇ'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/8CmRp3H.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';빼액'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/wi6UwCn.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';?!'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/dvH1YFY.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';팝콘'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/XwVApTH.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';팝그작'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/XwVApTH.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';박수'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/SG7T8bg.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';짝짝'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/SG7T8bg.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';따봉'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/8Jmtmwc.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';최고'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/8Jmtmwc.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';굿'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/8Jmtmwc.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';설'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/jFDM3WP.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';레'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/t8mYziM.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';여'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/7tCg5sG.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';라'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/vxsQSVy.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';얍'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/7ekHsen.png")
         await client.send_message(message.channel, embed=em)
            
                                   
    elif message.content.startswith(';설레여라얍'):
         em = discord.Embed()
         em.set_image(url="https://i.imgur.com/jFDM3WP.png")
         await client.send_message(message.channel, embed=em)
         em.set_image(url="https://i.imgur.com/t8mYziM.png")
         await client.send_message(message.channel, embed=em)            
         em.set_image(url="https://i.imgur.com/7tCg5sG.png")
         await client.send_message(message.channel, embed=em)
         em.set_image(url="https://i.imgur.com/vxsQSVy.png")
         await client.send_message(message.channel, embed=em)            
         em.set_image(url="https://i.imgur.com/7ekHsen.png")
         await client.send_message(message.channel, embed=em)
            
         
    elif message.content.startswith(';목록'):
         embed=discord.Embed(title="★***거미콘 명령어 목록입니다.***", color=0xffff00)
         embed.add_field(name=";야호", value="https://i.imgur.com/xXk8nVo.gif")
         embed.add_field(name=";삐짐", value="https://i.imgur.com/64vOuO4.png")
         embed.set_footer(text="Made by 유아루")
         await client.send_message(message.channel, embed=embed)
         
         
            
client.run(token)


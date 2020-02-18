import discord
import os



@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("===========")


@client.event


async def on_message(message):
    where = message.guild.name
    meg = message.content
    id = message.author.name
    channel = message.channel.name
    tag = message.author.discriminator
    joy1 = "https://cdn.discordapp.com/attachments/677518892037308426/677519209626075146/31425.PNG"
    joy2 = "https://cdn.discordapp.com/attachments/677518892037308426/677519198343266364/54541346.PNG"
    boom = "https://tenor.com/view/wow-boom-explode-explosion-gif-14234227"
    news = "조이 반고자 인정을해..."
    news2 = "조이 마약밀매놀란 섹스를못해 ..."
    news3 = "로리콘 바이러스 놀라운 전염속도..."

    print("name :" + id)
    print("channel :" + channel)
    print("tag :" + tag)
    print("meg : " + meg)
    print("where : " + where)
    print("================")
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다
    
    if message.content.startswith('!DM'):
            author = message.content[4:22]
            msg = message.content[22:100]
            await message.author.send(msg)


    if message.content.startswith('!조이고자'):
        await message.channel.send("`맞아`")

        
    if message.content.startswith('!진료기록'):
        await message.channel.send(joy1)
        await message.channel.send(joy2)
        

    if message.content.startswith('!뉴스'):
        rand = random.choice([1,2,3,])

        if rand == 1:
            await message.channel.send("> :loudspeaker:"+ news + ":loudspeaker:")
        if rand == 2:
            await message.channel.send("> :loudspeaker:"+ news2 + ":loudspeaker:")
        if rand == 3:
            await message.channel.send("> :loudspeaker:"+ news3 + ":loudspeaker:")


    if message.content.startswith('!자폭'):
        await message.channel.send(boom)


    if message.content.startswith('!섹스'):
        await message.channel.send("아 ~~섹스하고싶다~~")
        await message.channel.send(":point_right: :ok_hand:")

    
    if message.content.startswith('!반성문'):
        await message.channel.send("> https://cdn.discordapp.com/attachments/679195830846095403/679273849644384256/Screenshot_20200217-172537.png")



    if message.content.startswith('!명령어'):
        await message.channel.send("`!조이고자`")
        await message.channel.send("`!진료기록`")
        await message.channel.send("`!뉴스`")
        await message.channel.send("`!자폭`")
        await message.channel.send("`!섹스`")
        await message.channel.send("`!반성문`")
        await message.channel.send("`!개발자문자 (보낼메시지)`")
        
            
        
        
        

client.run('Njc5MTkxMTE1OTUzNDcxNDg4.XkwlQw.bByp6389Df7mBk_CfJ2UK5hDbKA')

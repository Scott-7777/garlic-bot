import discord
import asyncio
import random
import openpyxl
import os

client = discord.Client()

token = "Njc3NDM2NzM2OTU0OTU3ODI2.XkZoig.fsTWxYxT767iXnw9OIJ6vkZxDAE"

@client.event
async def on_ready():
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game(".도움")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content.startswith(".도움"):
        embed = discord.Embed(title="도움말", description="** '마늘 바게트' 봇은 디스코드를 재밌게 즐길 수 있도록 도와주는 봇 입니다!** \n 마늘바게트는 주 코드가 C#이고 부 코드는 파이썬 입니다 \n \n .커맨드 = 마늘바게트의 커맨드 사용법을 알려줍니다 \n .코드 = 현재 이 봇을 실행중인 코딩 언어를 알려줍니다 \n .초대 링크 = 봇의 초대 링크를 알려드립니다", color=0x00ff00) 
        embed.set_footer(text = "by 마늘 바게트")
        await message.channel.send(embed=embed)

    if (message.content == ".코드"):
        await message.channel.send("현재 이 봇을 실행중인 코딩 언어는 **Python** 입니다.")

    if (message.content == ".초대 링크"):
        await message.channel.send("https://discordapp.com/oauth2/authorize?client_id=677436736954957826&scope=bot")

    if (message.content == ".커맨드"):
        embed = discord.Embed(title="커맨드", description="**'마늘 바게트' 봇의 커맨드를 알려줍니다** \n \n .테스트 핑 = dm을 테스트용으로 보내줍니다 \n .봇 이름 = 봇 이름을 dm으로 보내줍니다 \n .나 = 사용자의 닉네임을 알려줍니다", color=0x00ff00) 
        embed.set_footer(text = "by 마늘 바게트")
        await message.channel.send(embed=embed)

    if (message.content == ".테스트 핑"):
        await message.author.send ("dm 보내기 완료")

    if (message.content == ".봇 이름"):
        await message.author.send (client.user.name)

    if (message.content == ".자신 핑"):
        await message.channel.send(str(message.author.name) + "핑을 보냈습니다")

    if (message.content == ".나"):
        await message.channel.send("당신의 닉네임은 **"+(message.author.name)+"** 입니다")

    
    if message.content.startswith(""):
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        exp = [1, 3, 5, 7, 9]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                 sheet["B" + str(i)].value = sheet["B" + str(i)].value + 1
                 if sheet["B" + str(i)].value>= exp[sheet["C" + str(i)].value - 1]:
                     sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                     await message.channel.send(""+(message.author.name)+"님의 레벨이 1 올랐습니다! \n 현재 레벨 : " + str(sheet["C" + str(i)].value))
                 file.save("레벨.xlsx")
                 break


            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save("레벨.xlsx")
                break

            i += 1  


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)


import discord

RedR = discord.Object(id='268366492305719306')
BlueR = discord.Object(id='268366530452914177')

bot =discord.Client()

@bot.event
async def on_ready():
    print('Connected!')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)


async def getroles(user):
    rlist = []
    for r in user.roles:
        rlist.append(r.name)

    print(rlist)
    return rlist

@bot.event
async def on_message(message):
    if message.content.startswith('!assign Red'):
        test= await getroles(message.author)

        if 'Blue' in test:
            await bot.send_message(message.channel,'You are assigned a team already! Contact a admin for a team switch!')
        else:
            await bot.send_message(message.channel,'🔴 Assigned to Team Red')
            await bot.add_roles(message.author,RedR)


    if message.content.startswith('!assign Blue'):
        test= await getroles(message.author)

        if 'Red' in test:
            await bot.send_message(message.channel,'You are assigned a team already! Contact a admin for a team switch!')
        else:
            await bot.send_message(message.channel,'🔵 Assigned to Team Blue')
            await bot.add_roles(message.author,BlueR)


    if message.content.startswith('korro'):
        await bot.send_message(message.channel,'a shit')

bot.run('')




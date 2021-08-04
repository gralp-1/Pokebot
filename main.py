# yapf: enable
import requests as r
import random
import json
import discord
from decouple import config

client_secret = config("client_secret")
message_counter = 1
message_target = random.randint1(1, 898)


client = discord.Client()


class main_bot(discord.Client):
    async def on_ready(self):
        print("I swear I'm working")

    async def on_message(self, ctx):

        global message_counter, message_target

        if ctx.author != self.user:
            if message_counter == message_target:
                img = json.loads(
                    r.get("https://pokeapi.co/api/v2/pokemon/" + str(rand.randint(1, 898))).text)

                embed = discord.Embed(
                    title="PokéBot", colour=discord.Colour.blurple())
                embed.set_image(url=str(img["sprites"]["front_default"]))
                embed.set_footer(text=img["name"])

                await ctx.channel.send(embed=embed)
                message_counter = 0
                message_target = rand.randint(50, 300)
                print("new message target "+str(message_target))
            else:
                message_counter += 1


client = main_bot()
client.run(client_secret)

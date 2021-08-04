import requests as r
import random as rand
import json
import discord
import os
from decouple import config

client_secret = config("client_secret")
message_counter = 1
message_target = 5


class main_bot(discord.Client):
    async def on_ready(self):
        print("I swear I'm working")

    async def on_message(self, ctx):
        global message_counter, message_target
        print(message_counter)
        print(ctx.author)
        print(self.user)
        if str(ctx.author) != str(self.user):
            if message_counter == message_target:
                img = json.loads(
                    r.get("https://pokeapi.co/api/v2/pokemon/" + str(rand.randint(1, 898))).text)
                await ctx.channel.send(img["sprites"]["front_default"])
                message_counter = 0
                message_target = rand.randint(50, 300)
                print("new message target "+str(message_target))
            else:
                message_counter += 1


client = main_bot()
client.run(client_secret)

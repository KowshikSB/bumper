from discord.embeds import Embed
from discord.ext import commands
from discord import channel, utils
import discord
import asyncio
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from discord.ext.commands import bot

import discord
from discord.ext import commands
class bumper(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        guild=self.bot.get_guild(799526257506254868)
        musik = guild.get_channel(835539153235476570) 
        if message.channel.id==846610690592342017:
            async with aiohttp.ClientSession() as session:
                ping=f'{message.content}'
                webhook = Webhook.from_url('https://discord.com/api/webhooks/841683251742638080/L0R1BZjsh6zXxm_u71BL-Br5eVANJ75DoYLJUMt6aUaTb9CGYrZsJP7CZ1nJHb_KE6yf', adapter=AsyncWebhookAdapter(session))
                await webhook.send(ping, username='Musik')
        try:    
          s= message.embeds
          
          z=s[0]
          
          y=z.description
          
          guild=self.bot.get_guild(799526257506254868)
          channel = guild.get_channel(826399186659442689) 
          x='''It's Bump Time! 
  Type **!d bump** to Support us'''
          

          if 'Bump done' in y: 
              emd=discord.Embed(description='<:fox_wot:836972475828404255> *Drop a review about this server* **[here](https://disboard.org/review/create/799526257506254868)** *if you want*',color=0x2f3136)
              await channel.send(embed=emd)
              
              await asyncio.sleep(7200)
              em=discord.Embed(title='Discord Bump Reminder!',description=x,color=0x2f3136)
              em.set_thumbnail(url='https://cdn.discordapp.com/attachments/824594210727395368/826412920766332998/B.gif')
              em.set_footer(text="Cloudy With A Chance of Depression")
              await channel.send ('<a:capoo_work:825020992609976380> <@&825015601365778482>',embed=em)
        except IndexError:
          return None
    
        
        
def setup(bot):
    bot.add_cog(bumper(bot))

from discord.embeds import Embed
from discord.ext import commands
from discord import channel, utils
import discord
import asyncio

from discord.ext.commands import bot

import discord
from discord.ext import commands
class bumper(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        try:
          s= message.embeds
          
          z=s[0]
          
          y=z.description
          
          guild=self.bot.get_guild(799526257506254868)
          channel = guild.get_channel(826399186659442689) 
          x='''It's Bump Time! 
  Type **!d bump** to Support us'''
          rev='(https://disboard.org/review/create/799526257506254868)'

          if 'Bump done' in y: 
              
              await channel.send(f'<:fox_wot:836972475828404255> *Drop a review* **[here]{rev}** if you want')
              await asyncio.sleep(7200)
              em=discord.Embed(title='Discord Bump Reminder!',description=x,color=0x2f3136)
              
              await channel.send ('<a:capoo_work:825020992609976380> <@&825015601365778482>',embed=em)
        except IndexError:
          return None
    @commands.command()
    async def test_bump(self,message):
        guild=self.bot.get_guild(799526257506254868)
        channel = guild.get_channel(826399186659442689)
        rev='(https://disboard.org/review/create/799526257506254868)'
        em=discord.Embed(description='<:fox_wot:836972475828404255> *Drop a review* **[here]{rev}** if you want',color=0x2f3136)
        await channel.send(embed=em)
def setup(bot):
    bot.add_cog(bumper(bot))

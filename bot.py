import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} comandos registrados.")
    except Exception as e:
        print(f"Erro ao registrar comandos: {e}")

@bot.tree.command(name="playstore", description="Buscar link de jogo na Play Store")
@app_commands.describe(jogo="Nome do jogo")
async def playstore(interaction: discord.Interaction, jogo: str):
    query = jogo.replace(" ", "+")
    url = f"https://play.google.com/store/search?q={query}&c=apps"
    await interaction.response.send_message(f"🔍 Resultado para **{jogo}** na Play Store:\n{url}")

@bot.tree.command(name="apkpure", description="Buscar link de jogo no APKPure")
@app_commands.describe(jogo="Nome do jogo")
async def apkpure(interaction: discord.Interaction, jogo: str):
    query = jogo.replace(" ", "+")
    url = f"https://apkpure.com/br/search?q={query}"
    await interaction.response.send_message(f"🔍 Resultado para **{jogo}** no APKPure:\n{url}")

bot.run(os.getenv("TOKEN"))

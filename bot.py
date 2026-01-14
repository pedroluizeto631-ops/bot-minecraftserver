import discord
from discord.ext import commands
from discord.ui import View, Button
import random
import os
from dotenv import load_dotenv

# =========================
# CARREGAR VARIÁVEIS
# =========================
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# =========================
# INTENTS
# =========================
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# LINKS (MANTIDOS NA ORDEM)
# =========================

CASAS_LINKS = [
    "https://www.youtube.com/shorts/HzjSzoXP5hQ",
    "https://www.youtube.com/watch?v=Kp73eZjLQi8",
    "https://www.youtube.com/watch?v=YvzP0U8Tm5Q",
    "https://www.youtube.com/shorts/J1fYUHPX4FI"
]

BASES_LINKS = [
    "https://www.youtube.com/shorts/GHspEQPFBas",
    "https://www.youtube.com/watch?v=8WTbW7FMFss",
    "https://www.youtube.com/watch?v=niS_Fpy_2-U",
    "https://www.youtube.com/shorts/zwc1DSnkNxE"
]

FARM_COMIDA = [
    "https://www.youtube.com/shorts/Hh99QaH4GsE"
]

FARM_XP = [
    "https://www.youtube.com/shorts/17mpDMFgVs4"
]

FARM_FERRO = [
    "https://www.youtube.com/shorts/CnpxlCmc9PA"
]

FARM_MADEIRA = [
    "https://www.youtube.com/shorts/FEe8aob3c4w"
]

# =========================
# EVENTO READY
# =========================

@bot.event
async def on_ready():
    print(f"🤖 Bot online como {bot.user}")
    bot.add_view(MenuConstrucao())
    bot.add_view(MenuFarms())

# =========================
# MENU FARMS
# =========================

class MenuFarms(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="📚 Farm de Livro", style=discord.ButtonStyle.primary)
    async def livro(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"📚 **Farm de Livro**\n🎥 {random.choice(FARM_COMIDA)}"
        )

    @discord.ui.button(label="✨ Farm de XP", style=discord.ButtonStyle.primary)
    async def xp(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"✨ **Farm de XP**\n🎥 {random.choice(FARM_XP)}"
        )

    @discord.ui.button(label="⛓️ Farm de Ferro", style=discord.ButtonStyle.primary)
    async def ferro(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"⛓️ **Farm de Ferro**\n🎥 {random.choice(FARM_FERRO)}"
        )

    @discord.ui.button(label="🌾 Farm de Comida", style=discord.ButtonStyle.primary)
    async def comida(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"🌾 **Farm de Comida**\n🎥 {random.choice(FARM_COMIDA)}"
        )

    @discord.ui.button(label="🌲 Farm de Madeira", style=discord.ButtonStyle.primary)
    async def madeira(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"🌲 **Farm de Madeira**\n🎥 {random.choice(FARM_MADEIRA)}"
        )

# =========================
# MENU CONSTRUÇÃO
# =========================

class MenuConstrucao(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🏠 Casa", style=discord.ButtonStyle.primary)
    async def casa(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"🏠 **Ideia de Casa**\n🎥 {random.choice(CASAS_LINKS)}"
        )

    @discord.ui.button(label="🕵️ Base", style=discord.ButtonStyle.secondary)
    async def base(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"🕵️ **Ideia de Base**\n🎥 {random.choice(BASES_LINKS)}"
        )

    @discord.ui.button(label="🌱 Farms", style=discord.ButtonStyle.success)
    async def farms(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            "🌱 **Escolha a farm desejada:**",
            view=MenuFarms()
        )

# =========================
# COMANDO PRINCIPAL
# =========================

@bot.command()
async def construcao(ctx):
    await ctx.send(
        "🧱 **Escolha o que você quer construir:**",
        view=MenuConstrucao()
    )

# =========================
# START
# =========================

bot.run(DISCORD_TOKEN)

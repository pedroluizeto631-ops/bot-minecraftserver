import discord
from discord.ext import commands
from discord.ui import View, Button
import random
from openai import OpenAI
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()


# =========================
# CONFIG
# =========================

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# =========================
# LINKS (ORDEM ORIGINAL)
# =========================

FARM_LIVRO = [
    "https://www.youtube.com/shorts/Hh99QaH4GsE"
]

FARM_XP = [
    "https://www.youtube.com/shorts/17mpDMFgVs4"
]

FARM_FERRO = [
    "https://www.youtube.com/shorts/CnpxlCmc9PA"
]

FARM_COMIDA = [
    "https://www.youtube.com/shorts/zC25kquts_Q"
]

FARM_MADEIRA = [
    "https://www.youtube.com/shorts/FEe8aob3c4w"
]

BASES_LINKS = [
    "https://www.youtube.com/shorts/GHspEQPFBas",
    "https://www.youtube.com/watch?v=8WTbW7FMFss",
    "https://www.youtube.com/watch?v=niS_Fpy_2-U",
    "https://www.youtube.com/watch?v=niS_Fpy_2-U",
    "https://www.youtube.com/shorts/zwc1DSnkNxE"
]

CASAS_LINKS = [
    "https://www.youtube.com/shorts/HzjSzoXP5hQ",
    "https://www.youtube.com/watch?v=Kp73eZjLQi8",
    "https://www.youtube.com/watch?v=YvzP0U8Tm5Q",
    "https://www.youtube.com/shorts/J1fYUHPX4FI",
    "https://www.youtube.com/shorts/HzjSzoXP5hQ"
]

# =========================
# EVENTO
# =========================

async def terminal_status_control(bot):
    await bot.wait_until_ready()

    while not bot.is_closed():
        comando = await asyncio.to_thread(input, ">> ")

        if comando.startswith("online"):
            atividade = comando.replace("online", "").strip()
            await bot.change_presence(
                status=discord.Status.online,
                activity=discord.Game(atividade or "Minecraft")
            )
            print("🟢 Status: ONLINE")

        elif comando.startswith("ausente"):
            atividade = comando.replace("ausente", "").strip()
            await bot.change_presence(
                status=discord.Status.idle,
                activity=discord.Game(atividade or "Minecraft")
            )
            print("🌙 Status: AUSENTE")

        elif comando.startswith("dnd"):
            atividade = comando.replace("dnd", "").strip()
            await bot.change_presence(
                status=discord.Status.dnd,
                activity=discord.Game(atividade or "Minecraft")
            )
            print("⛔ Status: NÃO PERTURBE")

        elif comando == "sair":
            print("👋 Desligando bot...")
            await bot.close()
            break


@bot.event
async def on_ready():
    print(f"🤖 Bot online como {bot.user}")
    bot.loop.create_task(terminal_status_control(bot))


# =========================
# COMANDO IA
# =========================

@bot.command()
async def ia(ctx, *, pergunta: str):
    await ctx.send("🧠 Pensando...")

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente direto e útil."},
            {"role": "user", "content": pergunta}
        ]
    )

    await ctx.send(resposta.choices[0].message.content)

# =========================
# MENU FARMS
# =========================

class MenuFarms(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="📘 Livro", style=discord.ButtonStyle.primary)
    async def livro(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"📘 Farm de Livro:\n🎥 {random.choice(FARM_LIVRO)}",
            ephemeral=True
        )

    @discord.ui.button(label="✨ XP", style=discord.ButtonStyle.primary)
    async def xp(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"✨ Farm de XP:\n🎥 {random.choice(FARM_XP)}",
            ephemeral=True
        )

    @discord.ui.button(label="⛏️ Ferro", style=discord.ButtonStyle.primary)
    async def ferro(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"⛏️ Farm de Ferro:\n🎥 {random.choice(FARM_FERRO)}",
            ephemeral=True
        )

    @discord.ui.button(label="🍖 Comida", style=discord.ButtonStyle.primary)
    async def comida(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"🍖 Farm de Comida:\n🎥 {random.choice(FARM_COMIDA)}",
            ephemeral=True
        )

    @discord.ui.button(label="🪵 Madeira", style=discord.ButtonStyle.primary)
    async def madeira(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"🪵 Farm de Madeira:\n🎥 {random.choice(FARM_MADEIRA)}",
            ephemeral=True
        )

# =========================
# MENU CONSTRUÇÃO
# =========================

class MenuConstrucao(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="🏠 Casa", style=discord.ButtonStyle.secondary)
    async def casa(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"🏠 Ideia de Casa:\n🎥 {random.choice(CASAS_LINKS)}",
            ephemeral=True
        )

    @discord.ui.button(label="🏰 Base", style=discord.ButtonStyle.secondary)
    async def base(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            f"🏰 Ideia de Base:\n🎥 {random.choice(BASES_LINKS)}",
            ephemeral=True
        )

    @discord.ui.button(label="🌾 Farms", style=discord.ButtonStyle.success)
    async def farms(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message(
            "🌾 Escolha o tipo de farm:",
            view=MenuFarms(),
            ephemeral=True
        )

# =========================
# COMANDO
# =========================

@bot.command()
async def construcao(ctx):
    await ctx.send(
        "🧱 **Menu de Construção**",
        view=MenuConstrucao()
    )

@bot.command()
async def marcar(ctx):
    await ctx.send("✅ Comando **marcar** funcionando!")

# =========================
# START
# =========================

bot.run(DISCORD_TOKEN)

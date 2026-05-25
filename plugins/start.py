import time
import logging
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from bot import app

logger = logging.getLogger(__name__)

BACK = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔙 Back", callback_data="back_start")]
])


def start_markup():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📖 Commands", callback_data="help"),
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
        ],
        [InlineKeyboardButton("🏓 Ping", callback_data="ping")]
    ])


def start_text(first, build):
    return (
        f"**Namaste, {first}! 👋**\n\n"
        f"Main **🌸 Fuyuki Bot** hoon — tumhari madad ke liye yahan hoon.\n\n"
        f"╔═══════════════════╗\n"
        f"  🤖 Version  :  `{build}`\n"
        f"  ⚡ Status   :  Online ✅\n"
        f"╚═══════════════════╝\n\n"
        f"Neeche buttons se navigate karo 👇"
    )


@app.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message: Message):
    from info import BUILD_VERSION
    first = message.from_user.first_name or "Dost"
    await message.reply_text(start_text(first, BUILD_VERSION), reply_markup=start_markup())


@app.on_message(filters.command("help"))
async def help_cmd(client, message: Message):
    await message.reply_text(
        "**📖 Commands List:**\n\n"
        "• /start — Bot shuru karo\n"
        "• /help  — Yeh list dekho\n"
        "• /ping  — Bot response check karo\n"
        "• /id    — Apna / Chat ka ID dekho\n"
    )


@app.on_message(filters.command("ping"))
async def ping_cmd(client, message: Message):
    s = time.time()
    msg = await message.reply_text("🏓 Pinging...")
    ms = round((time.time() - s) * 1000)
    await msg.edit_text(f"🏓 **Pong!**\n⚡ Response: `{ms}ms`")


@app.on_message(filters.command("id"))
async def id_cmd(client, message: Message):
    user = message.from_user
    chat = message.chat
    text = f"**👤 Your ID:** `{user.id}`\n"
    if chat.id != user.id:
        text += f"**💬 Chat ID:** `{chat.id}`"
    await message.reply_text(text)


@app.on_callback_query(filters.regex("^help$"))
async def help_cb(client, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text(
        "**📖 Commands List:**\n\n"
        "• /start — Bot shuru karo\n"
        "• /help  — Yeh list dekho\n"
        "• /ping  — Bot response check karo\n"
        "• /id    — Apna / Chat ka ID dekho\n",
        reply_markup=BACK
    )


@app.on_callback_query(filters.regex("^about$"))
async def about_cb(client, cb: CallbackQuery):
    from info import BUILD_VERSION
    await cb.answer()
    await cb.message.edit_text(
        f"**🌸 Fuyuki Bot — About**\n\n"
        f"🛠️ **Version:** `{BUILD_VERSION}`\n"
        f"⚙️ **Framework:** Pyrofork\n"
        f"🗄️ **Database:** MongoDB (Motor async)\n"
        f"☁️ **Hosting:** Render / Koyeb\n"
        f"🐍 **Python:** 3.12\n",
        reply_markup=BACK
    )


@app.on_callback_query(filters.regex("^ping$"))
async def ping_cb(client, cb: CallbackQuery):
    await cb.answer("Pong! 🏓")
    await cb.message.edit_text("🏓 **Pong!** Bot online hai ✅", reply_markup=BACK)


@app.on_callback_query(filters.regex("^back_start$"))
async def back_cb(client, cb: CallbackQuery):
    from info import BUILD_VERSION
    first = cb.from_user.first_name or "Dost"
    await cb.answer()
    await cb.message.edit_text(start_text(first, BUILD_VERSION), reply_markup=start_markup())
    

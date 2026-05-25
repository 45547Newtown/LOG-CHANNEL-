import logging
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

logger = logging.getLogger(__name__)

# ── /start ────────────────────────────────────────────────────────
@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client: Client, message: Message):
    from info import BUILD_VERSION
    user = message.from_user
    first = user.first_name or "Dost"

    text = (
        f"**Namaste, {first}! 👋**\n\n"
        f"Main **🌸 Fuyuki Bot** hoon — tumhari madad ke liye yahan hoon.\n\n"
        f"╔═══════════════════╗\n"
        f"  🤖 Version  :  `{BUILD_VERSION}`\n"
        f"  ⚡ Status   :  Online ✅\n"
        f"╚═══════════════════╝\n\n"
        f"Neeche buttons se navigate karo 👇"
    )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📖 Commands", callback_data="help"),
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
        ],
        [
            InlineKeyboardButton("🏓 Ping", callback_data="ping"),
        ]
    ])

    await message.reply_text(text, reply_markup=buttons)


# ── /help ─────────────────────────────────────────────────────────
@Client.on_message(filters.command("help"))
async def help_cmd(client: Client, message: Message):
    await message.reply_text(
        "**📖 Commands List:**\n\n"
        "• /start — Bot shuru karo\n"
        "• /help  — Yeh list dekho\n"
        "• /ping  — Bot response check karo\n"
        "• /id    — Apna / Chat ka ID dekho\n"
    )


# ── /ping ─────────────────────────────────────────────────────────
@Client.on_message(filters.command("ping"))
async def ping_cmd(client: Client, message: Message):
    import time
    start = time.time()
    msg = await message.reply_text("🏓 Pinging...")
    ms = round((time.time() - start) * 1000)
    await msg.edit_text(f"🏓 **Pong!**\n⚡ Response: `{ms}ms`")


# ── /id ───────────────────────────────────────────────────────────
@Client.on_message(filters.command("id"))
async def id_cmd(client: Client, message: Message):
    user = message.from_user
    chat = message.chat
    text = f"**👤 Your ID:** `{user.id}`\n"
    if chat.id != user.id:
        text += f"**💬 Chat ID:** `{chat.id}`"
    await message.reply_text(text)


# ── Callbacks ─────────────────────────────────────────────────────
@Client.on_callback_query(filters.regex("^help$"))
async def help_cb(client: Client, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit_text(
        "**📖 Commands List:**\n\n"
        "• /start — Bot shuru karo\n"
        "• /help  — Yeh list dekho\n"
        "• /ping  — Bot response check karo\n"
        "• /id    — Apna / Chat ka ID dekho\n",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="back_start")]
        ])
    )


@Client.on_callback_query(filters.regex("^about$"))
async def about_cb(client: Client, cb: CallbackQuery):
    from info import BUILD_VERSION
    await cb.answer()
    await cb.message.edit_text(
        f"**🌸 Fuyuki Bot — About**\n\n"
        f"🛠️ **Version:** `{BUILD_VERSION}`\n"
        f"⚙️ **Framework:** Pyrofork (Pyrogram fork)\n"
        f"🗄️ **Database:** MongoDB (Motor async)\n"
        f"☁️ **Hosting:** Render / Koyeb\n"
        f"🐍 **Python:** 3.12\n",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="back_start")]
        ])
    )


@Client.on_callback_query(filters.regex("^ping$"))
async def ping_cb(client: Client, cb: CallbackQuery):
    import time
    await cb.answer("Pinging...")
    start = time.time()
    ms = round((time.time() - start) * 1000 + 1)
    await cb.message.edit_text(
        f"🏓 **Pong!**\n⚡ Response: `{ms}ms`",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Back", callback_data="back_start")]
        ])
    )


@Client.on_callback_query(filters.regex("^back_start$"))
async def back_start_cb(client: Client, cb: CallbackQuery):
    from info import BUILD_VERSION
    user = cb.from_user
    first = user.first_name or "Dost"

    text = (
        f"**Namaste, {first}! 👋**\n\n"
        f"Main **🌸 Fuyuki Bot** hoon — tumhari madad ke liye yahan hoon.\n\n"
        f"╔═══════════════════╗\n"
        f"  🤖 Version  :  `{BUILD_VERSION}`\n"
        f"  ⚡ Status   :  Online ✅\n"
        f"╚═══════════════════╝\n\n"
        f"Neeche buttons se navigate karo 👇"
    )

    await cb.answer()
    await cb.message.edit_text(
        text,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("📖 Commands", callback_data="help"),
                InlineKeyboardButton("ℹ️ About", callback_data="about"),
            ],
            [
                InlineKeyboardButton("🏓 Ping", callback_data="ping"),
            ]
        ])
    )
  

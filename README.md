# 🤖 Fuyuki Bot

Minimal Telegram bot — starts and sends restart message to log channel.

## 📨 Restart Message Format

```
Mai Fuyuki Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : 2026-05-22
⏰ Tɪᴍᴇ : 13:48:40 PM
🌐 Tɪᴍᴇᴢᴏɴᴇ : Asia/Kolkata
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs:  v1.4 [ Sᴛᴀʙʟᴇ ]
```

## 🔧 Required Variables

| Variable | Description |
|----------|-------------|
| `API_ID` | From [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | From [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | From [@BotFather](https://t.me/BotFather) |
| `LOG_CHANNEL` | Your log channel ID (bot must be admin) |

## ⚙️ Optional Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `TIMEZONE` | `Asia/Kolkata` | Timezone for timestamps |
| `BUILD_VERSION` | `v1.4` | Version shown in restart message |
| `SESSION` | `FuyukiBot` | Pyrogram session name |

## 🚀 Deploy

### Render / Koyeb
1. Upload to GitHub
2. New → **Worker** → Docker
3. Add env variables
4. Deploy

### VPS
```bash
git clone <your-repo>
cd FuyukiBot
pip install -r requirements.txt
cp .env.sample .env
# fill .env values
python3 bot.py
```

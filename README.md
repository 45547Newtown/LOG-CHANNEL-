# 🌸 Fuyuki Bot

Telegram bot — **Pyrofork** + **MongoDB** + **aiohttp** (keep-alive)

---

## ⚙️ Environment Variables

| Variable        | Required | Description |
|-----------------|----------|-------------|
| `API_ID`        | ✅ | [my.telegram.org](https://my.telegram.org) |
| `API_HASH`      | ✅ | [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN`     | ✅ | [@BotFather](https://t.me/BotFather) |
| `LOG_CHANNEL`   | ✅ | Log channel ID (e.g. `-1001234567890`) |
| `MONGO_URI`     | ✅ | `mongodb+srv://user:pass@cluster.mongodb.net/` |
| `SESSION`       | No | Session name (default: `FuyukiBot`) |
| `DB_NAME`       | No | MongoDB DB name (default: `FuyukiBot`) |
| `TIMEZONE`      | No | Default: `Asia/Kolkata` |
| `BUILD_VERSION` | No | Default: `v1.4` |
| `PORT`          | No | Default: `8080` |

---

## 🚀 Deploy

### ▶ Render.com
1. Repo GitHub par push karo
2. [render.com](https://render.com) → **New** → **Blueprint**
3. Repo connect karo — `render.yaml` auto-read hoga
4. Dashboard mein ye secret vars fill karo:
   `API_ID`, `API_HASH`, `BOT_TOKEN`, `LOG_CHANNEL`, `MONGO_URI`
5. **Deploy** ✅

### ▶ Koyeb
1. [koyeb.com](https://koyeb.com) → **Create App** → **GitHub**
2. **Builder:** Docker, **Dockerfile path:** `Dockerfile`
3. **Port:** `8080` — Health check path: `/health`
4. Saare env vars add karo
5. **Deploy** ✅

### ▶ Local Testing
```bash
cp .env.sample .env
# .env fill karo
pip install -r requirements.txt
python3 bot.py
```

### ▶ Docker Local
```bash
docker build -t fuyukibot .
docker run --env-file .env -p 8080:8080 fuyukibot
```

---

## 🍃 MongoDB Atlas (Free Setup)
1. [mongodb.com/atlas](https://www.mongodb.com/atlas) par free cluster banao
2. Database user create karo (read/write)
3. Network Access mein `0.0.0.0/0` whitelist karo
4. **Connect** → **Drivers** → URI copy karo → `MONGO_URI` mein paste karo

---

## 📁 Project Structure
```
FuyukiBot/
├── bot.py            # Main entry — bot + web server start
├── info.py           # Env vars config
├── database.py       # MongoDB async helpers
├── keep_alive.py     # aiohttp web server (Render/Koyeb health check)
├── plugins/
│   ├── __init__.py
│   └── start.py      # /start /help /ping /id commands
├── requirements.txt
├── Dockerfile
├── render.yaml       # Render.com config
├── app.json
├── Procfile
├── heroku.yml
├── logging.conf
└── .env.sample
```

## 🤖 Bot Commands
| Command | Description |
|---------|-------------|
| `/start` | Bot start message |
| `/help` | Commands list |
| `/ping` | Bot alive check |
| `/id` | Apna Telegram ID dekho |

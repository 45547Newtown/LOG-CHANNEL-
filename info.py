import re
from os import environ

id_pattern = re.compile(r'^-?\d+$')

# ── Core ──────────────────────────────────────────────────────────
SESSION    = environ.get("SESSION",   "FuyukiBot")
API_ID     = int(environ.get("API_ID",    ""))
API_HASH   = environ.get("API_HASH",  "")
BOT_TOKEN  = environ.get("BOT_TOKEN", "")

# ── Log Channel ───────────────────────────────────────────────────
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))

# ── Web / Server ─────────────────────────────────────────────────
PORT = int(environ.get("PORT", "8080"))

# ── Display ───────────────────────────────────────────────────────
TIMEZONE      = environ.get("TIMEZONE",      "Asia/Kolkata")
BUILD_VERSION = environ.get("BUILD_VERSION", "v1.4")

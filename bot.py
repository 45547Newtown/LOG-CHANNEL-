import asyncio
import logging
import logging.config
from datetime import datetime
import pytz
from pyrogram import Client, idle
from info import (
    API_ID, API_HASH, BOT_TOKEN,
    LOG_CHANNEL, SESSION, PORT, TIMEZONE, BUILD_VERSION
)

logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

logger = logging.getLogger(__name__)


class FuyukiBot(Client):
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=4,
            sleep_threshold=10,
        )


bot = FuyukiBot()


async def main():
    await bot.start()
    me = await bot.get_me()

    tz = pytz.timezone(TIMEZONE)
    now = datetime.now(tz)
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S %p")

    restart_msg = (
        f"Mai Fuyuki Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !\n\n"
        f"📅 Dᴀᴛᴇ : {date_str}\n"
        f"⏰ Tɪᴍᴇ : {time_str}\n"
        f"🌐 Tɪᴍᴇᴢᴏɴᴇ : {TIMEZONE}\n"
        f"🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs:  {BUILD_VERSION} [ Sᴛᴀʙʟᴇ ]"
    )

    await bot.send_message(chat_id=LOG_CHANNEL, text=restart_msg)
    logger.info(f"Bot @{me.username} started successfully.")

    await idle()
    await bot.stop()


if __name__ == "__main__":
    asyncio.run(main())

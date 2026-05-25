"""
keep_alive.py — Lightweight HTTP server
Render/Koyeb ko lagta hai bot "alive" hai.
Port 8080 par simple web server chalata hai.
"""

import asyncio
import logging
from aiohttp import web

logger = logging.getLogger(__name__)


async def health_handler(request):
    return web.Response(text="FuyukiBot is alive! 🌸", status=200)


async def start_webserver(port: int = 8080):
    app = web.Application()
    app.router.add_get("/", health_handler)
    app.router.add_get("/health", health_handler)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info(f"✅ Web server started on port {port}")

"""
database.py — MongoDB connection & helper functions
Uses motor (async) so it works perfectly with Pyrogram's asyncio loop.
"""

import logging
from motor.motor_asyncio import AsyncIOMotorClient
from info import MONGO_URI, DB_NAME

logger = logging.getLogger(__name__)

# ── Client & DB ───────────────────────────────────────────────────
_client: AsyncIOMotorClient | None = None


def get_db():
    """Return the active database instance."""
    if _client is None:
        raise RuntimeError("MongoDB not connected. Call connect_db() first.")
    return _client[DB_NAME]


async def connect_db():
    """Connect to MongoDB. Call once at bot startup."""
    global _client
    if not MONGO_URI:
        logger.warning("MONGO_URI not set — database features disabled.")
        return
    try:
        _client = AsyncIOMotorClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        # Ping to confirm connection
        await _client.admin.command("ping")
        logger.info(f"✅ Connected to MongoDB — database: {DB_NAME}")
    except Exception as e:
        logger.error(f"❌ MongoDB connection failed: {e}")
        _client = None


async def close_db():
    """Close MongoDB connection. Call at bot shutdown."""
    global _client
    if _client:
        _client.close()
        _client = None
        logger.info("MongoDB connection closed.")


# ── Generic Helpers ───────────────────────────────────────────────

async def db_find_one(collection: str, query: dict) -> dict | None:
    """Find a single document."""
    db = get_db()
    return await db[collection].find_one(query)


async def db_upsert(collection: str, query: dict, data: dict):
    """Insert or update a document."""
    db = get_db()
    await db[collection].update_one(query, {"$set": data}, upsert=True)


async def db_delete(collection: str, query: dict):
    """Delete matching documents."""
    db = get_db()
    await db[collection].delete_many(query)


async def db_find_all(collection: str, query: dict = {}) -> list:
    """Fetch all matching documents as a list."""
    db = get_db()
    cursor = db[collection].find(query)
    return await cursor.to_list(length=None)

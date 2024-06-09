import pytest
import asyncpg
from database import connect_db


@pytest.mark.asyncio
async def test_connect_db():
    conn = None
    try:
        conn = await connect_db('user2', 'password', 'images_db', '127.0.0.1', 5433)
        assert isinstance(conn, asyncpg.Connection)
    except Exception as e:
        pytest.fail(f"Failed to connect to the database: {e}")
    finally:
        if conn:
            await conn.close()

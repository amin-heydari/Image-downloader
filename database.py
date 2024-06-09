import asyncpg
import asyncio


async def connect_db(user, password, database, host='127.0.0.1', port=5433):
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host, port=port)
    return conn


async def create_table(conn):
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id SERIAL PRIMARY KEY,
            image_data BYTEA NOT NULL
        )
    ''')


async def store_image(conn, image_data):
    await conn.execute('''
        INSERT INTO images (image_data) VALUES ($1)
    ''', image_data)

import pytest
from database import connect_db, create_table


@pytest.mark.asyncio
async def test_create_table():
    conn = None
    try:
        conn = await connect_db('user2', 'password', 'images_db', '127.0.0.1', 5433)

        await create_table(conn)

        result = await conn.fetch("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'images'
            );
        """)

        table_exists = result[0]['exists']
        assert table_exists, "Table 'images' does not exist."

    except Exception as e:
        pytest.fail(f"Failed to create the table: {e}")
    finally:
        if conn:
            await conn.close()

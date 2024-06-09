import asyncpg

from database import connect_db, create_table, store_image
from downloadImages import download_images
from imageUrls import fetch_image_urls
import asyncio

from resizeImages import resize_image


async def main():
    query = input("please enter a search query: ")
    image_limit = int(input("please enter a number for maximum number of images to be fetched: "))
    resize_dimensions = (100, 100)

    db_user = input("Enter PostgreSQL username: ")
    db_password = input("Enter PostgreSQL password: ")
    db_name = input("Enter PostgreSQL database name: ")
    db_host = input("Enter PostgreSQL host (default '127.0.0.1'): ") or '127.0.0.1'
    db_port = input("Enter PostgreSQL port (default '5433'): ") or 5433

    image_urls = await fetch_image_urls(query, image_limit)
    print(f"Image URLs: {image_urls}")

    images = await download_images(image_urls)
    print(f"Downloaded {len(images)} images")

    resized_images = [resize_image(img, resize_dimensions) for img in images if img]
    print(f"Resized {len(resized_images)} images")

    conn = await connect_db(db_user, db_password, db_name, db_host, int(db_port))
    await create_table(conn)
    for img in resized_images:
        await store_image(conn, img)

    await conn.close()
    print('Images saved successfully!')


if __name__ == "__main__":
    asyncio.run(main())

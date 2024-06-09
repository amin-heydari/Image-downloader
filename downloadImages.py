import aiohttp
import asyncio


async def download_image(url, session):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.read()
        return None


async def download_images(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(url, session) for url in urls]
        return await asyncio.gather(*tasks)

import aiohttp
from bs4 import BeautifulSoup


async def fetch_image_urls(query, max_images):
    search_url = f"https://www.google.com/search?q={query}&tbm=isch"
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            image_elements = soup.find_all('img')

            image_urls = []
            for img in image_elements:
                src = img.get('src')
                if src and src.startswith('http'):
                    image_urls.append(src)
                if len(image_urls) >= max_images:
                    break

            return image_urls

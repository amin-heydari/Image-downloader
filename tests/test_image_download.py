import pytest
from downloadImages import download_images
from imageUrls import fetch_image_urls


@pytest.mark.asyncio
async def test_image_download():
    try:
        query = "test"
        image_limit = 1
        image_urls = await fetch_image_urls(query, image_limit)
        assert len(image_urls) == image_limit
        images = await download_images(image_urls)
        assert len(images) == image_limit
    except Exception as e:
        pytest.fail(f"Image download test failed: {e}")

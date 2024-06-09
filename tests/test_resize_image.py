import pytest
from resizeImages import resize_image


def test_resize_image():
    try:
        with open('tests/download.jpg', 'rb') as f:
            sample_image = f.read()
        resized_image = resize_image(sample_image, (100, 100))
    except Exception as e:
        pytest.fail(f"Image resizing test failed: {e}")

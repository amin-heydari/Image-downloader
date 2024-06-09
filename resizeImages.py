from PIL import Image
import io


def resize_image(image_bytes, size):
    image = Image.open(io.BytesIO(image_bytes))
    image = image.resize(size)
    byte_array = io.BytesIO()
    image.save(byte_array, format='PNG')
    return byte_array.getvalue()

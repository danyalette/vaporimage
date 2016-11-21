from django.core.files.uploadedfile import InMemoryUploadedFile
import StringIO
from PIL import Image, ImageOps

def invertImgColor(img):
    if img.mode == 'RGBA':
        r,g,b,a = img.split()
        rgb_image = Image.merge('RGB', (r,g,b))
        inverted_image = ImageOps.invert(rgb_image)
        r2,g2,b2 = inverted_image.split()
        final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
        return final_transparent_image
    else:
        inverted_image = ImageOps.invert(image)
    return inverted_image

def pilToPng(pillow, name):
    img_io = StringIO.StringIO()
    pillow.save(img_io, format='PNG')
    img_file = InMemoryUploadedFile(img_io, None, name + '.png', 'image/png',
                                  img_io.len, None)
    return img_file

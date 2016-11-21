from __future__ import unicode_literals
from __future__ import division
from PIL import Image
import random

from ops import addGradientToImg, addShapesToImg, createCutout
from utils import invertImgColor, pilToPng
from color import getColorPalette

def createImage(name, width, height):

    # scale image up in order to later downsize with antialiasing
    scale = 3
    img = Image.new('RGBA', (width * scale, height * scale), 'white')

    palette = getColorPalette()

    img = addGradientToImg(
        img=img,
        start_color=palette[0].getString(),
        end_color=palette[1].getString()
    )

    img = addShapesToImg(
        img=img,
        size=random.choice([width/24,width/16,width/8]) * scale,
        padding=random.randrange(width//200,width//40) * scale,
        color=palette[2].getString()
    )

    cutout = createCutout(
        img=img,
        padding=random.choice([width/24,width/16,width/8]) * scale
    )

    # do color and direction inversion
    cutout = invertImgColor(cutout).transpose(Image.FLIP_LEFT_RIGHT)

    # add cutout layer on image
    img.paste(cutout, (0, 0), cutout)

    # resize to original dimensions
    img = img.resize((width,height), Image.ANTIALIAS)

    return pilToPng(img, name)

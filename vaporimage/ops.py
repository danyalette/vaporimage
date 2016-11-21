from __future__ import division
from PIL import Image, ImageDraw, ImageFilter
import random

def addGradientToImg(img, start_color, end_color):
    width, height = img.size
    draw = ImageDraw.Draw(img)
    draw.rectangle((0,0,width/2,height), fill=start_color)
    draw.rectangle((width/2,0,width,height), fill=end_color)
    return img.filter(ImageFilter.GaussianBlur(radius=width/6))

def addShapesToImg(img, size, padding, color):
    draw = ImageDraw.Draw(img)
    shape_type = random.choice(['circle', 'square', 'triangle'])
    count_x = int(img.size[0]/size)
    count_y = int(img.size[1]/size)
    offset_top = (img.size[1] % size)/2

    for i in range(count_x):
        for n in range(count_y):
            drawShape(
                img=img,
                shape_type=shape_type,
                points=((i * size) + padding, (n * size) + padding + offset_top, ((i + 1) * size) - padding, ((n + 1) * size) - padding + offset_top),
                fill=color
            )
    return img

def drawShape(img, shape_type, points, fill):
    draw = ImageDraw.Draw(img)
    if shape_type == 'circle':
        return draw.ellipse(points, fill=fill)
    if shape_type == 'square':
        return draw.rectangle(points, fill=fill)
    if shape_type == 'triangle':
        x1, y1, x2, y2 = points
        # make triangle equilateral
        h = 0.866 * (x2 - x1)
        offset = ((y2 - y1) - h)/2
        y1 = y1 + offset
        y2 = y2 - offset
        return draw.polygon([(x1 + (x2-x1)/2, y1),(x2, y2),(x1, y2)], fill=fill)

def createCutout(img, padding):
    cutout = img.copy()

    # create mask
    mask = Image.new('L', cutout.size, 0)
    shape_size = min(cutout.size[0], cutout.size[1]) - padding * 2
    offset_left = (cutout.size[0] - (shape_size + padding * 2))/2
    offset_top = (cutout.size[1] - (shape_size + padding * 2))/2

    # draw shape in mask
    draw = ImageDraw.Draw(mask)
    shape_type = random.choice(['circle', 'square', 'triangle'])
    drawShape(
        img=mask,
        shape_type=shape_type,
        points=(padding + offset_left, padding + offset_top, shape_size + offset_left + padding, shape_size + offset_top + padding),
        fill=255
    )

    # apply mask
    cutout.putalpha(mask)

    return cutout

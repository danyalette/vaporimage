import random
import colorsys

def getColorPalette():
    starting_hue = random.randrange(360)
    colors = [HslColor({ "hue": starting_hue }).rotateHue((120*i)) for i in range(3)]
    return colors

class HslColor:
    def __init__(self, params):
        self.setHslOrRandom(params)

    def setHslOrRandom(self,params):
        self.hue = params.get('hue', random.randrange(360))
        self.sat = params.get('sat', random.randrange(0,30))
        self.lum = params.get('lum', random.randrange(30,70))
        rgb = colorsys.hls_to_rgb(self.hue/360, self.lum/100, self.sat/100)
        self.r, self.g, self.b = rgb

    def getString(self):
        return 'hsl(%d, %d%%, %d%%)' % (self.hue, self.sat, self.lum)

    def rotateHue(self, degrees):
        self.hue = (self.hue + degrees) % 360
        return self
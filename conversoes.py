### 1 - NORMALIZA RGB
def normaliza_RGB(R=0, G=0, B=0, r=0, g=0, b=0):
    r = R / (R + G + B)
    g = G / (R + G + B)
    b = B / (R + G + B)

    if (r, g, b) == (255, 255, 255):
        return r + g + b

### 2 - RGB PARA HSV
import colorsys
colorsys.rgb_to_hsv(.3, .4, .2)
(0.25, 0.5, 0.4)

### 3 - HSV PARA RGB
import colorsys
colorsys.hsv_to_rgb(0.25, 0.5, 0.4)
(0.3, 0.4, 0.2)

### 4 - RGB PARA CMYK
RGB_SCALE = 255
CMYK_SCALE = 100

def rgb_para_cmyk (r, g, b):
    if (r, g, b) == (0, 0, 0):
        #preto
        return 0, 0, 0, CMYK_SCALE

    # rgb [0, 255] -> cmyk [0, 1]
    c = 1 - r / RGB_SCALE
    m = 1 - g / RGB_SCALE
    y = 1 - b / RGB_SCALE

    #valor do k [0, 1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    return c * CMYK_SCALE, m * CMYK_SCALE, y * CMYK_SCALE, k * CMYK_SCALE

### 5 - CMYK PARA RGB
def cmyk_para_rgb(c, m, y, k, cmyk_scale, rgb_scale=255):
    r = rgb_scale * (1.0 - c / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    g = rgb_scale * (1.0 - m / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    b = rgb_scale * (1.0 - y / float(cmyk_scale)) * (1.0 - k / float(cmyk_scale))
    return r, g, b

### 6 - RGB PARA GRAYSCALE
def rgb_para_grayscale(I, R=0, G=0, B=0):
    if (R, G, B) == (10, 20, 30):
        I = (R+G+B) / 3
        return I



















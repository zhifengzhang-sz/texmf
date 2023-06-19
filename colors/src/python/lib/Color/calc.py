import spectra
import colorsys

indigo=spectra.html('#0d3d56')
sophia=spectra.html('#0f5b78')
skyee=spectra.html('#117899')
alice=spectra.html('#1496bb')
jade=spectra.html('#5ca794')
kelly=spectra.html('#a3b86c')
daisy=spectra.html('#ebc944')
amber=spectra.html('#edaa38')
april=spectra.html('#f08c2d')
coral=spectra.html('#f26d21')
rowan=spectra.html('#d94e20')
ruby=spectra.html('#c02f1d')

jet=spectra.html('#131516')
raven=spectra.html('#373d3f')
asher=spectra.html('#555f61')
stone=spectra.html('#707c80')
gray=spectra.html('#8c979a')
sterling=spectra.html('#a7b0b2')
heather=spectra.html('#c1c7c9')
pearl=spectra.html('#dadedf')
lilia=spectra.html('#f2f3f4')

def luminance(c:str)->float:
    color = c[1:]
    hex_red = int(color[0:2], base=16)
    hex_green = int(color[2:4], base=16)
    hex_blue = int(color[4:6], base=16)
    return hex_red * 0.2126 + hex_green * 0.7152 + hex_blue * 0.0722

def foreground(c:str)->str:
    l=luminance(c)
    if l<140: return lilia.hexcode
    else: return jet.hexcode

def complementary(val:tuple[int,int,int])->tuple[int,int,int]:
    """
    Takes rgb tuple and produces complimentary color.
    """
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 150 and 210 degrees
    deg_180_hue = h + (180.0 / 360.0)
    return tuple(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))

def rgb_complementary(c:tuple[int,int,int])->tuple[int,int,int]:
    return tuple(map(lambda x:255-x,c))

def shade(c:tuple[int,int,int],factor:float)->tuple[int,int,int]:
    return tuple(map(lambda x:int(x*(1-factor)),c))

def tint(c:tuple[int,int,int],factor:float)->tuple[int,int,int]:
    return tuple(map(lambda x:int(x+(255-x)*(1-factor)),c))

def triadic(val:tuple[int,int,int])->list[tuple[int,int,int]]:
    """
    Takes rgb tuple and produces list of triadic colors.
    """
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_120_hue = h + (120.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_120_rgb = tuple(map(lambda x: int(round(x * 255)),colorsys.hls_to_rgb(deg_120_hue, l, s)))
    color_240_rgb = tuple(map(lambda x: int(round(x * 255)),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_120_rgb, color_240_rgb]

def tetradic(val:tuple[int,int,int])->list[tuple[int,int,int]]:
    """
    Takes rgb tuple and produces list of tetradic colors.
    """
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_60_hue = h + (60.0 / 360.0)
    deg_180_hue = h + (180.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_60_rgb = tuple(map(lambda x: int(round(x * 255)),colorsys.hls_to_rgb(deg_60_hue, l, s)))
    color_180_rgb = tuple(map(lambda x: int(round(x * 255)),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    color_240_rgb = tuple(map(lambda x: int(round(x * 255)),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_60_rgb, color_180_rgb, color_240_rgb]

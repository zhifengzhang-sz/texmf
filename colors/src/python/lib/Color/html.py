from IPython.display import HTML
import spectra
from Color.calc import foreground
from typing import Dict

swatch_template = """
<div style="float: left;">
    <div style="width: 50px; height: 50px; background: {0};"></div>
    <div>{0}</div>
</div>
"""
swatch_outer = """
<div style='width: 500px; overflow: auto; font-size: 10px; 
    font-weight: bold; text-align: center; line-height: 1.5;'>{0}</div>
"""

def show_palette(colors:list[str])->HTML:
    html =  swatch_outer.format("".join(map(swatch_template.format, colors)))
    return HTML(html)

def swatches(colors:list[spectra.core.Color])->HTML:
    hexes = (c.hexcode.upper() for c in colors)
    return show_palette(hexes)

def less_palette(pname:str,palette:Dict[str,str])->None:
    for n,c in palette.items():
        print(f'@{pname}_{n}:{c};')
        if pname != 'body_text':
            print(f"@{pname}_{n}_fg:{foreground(c)};")

def css_palette(pname:str,palette:Dict[str,str])->None:
    print(":root{")
    for n,c in palette.items():
        print(f'--{pname}_{n}:{c};')
        if pname != 'body_text':
            print(f"--{pname}_{n}_fg:{foreground(c)};")
    print("}")
from Color.calc import foreground
import sys
from Color.database import PaletteDB

def definecolor(name,color)->str:
    return f'\\definecolor[named]{{{name}}}{{HTML}}{{{color[1:]}}}'
        
def qicolormodel(name:str,palette:list[str])->str:
    cmd=f'\\qicolormodel{{{name}}}'
    for c in palette:
        cmd+=f'{{{c[1:]}}}'
    return cmd

def qicolormodeltext(name:str,palette:list[str])->str:
    cmd=f'\\qicolormodeltext{{{name}}}'
    for c in tuple(map(lambda x:foreground(x),palette)):
        cmd+=f'{{{c[1:]}}}'
    return cmd

def key2model(name:str,key:int)->str: return qicolormodel(name,PaletteDB.palette(key))
def key2modeltext(name:str,key:int)->str: return qicolormodeltext(name,PaletteDB.palette(key))

def colormap(key:int)->str:
    cs=''
    for c in PaletteDB.palette(key):
        cs+=f'{c[1:]},'
    return f'{{{key}({cs[:-1]})}}'

def colormaplist(keys:list[int])->str:
    ks=''
    for k in keys:
        ks+=f'{colormap(k)},\n\t'
    return f'colormap/.list={{\n\t{ks[:-3]}}}'

def colormaptext(keys:list[int])->str:
    ks=''
    for k in keys:
        cs=''
        p=PaletteDB.palette(k)
        for c in p:
            cs+=f'{foreground(c)[1:]},'
        ks+=f'{{{k}({cs[:-1]})}},\n\t'
    return f'colormapc/.list={{\n\t{ks[:-3]}}}'
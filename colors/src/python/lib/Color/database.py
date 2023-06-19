class PaletteDB:
    image_links={587:'https://colorpalettes.net/wp-content/uploads/2014/10/cvetovaya-palitra-587.jpg'
                ,3841:'https://colorpalettes.net/wp-content/uploads/2018/05/farbpalette-3841.png'
                ,4405:'https://colorpalettes.net/wp-content/uploads/2022/05/color-palette-4405.png'
                ,4502:'https://colorpalettes.net/wp-content/uploads/2022/07/color-palette-4502.png'
                ,4507:'https://colorpalettes.net/wp-content/uploads/2022/07/color-palette-4507.png'
                ,4508:'https://colorpalettes.net/wp-content/uploads/2022/07/color-palette-4508.png'
                ,4522:'https://colorpalettes.net/wp-content/uploads/2022/07/color-palette-4522.png'
                ,4529:'https://colorpalettes.net/wp-content/uploads/2022/07/color-palette-4529.png'
                ,4530:'https://colorpalettes.net/wp-content/uploads/2022/07/color-palette-4530.png'
                ,4552:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4552.png'
                ,4555:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4555.png'
                ,4558:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4558.png'
                ,4561:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4561.png'
                ,4565:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4565.png'
                ,4566:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4566.png'
                ,4571:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4571.png'
                ,4572:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4572.png'
                ,4573:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4573.png'
                ,4574:'https://colorpalettes.net/wp-content/uploads/2022/08/color-palette-4574.png'
                }
    palettes={587:['#d35002','#ffa602','#f9d692','#c18e01','#4f5819']
             ,3841:['#A05E2B','#E0992C','#F1EEA6','#EBDDD2','#F7F5F6']
             ,4405:['#274215','#85BB4D','#CAD8D8','#EEA402','#DD7236']
             ,4502:['#BF8709','#EAC57D','#B9BBDE','#807490','#523857']
             ,4507:['#6A3F36','#C8A796','#F4F3EE','#F8E4BE','#EEA988']
             ,4508:['#6A7793','#CFD1E0','#F9F7FA','#D0C9D0','#B4A8AA']
             ,4522:['#567A04','#D4CF6D','#D7A3B6','#9783A9','#54387F']
             ,4529:['#945D87','#EDD1EC','#EECC70','#D71232','#82071B']
             ,4530:['#D3B19E','#D39CBD','#995E7C','#683142','#312528']
             ,4552:['#BB35AE','#E99FF4','#EDE7F8','#F5BB2C','#D2B4AA']
             ,4555:['#3D5220','#B7CB99','#778FD2','#2A3759','#431D32']
             ,4558:['#5A7A0A','#83D350','#FAB036','#FDD48A','#513C2F']
             ,4561:['#338309','#C9D46C','#E48716','#FAAB01','#DFBCB2']
             ,4565:['#677C77','#445F3B','#8EA076','#E0EFEA','#564734']
             ,4566:['#180C0C','#483948','#B2AB2E','#ED413E','#EFB786']
             ,4571:['#217074','#37745B','#8B9D77','#E7EAEF','#EDC5AB']
             ,4572:['#AA1803','#BD613C','#F1BAA1','#BCAF4D','#6D8C00']
             ,4573:['#1A2902','#344C11','#778D45','#AEC09A','#AEC670']
             ,4574:['#583E26','#A78B71','#F7C815','#EC9704','#9C4A1A']
             }
    colorpalette_address='https://colorpalettes.net/color-palette-'

    vgetdotcom={'indigo':'#0d3d56'
               ,'sophia':'#0f5b78'
               ,'skyee':'#117899'
               ,'alice':'#1496bb'
               ,'jade':'#5ca794'
               ,'kelly':'#a3b86c'
               ,'daisy':'#ebc944'
               ,'amber':'#edaa38'
               ,'april':'#f08c2d'
               ,'coral':'#f26d21'
               ,'rowan':'#d94e20'
               ,'ruby':'#c02f1d'
               ,'jet':'#131516'
               ,'raven':'#373d3f'
               ,'asher':'#555f61'
               ,'stone':'#707c80'
               ,'gray':'#8c979a'
               ,'sterling':'#a7b0b2'
               ,'heather':'#c1c7c9'
               ,'pearl':'#dadedf'
               ,'lilia':'#f2f3f4'}
    
    @staticmethod
    def palette(n:int)->list[str]:
        return PaletteDB.palettes[n]
    @staticmethod
    def palette_image_url(n:int)->str:
        return PaletteDB.image_links[n]
    @staticmethod
    def colorpalette_url(n:int)->str:
        return PaletteDB.colorpalette_address+str(n)
    

class LightPalette:
    body_text={'bg':PaletteDB.vgetdotcom['lilia'],'fg':PaletteDB.vgetdotcom['jet']}
    main={0:[PaletteDB.vgetdotcom['asher'],PaletteDB.vgetdotcom['stone'],PaletteDB.vgetdotcom['gray'],PaletteDB.vgetdotcom['coral']]
          }
    s1={0:[PaletteDB.vgetdotcom['asher'],PaletteDB.vgetdotcom['stone'],PaletteDB.vgetdotcom['gray'],PaletteDB.vgetdotcom['april']]}
    s2={0:[PaletteDB.vgetdotcom['asher'],PaletteDB.vgetdotcom['stone'],PaletteDB.vgetdotcom['gray'],PaletteDB.vgetdotcom['kelly']]}
    s3={0:[PaletteDB.vgetdotcom['asher'],PaletteDB.vgetdotcom['stone'],PaletteDB.vgetdotcom['gray'],PaletteDB.vgetdotcom['alice']]}

class DarkPalette:
    body_text={'bg':PaletteDB.vgetdotcom['jet'],'fg':PaletteDB.vgetdotcom['lilia']}
    main={0:[PaletteDB.vgetdotcom['lilia'],PaletteDB.vgetdotcom['pearl'],PaletteDB.vgetdotcom['heather'],PaletteDB.vgetdotcom['coral']]}
    s1={0:[PaletteDB.vgetdotcom['lilia'],PaletteDB.vgetdotcom['pearl'],PaletteDB.vgetdotcom['heather'],PaletteDB.vgetdotcom['april']]}
    s2={0:[PaletteDB.vgetdotcom['lilia'],PaletteDB.vgetdotcom['pearl'],PaletteDB.vgetdotcom['heather'],PaletteDB.vgetdotcom['kelly']]}
    s3={0:[PaletteDB.vgetdotcom['lilia'],PaletteDB.vgetdotcom['pearl'],PaletteDB.vgetdotcom['heather'],PaletteDB.vgetdotcom['alice']]}


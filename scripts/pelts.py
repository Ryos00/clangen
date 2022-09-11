from random import choice, randint


class SingleColour(object):
    name = "SingleColour"
    sprites = {1: 'single'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"
        self.patch_colour = False
        self.tortiebase = False
        
    def __repr__(self):
        return self.colour + self.length

class TwoColour(object):
    name = "TwoColour"
    sprites = {1: 'single', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'VAN', 'ANY', 'TUXEDO', 'LITTLE', 'VAN',
        'ANY2', 'ANY2', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'VANCREAMY', 'ANY2CREAMY', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO',
        'BUZZARDFANG', 'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'TIP', 'FANCY',
        'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'TAIL',
        'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'PAWS', 'FAROFA', 'DAMIEN',
        'MISTER', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'PANTS', 'REVERSEPANTS', 
        'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED',
        'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK'
    ]
    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True
        self.patch_colour = False
        self.tortiebase = False
        
    def __repr__(self):
        return f"white and {self.colour}{self.length}"

class Tabby(object):
    name = "Tabby"
    sprites = {1: 'tabby', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'VAN', 'ANY', 'TUXEDO', 'LITTLE', 'VAN',
        'ANY2', 'ANY2', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG',
        'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY',
        'LITTLECREAMY', 'VANCREAMY', 'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES',
        'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE',
        'BIB', 'UNDERS', 'PAWS', 'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES',
        'BROKENBLAZE', 'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 
        'APPALOOSA', 'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 
        'POINTMARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
        self.patch_colour = False
        self.tortiebase = False
        
    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} tabby"
        else:
            return self.colour + self.length + " tabby"

class Marbled(object):
    name = "Marbled"
    sprites = {1: 'marbled', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'VAN', 'ANY', 'TUXEDO', 'LITTLE', 'VAN',
        'ANY2', 'ANY2', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG',
        'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY',
        'LITTLECREAMY', 'VANCREAMY', 'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES',
        'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE',
        'BIB', 'UNDERS', 'PAWS', 'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES',
        'BROKENBLAZE', 'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 
        'APPALOOSA', 'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
        self.patch_colour = False
        self.tortiebase = False
        
    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} marbled"
        else:
            return self.colour + self.length + " marbled"

class Rosette(object):
    name = "Rosette"
    sprites = {1: 'rosette', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'VAN', 'ANY', 'TUXEDO', 'LITTLE', 'VAN',
        'ANY2', 'ANY2', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG',
        'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY',
        'LITTLECREAMY', 'VANCREAMY', 'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES',
        'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE',
        'BIB', 'UNDERS', 'PAWS', 'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES',
        'BROKENBLAZE', 'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 
        'APPALOOSA', 'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
        self.patch_colour = False
        self.tortiebase = False
        
    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} rosette"
        else:
            return self.colour + self.length + " rosette"

class Smoke(object):
    name = "Smoke"
    sprites = {1: 'smoke', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'VAN', 'ANY', 'TUXEDO', 'LITTLE', 'VAN',
        'ANY2', 'ANY2', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG',
        'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY',
        'LITTLECREAMY', 'VANCREAMY', 'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES',
        'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE',
        'BIB', 'UNDERS', 'PAWS', 'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES',
        'BROKENBLAZE', 'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 
        'APPALOOSA', 'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
        self.patch_colour = False
        self.tortiebase = False
        
    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} smoke"
        else:
            return self.colour + self.length + " smoke"

class Ticked(object):
    name = "Ticked"
    sprites = {1: 'ticked', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'VAN', 'ANY', 'TUXEDO', 'LITTLE', 'VAN',
        'ANY2', 'ANY2', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG',
        'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY',
        'LITTLECREAMY', 'VANCREAMY', 'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES',
        'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE',
        'BIB', 'UNDERS', 'PAWS', 'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES',
        'BROKENBLAZE', 'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 
        'APPALOOSA', 'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
        self.patch_colour = False

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ticked"
        else:
            return self.colour + self.length + " ticked"

class Speckled(object):
    name = "Speckled"
    sprites = {1: 'speckled', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
        self.patch_colour = False
        self.tortiebase = False
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} speckled{self.length}"
        else:
            return f"{self.colour} speckled{self.length}"

class Bengal(object):
    name = "Bengal"
    sprites = {1: 'bengal', 2: 'white'}
    white_patches = [
        'ANY', 'TUXEDO', 'LITTLE', 'ANY', 'TUXEDO', 'LITTLE', 'ANY2', 'ANY2',
        'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY',
        'ANY2CREAMY', 'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'UNDERS', 'PAWS',
        'FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TOES', 'BROKENBLAZE', 
        'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA',
        'PIEBALD', 'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK'

    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
        self.patch_colour = False
        self.tortiebase = False
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bengal{self.length}"
        else:
            return f"{self.colour} bengal{self.length}"

class Tortie(object):
    name = "Tortie"
    sprites = {1: 'tortiesolid', 2: 'tortietabby', 3: 'tortiebengal', 4: 'tortiemarbled',
    5: 'tortieticked', 6: 'tortiesmoke', 7: 'tortierosette', 8: 'tortiespeckled', 9: 'white'}
    white_patches = [
        'TUXEDO', 'LITTLE', 'TUXEDO', 'LITTLE', None, None, None, None,
        'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
        'VITILIGO', 'TUXEDOCREAMY', 'LITTLECREAMY', 'TIP', 'FANCY',
        'BLAZE', 'BIB', 'UNDERS', 'PAWS', 'DAMIEN', 'BELLY', 'TOES',
        'BROKENBLAZE', 'BROKENBLAZE', 'BROKENBLAZE', 'PAWS', 'PAWS', 'PAWS',
        'TOES', 'TOES', 'TOES', 'TIP', 'TIP', 'TIP',
        'KARPATI', 'SKUNK', 'LILTWO', 'POINTMARK'
        ]

    def __init__(self, white, length, patch_colour, tortiebase):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = choice(["SILVER", "GREY", "DARKGREY", "BLACK",
                              "LIGHTBROWN", "BROWN", "DARKBROWN"])
        self.length = length
        self.patch_colour = patch_colour
        self.tortiebase = tortiebase

    def __repr__(self):
        if self.white:
            return f"white and tortoiseshell{self.length}"
        else:
            return f"tortoiseshell{self.length}"

class Calico(object):
    name = "Calico"
    sprites = {1: 'tortiesolid', 2: 'tortietabby', 3: 'tortiebengal', 4: 'tortiemarbled',
    5: 'tortieticked', 6: 'tortiesmoke', 7: 'tortierosette', 8: 'tortiespeckled', 9: 'white'}
    white_patches = [
        'VAN', 'VAN', 'ANY', 'ANY2', 'ANY', 'ANY2'
        'ONEEAR', 'BROKEN', 'RAGDOLL',
        'LIGHTSONG', 'VITILIGO', 'VANCREAMY',
        'ANY2CREAMY', 'FRECKLES', 'RINGTAIL', 'HALFFACE',
        'PANTS2', 'GOATEE', 'TAIL', 'PRINCE', 'TAIL',
        'FAROFA', 'MISTER', 'FAROFA', 'MISTER',
        'PANTS', 'REVERSEPANTS', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 
        'PIEBALD', 'CURVED', 'HEART',  'GLASS', 'MOORISH', 'POINTMARK'
    ]
    def __init__(self, length, patch_colour, tortiebase):
        self.colour = choice(["SILVER", "GREY", "DARKGREY", "BLACK",
                              "LIGHTBROWN", "BROWN", "DARKBROWN"])
        self.length = length
        self.white = True
        self.patch_colour = patch_colour
        self.tortiebase = tortiebase

    def __repr__(self):
        return f"calico{self.length}"



# ATTRIBUTES, including non-pelt related
pelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN']
pelt_c_no_white = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER', 'GOLDEN',
    'GINGER', 'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN']
pelt_c_no_bw = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'PALEGINGER', 'GOLDEN', 'GINGER',
    'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN']
tortie_pattern = ['tortiesolid', 'tortietabby', 'tortiebengal', 'tortiemarbled', 'tortieticked',
    'tortiesmoke', 'tortierosette', 'tortiespeckled']
patch_colour = ['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'GOLDONE', 'GOLDTWO',
    'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
    'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']
tortiebase = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled']
tortiecolour = ["SILVER", "GREY", "DARKGREY", "BLACK", "LIGHTBROWN", "BROWN", "DARKBROWN"]

pelt_length = ["short", "medium", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE']
scars1 = ["ONE", "TWO", "THREE"]
scars2 = ["LEFTEAR", "RIGHTEAR", "LEFTEAR", "RIGHTEAR", "NOTAIL"]
scars3 = ["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
          "BLACK", "SPIKES", "PINK", "PURPLE", "MULTI", "CRIMSONBELL", "BLUEBELL",
          "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
          "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "PINKBELL", "PURPLEBELL",
          "MULTIBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
          "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "PINKBOW",
          "PURPLEBOW", "MULTIBOW"]
scars4 = ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY", "TOETRAP"]
scars5 = ["SNAKE"]

pelt_names_F = ["SingleColour", "SingleColour", "TwoColour", "Tabby", "Tortie", "Calico",
    "Tabby", "TwoColour", "Speckled", "Marbled", "Bengal", "TortieBengal",
    "Rosette", "Smoke", "Ticked", "CalicoBengal"]
pelt_names_M = ["SingleColour", "SingleColour", "TwoColour", "Tabby", "Tabby", "Speckled",
    "TwoColour", "Marbled", "Bengal", "Rosette", "Smoke", "Ticked"]

# SPRITE NAMES
single_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'LIGHTBROWN', 'BROWN', 'DARKBROWN']
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE',
    'BLUEYELLOW', 'BLUEGREEN']
white_sprites = [
    'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANYCREAMY',
    'TUXEDOCREAMY', 'LITTLECREAMY', 'COLOURPOINTCREAMY', 'VANCREAMY', 'ONEEAR',
    'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL', 'LIGHTSONG', 'VITILIGO',
    'TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE',
    'TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'PAWS', 'FAROFA', 'DAMIEN',
    'MISTER', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE',
    'PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
    'CURVED', 'HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK']
skin_sprites = ['BLACK', 'RED', 'PINK']


# CHOOSING PELT
def choose_pelt(gender,
                colour=None,
                white=None,
                pelt=None,
                length=None,
                patch_colour=None,
                tortiebase=None,
                determined=False):
    if pelt is None:
        if gender == 'female':
            pelt = choice(pelt_names_F)
        else:
            if randint(0,100) == 1:
                pelt = choice(pelt_names_F)
            else:
                pelt = choice(pelt_names_M)
                
    length = choice(pelt_length)
    if pelt == "SingleColour":
        if colour is None and not white:
            return SingleColour(choice(pelt_colours), length)
        elif colour is None:
            return SingleColour("WHITE", length)
        else:
            return SingleColour(colour, length)
    elif pelt == "TwoColour":
        if colour is None:
            return TwoColour(choice(pelt_c_no_white), length)
        else:
            return TwoColour(colour, length)
    elif pelt == "Tabby":
        if colour is None and white is None:
            return Tabby(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Tabby(choice(pelt_colours), white, length)
        else:
            return Tabby(colour, white, length)
    elif pelt == "Marbled":
        if colour is None and white is None:
            return Marbled(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Marbled(choice(pelt_colours), white, length)
        else:
            return Marbled(colour, white, length)
    elif pelt == "Rosette":
        if colour is None and white is None:
            return Rosette(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Rosette(choice(pelt_colours), white, length)
        else:
            return Rosette(colour, white, length)
    elif pelt == "Smoke":
        if colour is None and white is None:
            return Smoke(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Smoke(choice(pelt_colours), white, length)
        else:
            return Smoke(colour, white, length)
    elif pelt == "Ticked":
        if colour is None and white is None:
            return Ticked(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ticked(choice(pelt_colours), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == "Speckled":
        if colour is None and white is None:
            return Speckled(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Speckled(choice(pelt_colours), white, length)
        else:
            return Speckled(colour, white, length)
    elif pelt == "Bengal":
        if colour is None and white is None:
            return Bengal(choice(pelt_colours), choice([False, True]),
                             length)
        elif colour is None:
            return Bengal(choice(pelt_colours), white, length)
        else:
            return Bengal(colour, white, length)
    elif pelt == "Tortie":
        if white is None:
            return Tortie(choice([False, True]), length, patch_colour, tortiebase)
        else:
            return Tortie(white, length, patch_colour, tortiebase)
    else:
        return Calico(length, patch_colour, tortiebase)

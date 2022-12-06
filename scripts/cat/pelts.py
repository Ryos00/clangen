from random import choice, randint


class SingleColour():
    name = "SingleColour"
    sprites = {1: 'single'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length

class TwoColour():
    name = "TwoColour"
    sprites = {1: 'single', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"

class Tabby():
    name = "Tabby"
    sprites = {1: 'tabby', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} tabby"
        else:
            return self.colour + self.length + " tabby"

class Spotted():
    name = "Spotted"
    sprites = {1: 'spotted', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} spotted"
        else:
            return self.colour + self.length + " spotted"

class Patternless():
    name = "Patternless"
    sprites = {1: 'patternless', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO', 'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} patternless"
        else:
            return self.colour + self.length + " patternless"

class Smoke():
    name = "Smoke"
    sprites = {1: 'smoke', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} smoke"
        else:
            return self.colour + self.length + " smoke"

class Ticked():
    name = "Ticked"
    sprites = {1: 'ticked', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ticked"
        else:
            return self.colour + self.length + " ticked"

class Speckled():
    name = "Speckled"
    sprites = {1: 'speckled', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} speckled{self.length}"
        else:
            return f"{self.colour} speckled{self.length}"

class Classic():
    name = "Classic"
    sprites = {1: 'classic', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} classic{self.length}"
        else:
            return f"{self.colour} classic{self.length}"

class Broken():
    name = "Broken"
    sprites = {1: 'broken', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',
        'MITAINE', 'SQUEAKS', 'STAR',
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS', 
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO',
        'VITILIGO2'
    ]
    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length
    def __repr__(self):
        if self.white:
            return f"white and {self.colour} broken{self.length}"
        else:
            return f"{self.colour} broken{self.length}"

class Tortie():
    name = "Tortie"
    sprites = {1: 'tortie', 2: 'white'}
    white_patches = [
        'LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 
        'BIB', 'VEE', 'PAWS', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO',
        'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
        'TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK',  'MITAINE', 'SQUEAKS', 'STAR',
        'COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL', 'POINTMARK', 'VITILIGO', 'VITILIGO2'
        ]

    def __init__(self, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = choice(["SILVER", "GREY", "DARKGREY", "BLACK",
                              "LIGHTBROWN", "BROWN", "DARKBROWN", "DARKCHOC", "TAUPE", "LIGHTTAUPE",
                              "LIGHTFAWN", "FAWN", "CINNAMON", "DARKCINNAMON", "CARAMEL", "LIGHTCARAMEL"])
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and tortoiseshell{self.length}"
        else:
            return f"tortoiseshell{self.length}"

class Calico():
    name = "Calico"
    sprites = {1: 'calico', 2: 'white'}
    white_patches = [
        'ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 
        'HALFFACE', 'PANTS2', 'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 
        'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED', 'GLASS',
        'VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH',
        'MASKMANTLE', 'APRON', 'CAPSADDLE'
    ]
    def __init__(self, length):
        self.colour = choice(["SILVER", "GREY", "DARKGREY", "BLACK",
                              "LIGHTBROWN", "BROWN", "DARKBROWN", "DARKCHOC", "TAUPE", "LIGHTTAUPE",
                              "LIGHTFAWN", "FAWN", "CINNAMON", "DARKCINNAMON", "CARAMEL", "LIGHTCARAMEL"])
        self.length = length
        self.white = True

    def __repr__(self):
        return f"calico{self.length}"


# ATTRIBUTES, including non-pelt related
pelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'APRICOT', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'DARKCHOC', 'TAUPE', 'LIGHTTAUPE', 'LIGHTFAWN', 'FAWN', 'CINNAMON', 'DARKCINNAMON', 'CARAMEL',
    'LIGHTCARAMEL'
]
pelt_c_no_white = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'APRICOT', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'DARKCHOC', 'TAUPE', 'LIGHTTAUPE', 'LIGHTFAWN', 'FAWN', 'CINNAMON', 'DARKCINNAMON', 'CARAMEL',
    'LIGHTCARAMEL'
]
pelt_c_no_bw = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'APRICOT', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'DARKCHOC', 'TAUPE', 'LIGHTTAUPE', 'LIGHTFAWN', 'FAWN', 'CINNAMON', 'DARKCINNAMON', 'CARAMEL',
    'LIGHTCARAMEL'
]
tortiepatterns = ['tortiesolid', 'tortietabby', 'tortiespotted', 'tortieticked',
    'tortiesmoke', 'tortiepatternless', 'tortiespeckled', 'tortieclassic', 'tortiebroken']
patch_colours = ['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'GOLDONE', 'GOLDTWO',
    'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR',
    'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR', 'CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR',
    'APRICOTONE', 'APRICOTTWO', 'APRICOTTHREE', 'APRICOTFOUR']
tortiebases = ['single', 'tabby', 'spotted', 'ticked', 'smoke', 'patternless', 'speckled', 'classic', 'broken']
tortiecolours = ["SILVER", "GREY", "DARKGREY", "BLACK", "LIGHTBROWN", "BROWN", "DARKBROWN", 
                "DARKCHOC", "TAUPE", "LIGHTTAUPE", "LIGHTFAWN", "FAWN", "CINNAMON", "DARKCINNAMON", 
                "CARAMEL", "LIGHTCARAMEL"]

pelt_length = ["short", "medium", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE']
# scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE"]
scars2 = ["LEFTEAR", "RIGHTEAR", "LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW"]
scars3 = ["SNAKE", "TOETRAP"]

plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                    "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                    "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "PINK", "PURPLE", "MULTI", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW"
]

pelt_names_F = ["SingleColour", "TwoColour", "Tabby", "Tortie", "Calico",
                "Spotted", "Patternless", "Smoke", "Ticked"]
pelt_names_M = ["SingleColour", "TwoColour", "Tabby", "Spotted", "Patternless", "Smoke", "Ticked"]

# SPRITE NAMES
single_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'APRICOT', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'DARKCHOC', 'TAUPE', 'LIGHTTAUPE', 'LIGHTFAWN', 'FAWN', 'CINNAMON', 'DARKCINNAMON', 'CARAMEL',
    'LIGHTCARAMEL'
]
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE',
    'BLUEYELLOW', 'BLUEGREEN'
]
little_white = ['LITTLE', 'LITTLECREAMY', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS', 
    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY']
mid_white = ['TUXEDO', 'TUXEDOCREAMY', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR']
high_white = ['ANY', 'ANYCREAMY', 'ANY2', 'ANY2CREAMY', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 
    'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
    'CURVED', 'GLASS', 'MASKMANTLE']
mostly_white = ['VAN', 'VANCREAMY', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE']
point_markings = ['COLOURPOINT', 'COLOURPOINTCREAMY', 'RAGDOLL']
vit = ['VITILIGO', 'VITILIGO2']
white_sprites = [
    little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE', 'EXTRA', 'POINTMARK'
]

skin_sprites = ['BLACK', 'RED', 'PINK']


# CHOOSING PELT
def choose_pelt(gender,colour=None,white=None,pelt=None,length=None,determined=False):
    if pelt is None:
        a = randint(0, 100)
        if a != 1:
            pelt = choice(pelt_names_F) if gender == "female" else choice(pelt_names_M)
        else:
            pelt = choice(pelt_names_F)
            if gender == 'male' and pelt in ['Tortie', 'Calico']:
                print("Male tortie/calico!")
    elif pelt in ['Tortie', 'Calico'] and gender == 'male' and not determined:
        a = randint(0, 200)
        if a != 1:
            pelt = choice(pelt_names_M)
    if length is None:
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
            return Tabby(choice(pelt_c_no_white), choice([False, True]), length)
        elif colour is None:
            return Tabby(choice(pelt_c_no_white), white, length)
        else:
            return Tabby(colour, white, length)
    elif pelt == "Spotted":
        if colour is None and white is None:
            return Spotted(choice(pelt_c_no_white), choice([False, True]), length)
        elif colour is None:
            return Spotted(choice(pelt_c_no_white), white, length)
        else:
            return Spotted(colour, white, length)
    elif pelt == "Patternless":
        if colour is None and white is None:
            return Patternless(choice(pelt_c_no_white), choice([False, True]), length)
        elif colour is None:
            return Patternless(choice(pelt_c_no_white), white, length)
        else:
            return Patternless(colour, white, length)
    elif pelt == "Speckled":
        if colour is None and white is None:
            return Speckled(choice(pelt_c_no_white), choice([False, True]), length)
        elif colour is None:
            return Speckled(choice(pelt_c_no_white), white, length)
        else:
            return Speckled(colour, white, length)
    elif pelt == "Classic":
        if colour is None and white is None:
            return Classic(choice(pelt_c_no_white), choice([False, True]), length)
        elif colour is None:
            return Classic(choice(pelt_c_no_white), white, length)
        else:
            return Classic(colour, white, length)
    elif pelt == "Broken":
        if colour is None and white is None:
            return Broken(choice(pelt_c_no_white), choice([False, True]), length)
        elif colour is None:
            return Broken(choice(pelt_c_no_white), white, length)
        else:
            return Broken(colour, white, length)
    elif pelt == "Smoke":
        if colour is None and white is None:
            return Smoke(choice(pelt_c_no_white), choice([False, True]), length)
        elif colour is None:
            return Smoke(choice(pelt_c_no_white), white, length)
        else:
            return Smoke(colour, white, length)
    elif pelt == "Ticked":
        if colour is None and white is None:
            return Ticked(choice(pelt_c_no_white), choice([False, True]), length)
        elif colour is None:
            return Ticked(choice(pelt_c_no_white), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == "Tortie":
        if white is None:
            return Tortie(choice([False, True]), length)
        else:
            return Tortie(white, length)
    else:
        return Calico(length)

def describe_color(pelt, tortiecolour, tortiepattern, white_patches):
        color_name = ''
        color_name = str(pelt.colour).lower()
        if tortiecolour is not None:
            color_name = str(tortiecolour).lower()
        if color_name == 'palegrey':
            color_name = 'pale grey'
        elif color_name == 'darkgrey':
            color_name = 'dark grey'
        elif color_name == 'paleginger':
            color_name = 'pale ginger'
        elif color_name == 'darkginger':
            color_name = 'red'
        elif color_name == 'lightbrown':
            color_name = 'light brown'
        elif color_name == 'darkbrown':
            color_name = 'chocolate'
        elif color_name == 'darkchoc':
            color_name = 'dark chocolate'
        elif color_name == 'lighttaupe':
            color_name = 'light taupe'
        elif color_name == 'lightfawn':
            color_name = 'light fawn'
        elif color_name == 'darkcinnamon':
            color_name = 'dark cinnamon'
        elif color_name == 'lightcaramel':
            color_name = 'light caramel'
        if pelt.name == "Tabby":
            color_name = color_name + ' mackerel tabby'
        elif pelt.name == "Spotted":
            color_name = color_name + ' spotted tabby'
        elif pelt.name == "Patternless":
            color_name = color_name + ' agouti'
        elif pelt.name == "Ticked":
            color_name = color_name + ' ticked tabby'
        elif pelt.name == "Smoke":
            color_name = color_name + ' smoke'
        elif pelt.name == "Speckled":
            color_name = color_name + ' speckled tabby'
        elif pelt.name == "Classic":
            color_name = color_name + ' classic tabby'
        elif pelt.name == "Broken":
            color_name = color_name + ' broken mackerel tabby'

        elif pelt.name == "Tortie":
            if tortiepattern not in ["tortiesolid", "tortiesmoke", "tortiepatternless"]:
                color_name = color_name + ' torbie'
            else:
                color_name = color_name + ' tortie'
        elif pelt.name == "Calico":
            if tortiepattern not in ["tortiesolid", "tortiesmoke", "tortiepatternless"]:
                color_name = color_name + ' tabico'
            else:
                color_name = color_name + ' calico'
        # enough to comment but not make calico
        if white_patches is not None:
            if white_patches in little_white + mid_white:
                color_name = color_name + ' and white'
            # and white
            elif white_patches in high_white:
                if pelt.name != "Calico":
                    color_name = color_name + ' and white'
            # white and
            elif white_patches in mostly_white:
                color_name = 'white and ' + color_name
            # colorpoint
            elif white_patches in point_markings:
                color_name = color_name + ' point'
                if color_name == 'red point' or color_name == 'ginger point':
                    color_name = 'flame point'
            # vitiligo
            elif white_patches in vit:
                color_name = color_name + ' with vitiligo'
        else:
            color_name = color_name

        if color_name == 'tortie':
            color_name = 'tortoiseshell'

        if white_patches == 'FULLWHITE':
            color_name = 'white'

        if color_name == 'white and white':
            color_name = 'white'

        return color_name

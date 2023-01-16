import random
from .pelts import *
from scripts.cat.sprites import Sprites

# ---------------------------------------------------------------------------- #
#                               utility functions                              #
# ---------------------------------------------------------------------------- #

def plural_acc_names(accessory, plural, singular):
    acc_display = accessory.lower()
    if acc_display == 'maple leaf':
        if plural:
            acc_display = 'maple leaves'
        if singular:
            acc_display = 'maple leaf'
    elif acc_display == 'holly':
        if plural:
            acc_display = 'holly berries'
        if singular:
            acc_display = 'holly berry'
    elif acc_display == 'blue berries':
        if plural:
            acc_display = 'blueberries'
        if singular:
            acc_display = 'blueberry'
    elif acc_display == 'forget me nots':
        if plural:
            acc_display = 'forget me nots'
        if singular:
            acc_display = 'forget me not flower'
    elif acc_display == 'rye stalk':
        if plural:
            acc_display = 'rye stalks'
        if singular:
            acc_display = 'rye stalk'
    elif acc_display == 'laurel' or acc_display == 'laurel leaves':
        if plural:
            acc_display = 'laurel'
        if singular:
            acc_display = 'laurel plant'
    elif acc_display == 'bluebells':
        if plural:
            acc_display = 'bluebells'
        if singular:
            acc_display = 'bluebell flower'
    elif acc_display == 'nettle':
        if plural:
            acc_display = 'nettles'
        if singular:
            acc_display = 'nettle'
    elif acc_display == 'poppy' or acc_display == 'poppy flower':
        if plural:
            acc_display = 'poppies'
        if singular:
            acc_display = 'poppy flower'
    elif acc_display == 'lavender' or acc_display == 'lavender flower':
        if plural:
            acc_display = 'lavender'
        if singular:
            acc_display = 'lavender flower'
    elif acc_display == 'herbs':
        if plural:
            acc_display = 'herbs'
        if singular:
            acc_display = 'herb'
    elif acc_display == 'petals':
        if plural:
            acc_display = 'petals'
        if singular:
            acc_display = 'petal'
    elif acc_display == 'dry herbs':
        if plural:
            acc_display = 'dry herbs'
        if singular:
            acc_display = 'dry herb'
    elif acc_display == 'oak leaves' or acc_display == 'oak leaf':
        if plural:
            acc_display = 'oak leaves'
        if singular:
            acc_display = 'oak leaf'
    elif acc_display == 'catmint':
        if plural:
            acc_display = 'catnip'
        if singular:
            acc_display = 'catnip sprig'
    elif acc_display == 'maple seed':
        if plural:
            acc_display = 'maple seeds'
        if singular:
            acc_display = 'maple seed'
    elif acc_display == 'juniper' or acc_display == 'juniper berries':
        if plural:
            acc_display = 'juniper berries'
        if singular:
            acc_display = 'juniper berry'
    elif acc_display == 'red feathers':
        if plural:
            acc_display = 'cardinal feathers'
        if singular:
            acc_display = 'cardinal feather'
    elif acc_display == 'blue feathers':
        if plural:
            acc_display = 'crow feathers'
        if singular:
            acc_display = 'crow feather'
    elif acc_display == 'jay feathers':
        if plural:
            acc_display = 'jay feathers'
        if singular:
            acc_display = 'jay feather'
    elif acc_display == 'moth wings':
        if plural:
            acc_display = 'moth wings'
        if singular:
            acc_display = 'moth wing'
    elif acc_display == 'cicada wings':
        if plural:
            acc_display = 'cicada wings'
        if singular:
            acc_display = 'cicada wing'
    elif acc_display == 'beech leaf':
        if plural:
            acc_display = 'beech leaves'
        if singular:
            acc_display = 'beech leaf'
    elif acc_display == 'borage flower':
        if plural:
            acc_display = 'borage flowers'
        if singular:
            acc_display = 'borage flower'
    elif acc_display == 'coltsfoot flower':
        if plural:
            acc_display = 'coltsfoot flowers'
        if singular:
            acc_display = 'coltsfoot flower'
    elif acc_display == 'tormentil flower':
        if plural:
            acc_display = 'tormentil flowers'
        if singular:
            acc_display = 'tormentil flower'
    elif acc_display == 'yarrow clump':
        if plural:
            acc_display = 'yarrow flowers'
        if singular:
            acc_display = 'yarrow clump'
    elif acc_display == 'daisy flower':
        if plural:
            acc_display = 'daisy flowers'
        if singular:
            acc_display = 'daisy flower'
    elif acc_display == 'bindweed vine':
        if plural:
            acc_display = 'bindweed vines'
        if singular:
            acc_display = 'bindweed vine'
    elif acc_display == 'bright-eye flower':
        if plural:
            acc_display = 'bright-eye flowers'
        if singular:
            acc_display = 'bright-eye flower'

    if plural is True and singular is False:
        return acc_display
    elif singular is True and plural is False:
        return acc_display

# ---------------------------------------------------------------------------- #
#                                init functions                                #
# ---------------------------------------------------------------------------- #

def init_eyes(cat):
    if cat.eye_colour is not None:
        return
    hit = randint(0, 250)
    if hit == 1:
        cat.eye_colour = choice(["BLUEYELLOW", "BLUEGREEN", "GREENGOLD", "PINKBLUE"])
    else:
        if cat.parent1 is None:
            cat.eye_colour = choice(eye_colours)
        elif cat.parent2 is None:
            par1 = cat.all_cats[cat.parent1]
            cat.eye_colour = choice(
                [par1.eye_colour, choice(eye_colours)])
        else:
            par1 = cat.all_cats[cat.parent1]
            par2 = cat.all_cats[cat.parent2]
            cat.eye_colour = choice([
                par1.eye_colour, par2.eye_colour,
                choice(eye_colours)
            ])

def init_pelt(cat):
    if cat.pelt != None:
        return

    if cat.parent2 is None and cat.parent1 in cat.all_cats.keys():
        # 1 in 3 chance to inherit a single parent's pelt
        par1 = cat.all_cats[cat.parent1]
        cat.pelt = choose_pelt(cat.gender, choice([par1.pelt.colour, None]), choice([par1.pelt.white, None]), choice([par1.pelt.name, None]),
                                choice([par1.pelt.length, None]))
    if cat.parent1 in cat.all_cats.keys() and cat.parent2 in cat.all_cats.keys():
        # 2 in 3 chance to inherit either parent's pelt
        par1 = cat.all_cats[cat.parent1]
        par2 = cat.all_cats[cat.parent2]
        cat.pelt = choose_pelt(cat.gender, choice([par1.pelt.colour, par2.pelt.colour, None]), choice([par1.pelt.white, par2.pelt.white, None]),
                                choice([par1.pelt.name, par2.pelt.name, None]), choice([par1.pelt.length, par2.pelt.length, None]))                  
    else:
        cat.pelt = choose_pelt(cat.gender)
    if cat.pelt.name in ['Pinstripe', 'Clouded', 'Merle', 'Abyssinian', 'Ghost', 'Snowflake',
                         'Doberman', 'Spotted', 'Classic', 'Mackerel', 'Sokoke', 'Gradient', 'Siamese']:
            cat.pelt.colour = choice(["WHITE", "PALEGREY", "SILVER", "GREY", "DARKGREY", "BLACK",
                                      "PALEGINGER", "GOLDEN", "GINGER", "DARKGINGER", "LIGHTBROWN",
                                      "BROWN", "DARKBROWN"])
    if cat.pelt.name in ['Cloudy', 'Ragdoll', 'Shaded']:
            cat.pelt.colour = choice(["WHITE", "PALEGREY", "SILVER", "GREY", "DARKGREY", "BLACK",
                                      "PALEGINGER", "GOLDEN", "GINGER", "DARKGINGER", "LIGHTBROWN",
                                      "BROWN", "DARKBROWN", "CREAM"])
    if cat.pelt.name in ['Single', 'Bengal', 'Marbled', 'Speckled', 'Tabby', 'Ticked']:
            cat.pelt.colour = choice(["BLACK", "DARKBROWN", "DARKGREY", "BROWN", "SILVER", "GREY", "LIGHTBROWN",
                                  "WHITE", "PALEGREY", "PALEGINGER", "GINGER", "DARKGINGER", "GOLDEN", "WHITE2",
                                  "BLUE", "CARAMEL", "LILAC", "DARK", "BLACK2", "PALE", "APRICOT", "CREAM",
                                  "ORANGE", "FAWN", "CINNAMON", "CHOCOLATE", "CREAM2", "LIGHTPINK", "PINK",
                                  "DARKPINK", "LIGHTBG", "BG", "DARKBG", "CREAM3", "PALEGINGER2", "GINGER2",
                                  "DARKGINGER2", "LIGHTGB", "GB", "DARKGB", "LIGHTGREEN", "GREEN", "DARKGREEN",
                                  "LIGHTPURPLE", "PURPLE", "DARKPURPLE", "SNOW", "LIGHTGREY2", "GREY2",
                                  "DARKGREY2", "BLACK2", "EBONY", "PALEYELLOW", "YELLOW", "GOLD", "DARKCREAM",
                                  "LIGHTGB2", "GB2", "DARKGB2", "LIGHTBROWN2", "BROWN2", "DARKBROWN2",
                                  'WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE', 'COAL', 'OBSIDIAN',
                                  'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2', 'FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3',
                                  'CHOCOLATE', 'DARKBROWN3', 'EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE',
                                  'DARKGINGER3', 'RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2', 'DARKLILAC',
                                  'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY', 'LIGHTSILVER', 'SILVER2', 'DARKSILVER',
                                  'PALEBLUE', 'LIGHTBLUE', 'BLUE1', 'RUSSIAN', 'DARKBLUE'])
    if cat.pelt.name in ['Smoke', 'Rosette']:
        cat.pelt.colour = choice(["BLACK", "DARKBROWN", "DARKGREY", "BROWN", "SILVER", "GREY", "LIGHTBROWN",
                                  "WHITE", "PALEGREY", "PALEGINGER", "GINGER", "DARKGINGER", "GOLDEN", "WHITE2",
                                  "BLUE", "CARAMEL", "LILAC", "DARK", "BLACK2", "PALE", "APRICOT", "CREAM",
                                  "ORANGE", "FAWN", "CINNAMON", "CHOCOLATE", "CREAM2",
                                  'WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE', 'COAL', 'OBSIDIAN',
                                  'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2', 'FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3',
                                  'CHOCOLATE', 'DARKBROWN3', 'EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE',
                                  'DARKGINGER3', 'RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2', 'DARKLILAC',
                                  'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY', 'LIGHTSILVER', 'SILVER2', 'DARKSILVER',
                                  'PALEBLUE', 'LIGHTBLUE', 'BLUE1', 'RUSSIAN', 'DARKBLUE'])

    if cat.pelt.name in ['DarkTabby', "DilutedTabby", "DilutedTabby", "Tonkinese", "DilutedTonkinese",
    "DilutedBengal", "DilutedSpeckled", "DilutedMarbled", "Freckled", "DilutedFreckled", "Somali", "DilutedTicked", 
    "DilutedRosette", "DilutedClassic", "DilutedSokoke", "DilutedMackerel", "DarkMackerel", "DarkSpeckled", "DarkSokoke",
    "DarkRosette", "DarkClassic", "DarkMarbled", "DarkBengal"]:
        cat.pelt.colour = choice(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE', 'COAL', 'OBSIDIAN',
                                  'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2', 'FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3',
                                  'CHOCOLATE2', 'DARKBROWN3', 'EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE',
                                  'DARKGINGER3', 'RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2', 'DARKLILAC',
                                  'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY', 'LIGHTSILVER', 'SILVER2', 'DARKSILVER',
                                  'PALEBLUE', 'LIGHTBLUE', 'BLUE1', 'RUSSIAN', 'DARKBLUE'])

def init_sprite(cat):
    if cat.pelt is None:
        init_pelt(cat)
    cat.age_sprites = {
        'kitten': randint(0, 2),
        'adolescent': randint(3, 5),
        'elder': randint(3, 5)
    }
    cat.reverse = choice([True, False])
    hit = randint(0, 200)
    if hit == 1:
        cat.skin = choice(["ALBINOPINK", "ALBINOBLUE", "ALBINORED", "ALBINOVIOLET", "MELANISTICLIGHT", "MELANISTIC", "MELANISTICDARK"])
    else:
        if cat.parent1 is None:
            cat.skin = choice(skin_sprites)
        elif cat.parent2 is None:
            par1 = cat.all_cats[cat.parent1]
            cat.skin = choice(
                [par1.skin, choice(skin_sprites)])
        else:
            par1 = cat.all_cats[cat.parent1]
            par2 = cat.all_cats[cat.parent2]
            cat.skin = choice([
                par1.skin, par2.skin,
                choice(skin_sprites)
            ])
            
    if cat.pelt is not None:
        if cat.pelt.length != 'long':
            cat.age_sprites['adult'] = randint(6, 8)
        else:
            cat.age_sprites['adult'] = randint(0, 2)
        cat.age_sprites['young adult'] = cat.age_sprites['adult']
        cat.age_sprites['senior adult'] = cat.age_sprites['adult']
        cat.age_sprites['dead'] = None

def init_scars(cat):
    scar_choice = randint(0, 15)
    if cat.age in ['kitten', 'adolescent']:
        scar_choice = randint(0, 50)
    elif cat.age in ['young adult', 'adult']:
        scar_choice = randint(0, 20)
    if scar_choice == 1:
        cat.specialty = choice([
            choice(scars1),
            choice(scars2),
            choice(scars3)
        ])
    else:
        cat.specialty = None
        
    scar_choice2 = randint(0, 30)
    if cat.age in ['kitten', 'adolescent']:
        scar_choice2 = randint(0, 100)
    elif cat.age in ['young adult', 'adult']:
        scar_choice2 = randint(0, 40)
    if scar_choice2 == 1:
        cat.specialty2 = choice([
            choice(scars1),
            choice(scars2),
            choice(scars3)
        ])
    else:
        cat.specialty2 = None
    if cat.specialty2 == 'NOTAIL':
        if cat.specialty == 'HALFTAIL':
            cat.specialty = None

def init_accessories(cat):
    acc_display_choice = randint(0, 35)
    if cat.age in ['kitten', 'adolescent']:
        acc_display_choice = randint(0, 15)
    elif cat.age in ['young adult', 'adult']:    
        acc_display_choice = randint(0, 50)
    if acc_display_choice == 1:
        cat.acc_display = choice([
            choice(plant_accessories),
            choice(wild_accessories)
        ])
    else:
        cat.acc_display = None

def init_pattern(cat):
    if cat.pelt == None:
        init_pelt(cat)
    if cat.pelt.name in ['Calico', 'Tortie']:
        cat.tortiecolour = cat.pelt.colour
        cat.tortiebase = choice(['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled',
                                 'pinstripe', 'doberman', 'ghost', 'clouded', 'merle', 'abyssinian', 'snowflake',
                                 'spotted', 'cloudy', 'classic', 'mackerel', 'sokoke', 'gradient', 'siamese',
                                 'ragdoll', 'shaded', 'dilutedtabby', 'dilutedbengal', 'dilutedmarbled', 'dilutedticked',
                                 'somali', 'dilutedrosette', 'dilutedspeckled', 'dilutedclassic', 'dilutedsokoke',
                                 'freckled', 'dilutedfreckled', 'dilutedmackerel', 'tonkinese', 'dilutedtonkinese'])
        cat.tortiepattern = choice(['tortietabby', 'tortiebengal', 'tortiemarbled', 'tortieticked', 'tortiesmoke',
                                    'tortierosette', 'tortiespeckled', 'tortiepinstripe', 'tortieghost', 'tortieclouded',
                                    'tortiemerle', 'tortiesnowflake', 'tortieclassic', 'tortiemackerel', 'tortiesokoke',
                                    'tortiefreckled', 'tortiedilutedfreckled', 'tortietonkinese', 'tortiedilutedtonkinese',
                                    'tortiedilutedsokoke', 'tortiedilutedmackerel', 'tortiedilutedclassic', 'tortiedilutedspeckled',
                                    'tortiesomali', 'tortiedilutedrosette', 'tortiedilutedticked', 'tortiedilutedtabby',
                                    'tortiedilutedbengal', 'tortiedilutedmarbled'])
    else:
        cat.tortiecolour = None
        cat.tortiebase = None
        cat.tortiepattern = None
    if cat.pelt.name in ['Calico', 'Tortie'] and cat.pelt.colour != None:
        if cat.pelt.colour in ["BLACK", "DARKBROWN", "BLACK2", "CHOCOLATE", "DARK", "DARKBG", "DARKGB", "DARKGB2", "BLACK3", "EBONY"]:
                cat.pattern = choice(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO',
                                      'GINGERTHREE', 'GINGERFOUR',
                                      'DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR', 'ORANGEONE', 'ORANGETWO',
                                      'ORANGETHREE', 'ORANGEFOUR'])
        elif cat.pelt.colour in ["DARKGREY", "BROWN", "BLUE", "CINNAMON", "DARKPURPLE", "DARKBROWN2", "BROWN2", "DARKGREY2", "GREY2"]:
            cat.pattern = choice(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE',
                                  'GINGERFOUR',
                                  'ORANGEONE', 'ORANGETWO', 'ORANGETHREE', 'ORANGEFOUR', 'APRICOTONE', 'APRICOTTWO',
                                  'APRICOTTHREE', 'APRICOTFOUR'])
        elif cat.pelt.colour in ["SILVER", "GREY", "LIGHTBROWN", "LILAC", "FAWN", "CARAMEL", "GREY2", "DARKPURPLE"]:
            cat.pattern = choice(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'PALEONE2', 'PALETWO2', 'PALETHREE2',
                                  'PALEFOUR2',
                                  'CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR', 'CREAMONE2', 'CREAMTWO2',
                                  'CREAMTHREE2', 'CREAMFOUR2', 'APRICOTONE', 'APRICOTTWO', 'APRICOTTHREE',
                                  'APRICOTFOUR'])
    if cat.tortiepattern in ['tortiepinstripe', 'tortieghost', 'tortieclouded', 'tortiemerle', 'tortiesnowflake', 'tortieclassic', 'tortiesokoke', 'tortiemackerel']:
        cat.pattern = choice(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR', 'GINGERONE', 'GINGERTWO', 'GINGERTHREE',
                              'GINGERFOUR', 'PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR', 'DARKONE', 'DARKTWO',
                              'DARKTHREE', 'DARKFOUR'])
    if cat.pelt in ['pinstripe', 'doberman', 'ghost', 'clouded', 'merle', 'abyssinian', 'snowflake', 'spotted',
                    'classic', 'sokoke', 'mackerel', 'gradient', 'siamese']:
        cat.pelt.colour = choice(["BLACK", "DARKBROWN", "DARKGREY", "BROWN", "SILVER", "GREY", "LIGHTBROWN",
                                  "WHITE", "PALEGREY", "PALEGINGER", "GINGER", "DARKGINGER", "GOLDEN"])
    if cat.pelt in ['cloudy', 'ragdoll', 'freckled', 'somali', 'dilutedtabby', 'dilutedbengal', 'dilutedmarbled',
                                 'dilutedticked', 'somali', 'dilutedrosette', 'dilutedspeckled', 'dilutedclassic', 'dilutedsokoke',
                                 'freckled', 'dilutedfreckled', 'dilutedmackerel', 'tonkinese', 'dilutedtonkinese']:
        cat.pelt.colour = choice(["BLACK", "DARKBROWN", "DARKGREY", "BROWN", "SILVER", "GREY", "LIGHTBROWN",
                                  "WHITE", "PALEGREY", "PALEGINGER", "GINGER", "DARKGINGER", "GOLDEN", "CREAM"])
    if cat.pelt.name in ['Calico', 'Tortie'] and cat.tortiebase in ['pinstripe', 'doberman', 'ghost', 'clouded',
                                                                    'merle', 'abyssinian', 'snowflake', 'spotted',
                                                                    'cloudy', 'sokoke', 'classic', 'gradient',
                                                                    'mackerel', 'siamese', 'ragdoll', 'shaded']:
        cat.tortiecolour = choice(["BLACK", "DARKBROWN", "DARKGREY", "BROWN", "SILVER", "GREY", "LIGHTBROWN"])
    if cat.pelt in ['smoke', 'rosette']:
        cat.pelt.colour = choice(["BLACK", "DARKBROWN", "DARKGREY", "BROWN", "SILVER", "GREY", "LIGHTBROWN",
                                  "WHITE", "PALEGREY", "PALEGINGER", "GINGER", "DARKGINGER", "GOLDEN", "WHITE2",
                                  "BLUE", "CARAMEL", "LILAC", "DARK", "BLACK2", "PALE", "APRICOT", "CREAM",
                                  "ORANGE", "FAWN", "CINNAMON", "CHOCOLATE", "CREAM2", 'WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE', 'COAL', 'OBSIDIAN',
    'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2', 'FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3',
    'CHOCOLATE', 'DARKBROWN3', 'EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE',
    'DARKGINGER3', 'RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2', 'DARKLILAC',
    'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY', 'LIGHTSILVER', 'SILVER2', 'DARKSILVER',
    'PALEBLUE', 'LIGHTBLUE', 'BLUE1', 'RUSSIAN', 'DARKBLUE'])
    if cat.pelt in ['single', 'bengal', 'marbled', 'speckled', 'tabby', 'ticked']:
        cat.pelt.colour = choice(["BLACK", "DARKBROWN", "DARKGREY", "BROWN", "SILVER", "GREY", "LIGHTBROWN",
                                  "WHITE", "PALEGREY", "PALEGINGER", "GINGER", "DARKGINGER", "GOLDEN", "WHITE2",
                                  "BLUE", "CARAMEL", "LILAC", "DARK", "BLACK2", "PALE", "APRICOT", "CREAM",
                                  "ORANGE", "FAWN", "CINNAMON", "CHOCOLATE", "CREAM2", "LIGHTPINK", "PINK",
                                  "DARKPINK", "LIGHTBG", "BG", "DARKBG", "CREAM3", "PALEGINGER2", "GINGER2",
                                  "DARKGINGER2", "LIGHTGB", "GB", "DARKGB", "LIGHTGREEN", "GREEN", "DARKGREEN",
                                  "LIGHTPURPLE", "PURPLE", "DARKPURPLE", "SNOW", "LIGHTGREY2", "GREY2",
                                  "DARKGREY2", "BLACK2", "EBONY", "PALEYELLOW", "YELLOW", "GOLD", "DARKCREAM",
                                  "LIGHTGB2", "GB2", "DARKGB2", "LIGHTBROWN2", "BROWN2", "DARKBROWN2",
                                  'WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE', 'COAL', 'OBSIDIAN',
    'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2', 'FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3',
    'CHOCOLATE', 'DARKBROWN3', 'EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE',
    'DARKGINGER3', 'RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2', 'DARKLILAC',
    'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY', 'LIGHTSILVER', 'SILVER2', 'DARKSILVER',
    'PALEBLUE', 'LIGHTBLUE', 'BLUE1', 'RUSSIAN', 'DARKBLUE'])
    if cat.pelt.name in ['Calico', 'Tortie'] and cat.tortiebase in ['smoke', 'rosette']:
        cat.tortiecolour = choice(["SILVER", "GREY", "DARKGREY", "BLACK",
                                  "LIGHTBROWN", "BROWN", "DARKBROWN",
                                  "BLACK2", "DARK", "CHOCOLATE", "FAWN",
                                  "LILAC", "BLUE", "CINNAMON", "CARAMEL"])
    if cat.pelt.name in ['Calico', 'Tortie'] and cat.tortiebase in ['single', 'bengal', 'marbled', 'speckled', 'tabby', 'ticked']:
        cat.tortiecolour = choice(["SILVER", "GREY", "DARKGREY", "BLACK", "LIGHTBROWN", "BROWN", "DARKBROWN", "BLUE",
                                  "LILAC", "BLACK2", "DARK", "FAWN", "CINNAMON", "CARAMEL", "CHOCOLATE", "DARKBG",
                                  "DARKGB", "DARKPURPLE", "DARKGREY2", "GREY2", "BLACK3", "EBONY", "DARKGB2",
                                  "BROWN2", "DARKBROWN2"])
        
    if cat.pelt in ['Freckled', 'Tonkinese', 'DilutedTabby', 'DilutedSpeckled', 
    'DilutedMarbled', 'DilutedBengal', 'DilutedTicked', 'Somali', 'DilutedRosette', 'DilutedClassic', 'DilutedMackerel', 'DilutedFreckled', 'DilutedTonkinese', 'DilutedSokoke', 'DarkTabby',
    'DarkMarbled', 'DarkSpeckled', 'DarkBengal', 'DarkClassic', 'DarkMackerel', 'DarkSokoke', 'DarkRosette']:
        cat.pelt.colour = choice(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE', 'COAL', 'OBSIDIAN',
    'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2', 'FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3',
    'CHOCOLATE2', 'DARKBROWN3', 'EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE',
    'DARKGINGER3', 'RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2', 'DARKLILAC',
    'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY', 'LIGHTSILVER', 'SILVER2', 'DARKSILVER',
    'PALEBLUE', 'LIGHTBLUE', 'BLUE1', 'RUSSIAN', 'DARKBLUE'])

def init_white_patches(cat):
    if cat.pelt is None:
        init_pelt(cat)
    non_white_pelt = False
    if cat.pelt.colour != 'WHITE' and cat.pelt.name in\
    ['Tortie', 'TwoColour', 'Tabby', 'Speckled', 'Marbled',
     'Bengal', 'Ticked', 'Smoke', 'Rosette', 'Merle', 'Clouded',
     'Snowflake', 'Abyssinian', 'Doberman', 'Ghost', 'Pinstripe',
     'Spotted', 'Cloudy', 'Classic', 'Mackerel', 'Sokoke',
     'Gradient', 'Siamese', 'Ragdoll', 'Shaded',
     'Freckled', 'Tonkinese', 'DilutedTabby', 'DilutedSpeckled',  'DilutedMarbled',
     'DilutedBengal', 'DilutedTicked', 'Somali', 'DilutedRosette', 'DilutedClassic', 'DilutedMackerel',
     'DilutedFreckled', 'DilutedTonkinese', 'DilutedSokoke', 'DarkTabby', 'DarkMarbled', 'DarkSpeckled',
     'DarkBengal', 'DarkClassic', 'DarkMackerel', 'DarkSokoke', 'DarkRosette']:
        non_white_pelt = True
    little_white_poss = little_white * 6
    mid_white_poss = mid_white * 4
    high_white_poss = high_white * 2
    mostly_white_poss = mostly_white
    if cat.pelt.white is True:
        pelt_choice = randint(0, 10)
        vit_chance = randint(0, 40)
        direct_inherit = randint(0, 10)
        # inheritance
        # one parent
        if cat.parent1 is not None and cat.parent2 is None and cat.parent1 in cat.all_cats:
            par1 = cat.all_cats[cat.parent1]
            if direct_inherit == 1:
                if par1.pelt.white is False:
                    cat.pelt.white = False
                else:
                    cat.white_patches = par1.white_patches
            elif vit_chance == 1:
                cat.white_patches = choice(vit)
            else:
                if par1.white_patches in point_markings and non_white_pelt is True:
                    cat.white_patches = choice(point_markings)
                elif par1.white_patches in vit:
                    cat.white_patches = choice(vit)
                elif par1.white_patches in [None] + little_white + mid_white + high_white:
                    cat.white_patches = choice([None] + little_white_poss + mid_white_poss + high_white_poss + mostly_white_poss)
                elif par1.white_patches in mostly_white:
                    cat.white_patches = choice(mid_white + high_white + mostly_white + ['FULLWHITE'])
            if par1.white_patches is None and cat.pelt.name == 'Calico':
                cat.pelt.name = 'Tortie'
            # two parents
        elif cat.parent1 is not None and cat.parent2 is not None and\
            cat.parent1 in cat.all_cats and cat.parent2 in cat.all_cats:
            # if 1, cat directly inherits parent 1's white patches. if 2, it directly inherits parent 2's
            par1 = cat.all_cats[cat.parent1]
            par2 = cat.all_cats[cat.parent2]
            if direct_inherit == 1:
                if par1.pelt.white is False:
                    cat.pelt.white = False
                else:
                    cat.white_patches = par1.white_patches
            elif direct_inherit == 2:
                if par2.pelt.white is False:
                    cat.pelt.white = False
                else:
                    cat.white_patches = par2.white_patches
            elif vit_chance == 1:
                cat.white_patches = choice(vit)
            else:
                if par1.white_patches in point_markings and non_white_pelt is True\
                or par2.white_patches in point_markings and non_white_pelt is True:
                    cat.white_patches = choice(point_markings)
                elif par1.white_patches in vit and non_white_pelt is True\
                or par2.white_patches in vit and non_white_pelt is True:
                    cat.white_patches = choice(vit)
                elif par1.white_patches is None:
                    if par2.white_patches is None:
                        cat.white_patches = None
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white_poss + [None])
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(little_white_poss + mid_white_poss)
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(little_white + mid_white_poss * 2 + high_white)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss + mostly_white)
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(little_white_poss + mid_white_poss + high_white_poss + mostly_white_poss + ['FULLWHITE'])
                    else:
                        cat.white_patches = choice(little_white)
                elif par1.white_patches in little_white:
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + [None])
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white_poss * 2 + mid_white_poss + [None])
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(little_white_poss + mid_white_poss + high_white)
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(little_white + mid_white_poss * 2 + high_white_poss + mostly_white)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(mid_white + high_white_poss + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(high_white_poss + mostly_white_poss + ['FULLWHITE'])
                    else:
                        cat.white_patches = choice(little_white)
                elif par1.white_patches in mid_white:
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + mid_white + [None])
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white_poss + mid_white_poss + high_white)
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(little_white + mid_white_poss * 3 + high_white)
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss * 3 + mostly_white)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(mid_white + high_white_poss * 2 + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(high_white_poss + mostly_white_poss + ['FULLWHITE'])
                    else:
                        cat.white_patches = choice(mid_white)
                elif par1.white_patches in high_white:
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + mid_white_poss + high_white + [None])
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white_poss + mid_white_poss + high_white)
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(little_white + mid_white_poss + high_white_poss)
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss * 2 + mostly_white)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(mid_white + high_white_poss + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(high_white_poss + mostly_white_poss + ['FULLWHITE'])
                    else:
                        cat.white_patches = choice(high_white)
                elif par1.white_patches in mostly_white:
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + mid_white + high_white + mostly_white)
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(little_white + mid_white_poss + high_white_poss + mostly_white)
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(high_white_poss + mostly_white + mostly_white + mostly_white + ['FULLWHITE'])
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(high_white + mostly_white * 4 + ['FULLWHITE'])
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(mostly_white * 5 + ['FULLWHITE', 'FULLWHITE', 'FULLWHITE'])
                    else:
                        cat.white_patches = choice(mostly_white)
                elif par1.white_patches == 'FULLWHITE':
                    if par2.white_patches is None:
                        cat.white_patches = choice(little_white + mid_white + high_white + mostly_white + [None] + ['FULLWHITE'])
                    elif par2.white_patches in little_white:
                        cat.white_patches = choice(mid_white_poss + high_white_poss * 2 + mostly_white * 2)
                    elif par2.white_patches in mid_white:
                        cat.white_patches = choice(mid_white + high_white_poss * 3 + mostly_white * 3 + ['FULLWHITE'])
                    elif par2.white_patches in high_white:
                        cat.white_patches = choice(high_white_poss + mostly_white * 4 + ['FULLWHITE'] * 3)
                    elif par2.white_patches in mostly_white:
                        cat.white_patches = choice(high_white + mostly_white * 4 + ['FULLWHITE'] * 4)
                    elif par2.white_patches == 'FULLWHITE':
                        cat.white_patches = choice(mostly_white + ['FULLWHITE'] * 6)
                    else:
                        cat.white_patches = choice(mostly_white)
            if cat.pelt.name == 'Calico' and par1.white_patches not in mid_white + high_white + mostly_white\
            and par2.white_patches not in mid_white + high_white + mostly_white:
                cat.pelt.name = 'Tortie'
                
        # regular non-inheritance white patches generation
        else:
            if pelt_choice == 1 and non_white_pelt is True:
                cat.white_patches = choice(point_markings)
            elif pelt_choice == 1 and cat.pelt.name == 'TwoColour' and cat.pelt.colour != 'WHITE':
                cat.white_patches = choice(point_markings + ['POINTMARK'])
            elif pelt_choice == 2 and cat.pelt.name in ['Calico', 'TwoColour', 'Tabby', 'Speckled',
                                                        'Marbled', 'Bengal', 'Ticked', 'Smoke',
                                                        'Rosette', 'Merle', 'Clouded', 'Snowflake',
                                                        'Abyssinian', 'Doberman', 'Ghost', 'Pinstripe',
                                                        'Spotted', 'Cloudy', 'Classic', 'Mackerel',
                                                        'Sokoke', 'Gradient', 'Siamese', 'Ragdoll', 'Shaded',
                                                        'Freckled', 'Tonkinese', 'DilutedTabby', 'DilutedSpeckled',  'DilutedMarbled',
     'DilutedBengal', 'DilutedTicked', 'Somali', 'DilutedRosette', 'DilutedClassic', 'DilutedMackerel',
     'DilutedFreckled', 'DilutedTonkinese', 'DilutedSokoke', 'DarkTabby', 'DarkMarbled', 'DarkSpeckled',
     'DarkBengal', 'DarkClassic', 'DarkMackerel', 'DarkSokoke', 'DarkRosette']:
                cat.white_patches = choice(mostly_white_poss)
            elif pelt_choice == 3 and cat.pelt.name in ['TwoColour', 'Tabby', 'Speckled', 'Marbled',
                                                        'Bengal', 'Ticked', 'Smoke', 'Rosette', 'Merle',
                                                        'Clouded', 'Snowflake', 'Abyssinian', 'Doberman',
                                                        'Ghost', 'Pinstripe', 'Spotted', 'Cloudy',
                                                        'Classic', 'Mackerel', 'Sokoke', 'Gradient',
                                                        'Siamese', 'Ragdoll', 'Shaded',
                                                        'Freckled', 'Tonkinese', 'DilutedTabby', 'DilutedSpeckled',  'DilutedMarbled',
     'DilutedBengal', 'DilutedTicked', 'Somali', 'DilutedRosette', 'DilutedClassic', 'DilutedMackerel',
     'DilutedFreckled', 'DilutedTonkinese', 'DilutedSokoke', 'DarkTabby', 'DarkMarbled', 'DarkSpeckled',
     'DarkBengal', 'DarkClassic', 'DarkMackerel', 'DarkSokoke', 'DarkRosette']\
            and cat.pelt.colour != 'WHITE':
                cat.white_patches = choice(['EXTRA', None, 'FULLWHITE'])
            else:
                if cat.pelt.name in ['TwoColour', 'Tabby', 'Speckled', 'Marbled', 'Bengal', 'Ticked',
                                     'Smoke', 'Rosette', 'Merle', 'Clouded', 'Snowflake', 'Abyssinian',
                                     'Doberman', 'Ghost', 'Pinstripe', 'Spotted', 'Cloudy', 'Classic',
                                     'Mackerel', 'Sokoke', 'Gradient', 'Siamese', 'Ragdoll', 'Shaded',
                                     'Freckled', 'Tonkinese', 'DilutedTabby', 'DilutedSpeckled',  'DilutedMarbled',
     'DilutedBengal', 'DilutedTicked', 'Somali', 'DilutedRosette', 'DilutedClassic', 'DilutedMackerel',
     'DilutedFreckled', 'DilutedTonkinese', 'DilutedSokoke', 'DarkTabby', 'DarkMarbled', 'DarkSpeckled',
     'DarkBengal', 'DarkClassic', 'DarkMackerel', 'DarkSokoke', 'DarkRosette']:
                    cat.white_patches = choice(little_white_poss + mid_white_poss + high_white_poss)
                elif cat.pelt.name in ['Tortie']:
                    cat.white_patches = choice(little_white_poss + mid_white_poss)
                elif cat.pelt.name in ['Calico']:
                    cat.white_patches = choice(high_white_poss)
                elif pelt_choice == 1 and vit_chance == 1 and cat.pelt.name in ['Tortie', 'TwoColour',
                                                                                'Tabby', 'Speckled',
                                                                                'Marbled', 'Bengal',
                                                                                'Ticked', 'Smoke',
                                                                                'Rosette', 'Merle',
                                                                                'Clouded', 'Snowflake',
                                                                                'Abyssinian', 'Doberman',
                                                                                'Ghost', 'Pinstripe',
                                                                                'Spotted', 'Cloudy',
                                                                                'Classic', 'Mackerel',
                                                                                'Sokoke', 'Gradient',
                                                                                'Siamese', 'Ragdoll',
                                                                                'Shaded', 'Freckled', 'Tonkinese', 'DilutedTabby', 'DilutedSpeckled',  'DilutedMarbled',
     'DilutedBengal', 'DilutedTicked', 'Somali', 'DilutedRosette', 'DilutedClassic', 'DilutedMackerel',
     'DilutedFreckled', 'DilutedTonkinese', 'DilutedSokoke', 'DarkTabby', 'DarkMarbled', 'DarkSpeckled',
     'DarkBengal', 'DarkClassic', 'DarkMackerel', 'DarkSokoke', 'DarkRosette']\
                and cat.pelt.colour != 'WHITE':
                    cat.white_patches = choice(vit)
                else:
                    cat.white_patches = None
        # just making sure no cats end up with no white patches and true white            
        if cat.white_patches is None:
            cat.white = False
    else:
        cat.white_patches = None
        cat.white = False

def init_tint(cat):
    # Basic tints as possible for all colors.
    possible_tints = Sprites.cat_tints["possible_tints"]["basic"].copy()
    if cat.pelt.colour in Sprites.cat_tints["colour_groups"]:
        color_group = Sprites.cat_tints["colour_groups"][cat.pelt.colour]
        possible_tints += Sprites.cat_tints["possible_tints"][color_group]
        cat.tint = choice(possible_tints)


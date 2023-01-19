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
    elif acc_display == 'laurel':
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
    elif acc_display == 'poppy':
        if plural:
            acc_display = 'poppies'
        if singular:
            acc_display = 'poppy flower'
    elif acc_display == 'lavender':
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
    elif acc_display == 'oak leaves':
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
    elif acc_display == 'juniper':
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
    hit = randint(0, 200)
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
                                  "WHITE3", "PALEGREY2", "LIGHTGREY3", "GREY3", "DARKGREY3", "STONE", "COAL", "OBSIDIAN",
                                  "BLACK4", "PALECREAM", "CREAM4", "DARKCREAM2", "FAWN2", "TAN", "LIGHTBROWN3", "BROWN3",
                                  "CHOCOLATE", "DARKBROWN3", "EBONY1", "PALEGINGER3", "LIGHTGINGER3", "GINGER3", "FIRE",
                                  "DARKGINGER3", "RUSSET", "RED", "AUBURN", "PALELILAC", "LIGHTLILAC", "LILAC2", "DARKLILAC",
                                  "ROSE", "LIGHTGOLD", "GOLDEN2", "DARKGOLD", "HONEY", "LIGHTSILVER", "SILVER2", "DARKSILVER",
                                  "PALEBLUE", "LIGHTBLUE", "BLUE1", "RUSSIAN", "DARKBLUE"])
    if cat.pelt.name in ['Smoke', 'Rosette']:
        cat.pelt.colour = choice(["BLACK", "DARKBROWN", "DARKGREY", "BROWN", "SILVER", "GREY", "LIGHTBROWN",
                                  "WHITE", "PALEGREY", "PALEGINGER", "GINGER", "DARKGINGER", "GOLDEN", "WHITE2",
                                  "BLUE", "CARAMEL", "LILAC", "DARK", "BLACK2", "PALE", "APRICOT", "CREAM",
                                  "ORANGE", "FAWN", "CINNAMON", "CHOCOLATE", "CREAM2",
                                  "WHITE3", "PALEGREY2", "LIGHTGREY3", "GREY3", "DARKGREY3", "STONE", "COAL", "OBSIDIAN",
                                  "BLACK4", "PALECREAM", "CREAM4", "DARKCREAM2", "FAWN2", "TAN", "LIGHTBROWN3", "BROWN3",
                                  "CHOCOLATE", "DARKBROWN3", "EBONY1", "PALEGINGER3", "LIGHTGINGER3", "GINGER3", "FIRE",
                                  "DARKGINGER3", "RUSSET", "RED", "AUBURN", "PALELILAC", "LIGHTLILAC", "LILAC2", "DARKLILAC",
                                  "ROSE", "LIGHTGOLD", "GOLDEN2", "DARKGOLD", "HONEY", "LIGHTSILVER", "SILVER2", "DARKSILVER",
                                  "PALEBLUE", "LIGHTBLUE", "BLUE1", "RUSSIAN", "DARKBLUE"])
    if cat.pelt.name in ['DarkTabby', "DilutedTabby", "DilutedTabby", "Tonkinese", "DilutedTonkinese",
                        "DilutedBengal", "DilutedSpeckled", "DilutedMarbled", "Freckled", "DilutedFreckled", "Somali", "DilutedTicked", 
                        "DilutedRosette", "DilutedClassic", "DilutedSokoke", "MackerelDilute", "DarkMackerel", "DarkSpeckled", "DarkSokoke",
                        "DarkRosette", "DarkClassic", "DarkMarbled", "DarkBengal"]:
        cat.pelt.colour = choice(["WHITE3", "PALEGREY2", "LIGHTGREY3", "GREY3", "DARKGREY3", "STONE", "COAL", "OBSIDIAN",
                                  "BLACK4", "PALECREAM", "CREAM4", "DARKCREAM2", "FAWN2", "TAN", "LIGHTBROWN3", "BROWN3",
                                  "CHOCOLATE2", "DARKBROWN3", "EBONY1", "PALEGINGER3", "LIGHTGINGER3", "GINGER3", "FIRE",
                                  "DARKGINGER3", "RUSSET", "RED", "AUBURN", "PALELILAC", "LIGHTLILAC", "LILAC2", "DARKLILAC",
                                  "ROSE", "LIGHTGOLD", "GOLDEN2", "DARKGOLD", "HONEY", "LIGHTSILVER", "SILVER2", "DARKSILVER",
                                  "PALEBLUE", "LIGHTBLUE", "BLUE1", "RUSSIAN", "DARKBLUE"])
    if cat.pelt.name in ['Tortie', 'Calico']:
        cat.pelt.colour = choice(tortiecolours)


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
    if not cat.scars:
        scar_choice = randint(0, 15)
        if cat.age in ['kitten', 'adolescent']:
            scar_choice = randint(0, 50)
        elif cat.age in ['young adult', 'adult']:
            scar_choice = randint(0, 20)
        if scar_choice == 1:
            cat.scars.append(choice([
                choice(scars1),
                choice(scars3)
            ]))

    if 'NOTAIL' in cat.scars and 'HALFTAIL' in cat.scars:
        cat.scars.remove('HALFTAIL')


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
        cat.tortiebase = choice(tortiebases)
        cat.tortiepattern = choice(tortiepatterns)
    if cat.pelt.name in ['Calico', 'Tortie'] and cat.pelt.colour != None:
        if cat.tortiepattern in [
            'tortiepinstripe', 'tortieghost', 'tortieclouded', 'tortiemerle', 'tortiesnowflake', 
            'tortieclassic', 'tortiesokoke', 'tortiemackerel']:
            cat.pattern = choice(basic_patch_colours)
        else:
            cat.pattern = choice(patch_colours)
        if cat.tortiebase in ['pinstripe', 'doberman', 'ghost', 'clouded', 'merle', 'abyssinian', 'snowflake', 'spotted',
                    'classic', 'sokoke', 'mackerel', 'gradient', 'siamese']:
            cat.tortiecolour = choice(basic_c_no_cream)
        if cat.tortiebase in ['cloudy', 'ragdoll', 'shaded']:
            cat.tortiecolour = choice(basic_colours)
        if cat.tortiebase in [
            'freckled', 'somali', 'dilutedtabby', 'dilutedbengal', 'dilutedmarbled',
            'dilutedticked', 'somali', 'dilutedrosette', 'dilutedspeckled', 'dilutedclassic', 'dilutedsokoke',
            'freckled', 'dilutedfreckled', 'dilutedmackerel', 'tonkinese', 'dilutedtonkinese']:
            cat.tortiecolour = choice(dilute_pelt_c)
    
        if cat.tortiebase in ['smoke', 'rosette']:
            cat.tortiecolour = choice(["BLACK", "DARKBROWN", "DARKGREY", "BROWN", "SILVER", "GREY", "LIGHTBROWN",
                "WHITE", "PALEGREY", "PALEGINGER", "GINGER", "DARKGINGER", "GOLDEN", "WHITE2",
                "BLUE", "CARAMEL", "LILAC", "DARK", "BLACK2", "PALE", "APRICOT", "CREAM",
                "ORANGE", "FAWN", "CINNAMON", "CHOCOLATE", "CREAM2", "WHITE3", "PALEGREY2", "LIGHTGREY3", "GREY3", "DARKGREY3", "STONE", "COAL", "OBSIDIAN",
                "BLACK4", "PALECREAM", "CREAM4", "DARKCREAM2", "FAWN2", "TAN", "LIGHTBROWN3", "BROWN3",
                "CHOCOLATE", "DARKBROWN3", "EBONY1", "PALEGINGER3", "LIGHTGINGER3", "GINGER3", "FIRE",
                "DARKGINGER3", "RUSSET", "RED", "AUBURN", "PALELILAC", "LIGHTLILAC", "LILAC2", "DARKLILAC",
                "ROSE", "LIGHTGOLD", "GOLDEN2", "DARKGOLD", "HONEY", "LIGHTSILVER", "SILVER2", "DARKSILVER",
                "PALEBLUE", "LIGHTBLUE", "BLUE1", "RUSSIAN", "DARKBLUE"])
        if cat.tortiepattern in ['single', 'bengal', 'marbled', 'speckled', 'tabby', 'ticked']:
            cat.tortiecolour = choice(tortiecolours)
        
        if cat.tortiebase.casefold() in dilute_pelts:
            cat.pelt.colour = choice(dilute_pelt_c)

    else:
        cat.tortiecolour = None
        cat.tortiebase = None
        cat.tortiepattern = None


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
    if cat.pelt.white is True:
        pelt_choice = randint(0, 10)
        vit_chance = randint(0, 40)
        direct_inherit = randint(0, 10)
        white_patches_choice = None
        white_list = [None, little_white, mid_white, high_white, mostly_white, 'FULLWHITE']
        # inheritance
        # one parent
        if cat.parent1 is not None and cat.parent2 is None and cat.parent1 in cat.all_cats:
            par1 = cat.all_cats[cat.parent1]
            if direct_inherit == 1:
                if par1.pelt.white is False:
                    cat.pelt.white = False
                    cat.white_patches = None
                else:
                    cat.white_patches = par1.white_patches
            elif vit_chance == 1:
                cat.white_patches = choice(vit)
            else:
                if par1.white_patches in point_markings and non_white_pelt:
                    if pelt_choice < 5:
                        cat.white_patches = choice(point_markings)
                    else:
                        cat.white_patches = choice(mid_white)
                elif par1.white_patches in vit:
                    cat.white_patches = choice(vit)
                elif par1.white_patches in [None, little_white, mid_white, high_white]:
                    white_patches_choice = random.choices(white_list, weights=(20, 20, 20, 20, 19, 1))
                elif par1.white_patches in mostly_white:
                    white_patches_choice = random.choices(white_list, weights=(0, 0, 30, 30, 30, 10))
            if par1.white_patches is None and cat.pelt.name == 'Calico':
                cat.pelt.name = 'Tortie'
            # two parents
        elif cat.parent1 and cat.parent2 and\
            cat.parent1 in cat.all_cats and cat.parent2 in cat.all_cats:
            # if 1, cat directly inherits parent 1's white patches. if 2, it directly inherits parent 2's
            par1 = cat.all_cats[cat.parent1]
            par2 = cat.all_cats[cat.parent2]
            if direct_inherit == 1:
                if par1.pelt.white is False:
                    cat.pelt.white = False
                    cat.white_patches = None
                else:
                    cat.white_patches = par1.white_patches
            elif direct_inherit == 2:
                if par2.pelt.white is False:
                    cat.pelt.white = False
                    cat.white_patches = None
                else:
                    cat.white_patches = par2.white_patches
            elif vit_chance == 1:
                cat.white_patches = choice(vit)
            else:
                if par1.white_patches in point_markings and non_white_pelt\
                    or par2.white_patches in point_markings and non_white_pelt:
                    if pelt_choice < 5:
                        cat.white_patches = choice(point_markings)
                    else:
                        cat.white_patches = choice(mid_white)
                elif par1.white_patches in vit and non_white_pelt\
                    or par2.white_patches in vit and non_white_pelt:
                    cat.white_patches = choice(vit)
                elif par1.white_patches is None:
                    if par2.white_patches is None:
                        cat.pelt.white = False
                        cat.white_patches = None
                    elif par2.white_patches in little_white:
                        white_patches_choice = random.choices(white_list, weights=(10, 70, 20, 0, 0, 0))
                    elif par2.white_patches in mid_white or par2.white_patches in point_markings:
                        white_patches_choice = random.choices(white_list, weights=(0, 60, 40, 0, 0, 0))
                    elif par2.white_patches in high_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 20, 60, 20, 0, 0))
                    elif par2.white_patches in mostly_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 5, 45, 30, 20, 0))
                    elif par2.white_patches == 'FULLWHITE':
                        white_patches_choice = random.choices(white_list, weights=(0, 20, 20, 20, 20, 20))
                    else:
                        cat.white_patches = choice(little_white)
                elif par1.white_patches in little_white:
                    if par2.white_patches is None:
                        white_patches_choice = random.choices(white_list, weights=(20, 50, 30, 0, 0, 0))
                    elif par2.white_patches in little_white:
                        white_patches_choice = random.choices(white_list, weights=(5, 55, 40, 0, 0, 0))
                    elif par2.white_patches in mid_white or par2.white_patches in point_markings:
                        white_patches_choice = random.choices(white_list, weights=(0, 40, 30, 30, 0, 0))
                    elif par2.white_patches in high_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 10, 50, 30, 10, 0))
                    elif par2.white_patches in mostly_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 25, 40, 25, 10))
                    elif par2.white_patches == 'FULLWHITE':
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 45, 35, 20))
                    else:
                        cat.white_patches = choice(little_white)
                elif par1.white_patches in mid_white or par1.white_patches in point_markings:
                    if par2.white_patches is None:
                        white_patches_choice = random.choices(white_list, weights=(0, 60, 40, 0, 0, 0))
                    elif par2.white_patches in little_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 40, 30, 30, 0, 0))
                    elif par2.white_patches in mid_white or par2.white_patches in point_markings:
                        white_patches_choice = random.choices(white_list, weights=(0, 20, 60, 20, 0, 0))
                    elif par2.white_patches in high_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 30, 50, 20, 0))
                    elif par2.white_patches in mostly_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 20, 50, 20, 10))
                    elif par2.white_patches == 'FULLWHITE':
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 30, 40, 30))
                    else:
                        cat.white_patches = choice(mid_white)
                elif par1.white_patches in high_white:
                    if par2.white_patches is None:
                        white_patches_choice = random.choices(white_list, weights=(0, 20, 60, 20, 0, 0))
                    elif par2.white_patches in little_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 10, 50, 30, 10, 0))
                    elif par2.white_patches in mid_white or par2.white_patches in point_markings:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 30, 50, 20, 0))
                    elif par2.white_patches in high_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 30, 50, 20, 0))
                    elif par2.white_patches in mostly_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 20, 30, 30, 20))
                    elif par2.white_patches == 'FULLWHITE':
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 25, 50, 25))
                    else:
                        cat.white_patches = choice(high_white)
                elif par1.white_patches in mostly_white:
                    if par2.white_patches is None:
                        white_patches_choice = random.choices(white_list, weights=(0, 5, 45, 30, 20, 0))
                    elif par2.white_patches in little_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 25, 40, 25, 10))
                    elif par2.white_patches in mid_white or par2.white_patches in point_markings:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 20, 50, 20, 10))
                    elif par2.white_patches in high_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 20, 30, 30, 20))
                    elif par2.white_patches in mostly_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 20, 60, 20))
                    elif par2.white_patches == 'FULLWHITE':
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 0, 60, 40))
                    else:
                        cat.white_patches = choice(mostly_white)
                elif par1.white_patches == 'FULLWHITE':
                    if par2.white_patches is None:
                        white_patches_choice = random.choices(white_list, weights=(0, 20, 20, 20, 20, 20))
                    elif par2.white_patches in little_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 45, 35, 20))
                    elif par2.white_patches in mid_white or par2.white_patches in point_markings:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 30, 40, 30))
                    elif par2.white_patches in high_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 25, 50, 25))
                    elif par2.white_patches in mostly_white:
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 0, 60, 40))
                    elif par2.white_patches == 'FULLWHITE':
                        white_patches_choice = random.choices(white_list, weights=(0, 0, 0, 0, 40, 60))
                    else:
                        cat.white_patches = choice(mostly_white)
            if cat.pelt.name == 'Calico' and not cat.pelt.white:
                cat.pelt.name = 'Tortie'
                
        # regular non-inheritance white patches generation
        else:
            if pelt_choice == 1 and non_white_pelt:
                cat.white_patches = choice(point_markings)
            elif pelt_choice == 2 and cat.pelt.name in ['Calico', 'TwoColour', 'Tabby', 'Speckled', 'Marbled', 'Bengal', 'Ticked', 'Smoke', 'Rosette']:
                cat.white_patches = choice(mostly_white)
            elif pelt_choice == 3 and cat.pelt.name in ['TwoColour', 'Tabby', 'Speckled', 'Marbled', 'Bengal', 'Ticked', 'Smoke', 'Rosette']\
            and cat.pelt.colour != 'WHITE':
                cat.white_patches = choice(['EXTRA', 'FULLWHITE'])
                if cat.white_patches == None:
                    cat.pelt.white = False
            else:
                if cat.pelt.name in ['TwoColour', 'Tabby', 'Speckled', 'Marbled', 'Bengal', 'Ticked', 'Smoke', 'Rosette']:
                    white_patches_choice = random.choices(white_list, weights=(0, 30, 30, 30, 10, 0))
                elif cat.pelt.name in ['Tortie']:
                    white_patches_choice = random.choices(white_list, weights=(0, 60, 40, 0, 0, 0))
                elif cat.pelt.name in ['Calico']:
                    cat.white_patches = choice(high_white)
                elif pelt_choice == 1 and vit_chance == 1 and non_white_pelt:
                    cat.white_patches = choice(vit)
                else:
                    cat.pelt.white = False
        # just making sure no cats end up with no white patches and true white 
        if cat.white_patches == None:
            if cat.pelt.white is False:
                cat.white_patches = None
                if cat.pelt.name == "Calico":
                    cat.pelt.name = "Tortie"
            elif white_patches_choice == None:
                cat.white_patches = None
                cat.pelt.white = False
                if cat.pelt.name == "Calico":
                    cat.pelt.name = "Tortie"
            elif white_patches_choice == 'EXTRA' or white_patches_choice == 'FULLWHITE' or white_patches_choice == 'POINTMARK':
                cat.white_patches = white_patches_choice
            else:
                whitechoice = choice(list(white_patches_choice))
                if whitechoice == None:
                    cat.pelt.white = False
                    cat.white_patches = None
                elif type(whitechoice) == list:
                    cat.white_patches = choice(whitechoice)
                else:
                    cat.white_patches = whitechoice
    else:
        cat.white_patches = None
        cat.pelt.white = False
        if cat.pelt.name == "Calico":
            cat.pelt.name = "Tortie"


def init_tint(cat):
    # Basic tints as possible for all colors.
    possible_tints = Sprites.cat_tints["possible_tints"]["basic"].copy()
    if cat.pelt.colour in Sprites.cat_tints["colour_groups"]:
        color_group = Sprites.cat_tints["colour_groups"][cat.pelt.colour]
        possible_tints += Sprites.cat_tints["possible_tints"][color_group]
        cat.tint = choice(possible_tints)


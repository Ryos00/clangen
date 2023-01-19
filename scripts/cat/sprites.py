import pygame

from scripts.game_structure.game_essentials import *
try:
    import ujson
except ImportError:
    import json as ujson


class Sprites():
    cat_tints = {}

    def __init__(self, original_size, new_size=None):
        self.size = original_size  # size of a single sprite in a spritesheet
        self.new_size = self.size * 2 if new_size is None else new_size
        self.spritesheets = {}
        self.images = {}
        self.groups = {}
        self.sprites = {}

        self.load_tints()

    def load_tints(self):
        try:
            with open("sprites/dicts/tint.json", 'r') as read_file:
                Sprites.cat_tints = ujson.loads(read_file.read())
        except:
            print("Error Reading Tints")

    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def find_sprite(self, group_name, x, y):
        """
        Find singular sprite from a group.

        Parameters:
        group_name -- Name of Pygame group to find sprite from.
        x -- X-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        y -- Y-offset of the sprite to get. NOT pixel offset, but offset of other sprites.
        """
        # pixels will be calculated automatically, so for x and y, just use 0, 1, 2, 3 etc.
        new_sprite = pygame.Surface((self.size, self.size),
                                    pygame.HWSURFACE | pygame.SRCALPHA)
        new_sprite.blit(self.groups[group_name], (0, 0),
                        (x * self.size, y * self.size, (x + 1) * self.size,
                         (y + 1) * self.size))
        return new_sprite

    def make_group(self,
                   spritesheet,
                   pos,
                   name,
                   sprites_x=3,
                   sprites_y=3):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a sprite-sheet into groups of sprites that are easily accessible.

        Parameters:
        spritesheet -- Name of spritesheet.
        pos -- (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites.
        name -- Name of group to make.
        
        Keyword Arguments
        sprites_x -- Number of sprites horizontally (default: 3)
        sprites_y -- Number of sprites vertically (default: 3)
        """

        # making the group
        new_group = pygame.Surface(
            (self.size * sprites_x, self.size * sprites_y),
            pygame.HWSURFACE | pygame.SRCALPHA)
        new_group.blit(
            self.spritesheets[spritesheet], (0, 0),
            (pos[0] * sprites_x * self.size, pos[1] * sprites_y * self.size,
             (pos[0] + sprites_x) * self.size,
             (pos[1] + sprites_y) * self.size))

        self.groups[name] = new_group

        # splitting group into singular sprites and storing into self.sprites section
        x_spr = 0
        y_spr = 0
        for x in range(sprites_x * sprites_y):
            new_sprite = pygame.Surface((self.size, self.size),
                                        pygame.HWSURFACE | pygame.SRCALPHA)
            new_sprite.blit(new_group, (0, 0),
                            (x_spr * self.size, y_spr * self.size,
                             (x_spr + 1) * self.size, (y_spr + 1) * self.size))
            self.sprites[name + str(x)] = new_sprite
            x_spr += 1
            if x_spr == sprites_x:
                x_spr = 0
                y_spr += 1

    def load_scars(self):
        """
        Loads scar sprites and puts them into groups.
        """
        scars = 'scars'

        for a, i in enumerate(
                ["ONE", "TWO", "THREE", "LEFTEAR", "RIGHTEAR", "NOTAIL"]):
            sprites.make_group('scars', (a, 0), f'scars{i}')
            sprites.make_group('scarsextra', (a, 0),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["MANLEG", "BRIGHTHEART", "MANTAIL", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]):
            sprites.make_group('scars', (a, 1), f'scars{i}')
            sprites.make_group('scarsextra', (a, 1),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["BRIDGE", "RIGHTBLIND", "LEFTBLIND", "BOTHBLIND", "BURNPAWS", "BURNTAIL"]):
            sprites.make_group('scars', (a, 2), f'scars{i}')
            sprites.make_group('scarsextra', (a, 2),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE"]):
            sprites.make_group('scars', (a, 3), f'scars{i}')
            sprites.make_group('scarsextra', (a, 3),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(
                ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE"]):
            sprites.make_group('Newscars', (a, 0), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 0),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["BELLY", "TOETRAP", "SNAKE"]):
            sprites.make_group('Newscars', (a, 1), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 1),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["LEGBITE", "NECKBITE", "FACE", "HALFTAIL", "NOPAW"]):
            sprites.make_group('Newscars', (a, 2), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 2),
                               f'scarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["FROSTFACE", "FROSTTAIL", "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"]):
            sprites.make_group('Newscars', (a, 3), f'scars{i}')
            sprites.make_group('Newscarsextra', (a, 3),
                               f'scarsextra{i}',
                               sprites_y=2)

            # Accessories
        for a, i in enumerate([
            "MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL"]):
            sprites.make_group('medcatherbs', (a, 0), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 0), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS"]):
            sprites.make_group('medcatherbs', (a, 1), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 1), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"]):
            sprites.make_group('medcatherbs', (a, 3), f'acc_herbs{i}')
            sprites.make_group('medcatherbsextra', (a, 3), f'acc_herbsextra{i}', sprites_y=2)    
        sprites.make_group('medcatherbs', (5, 2), 'acc_herbsDRY HERBS')
        sprites.make_group('medcatherbsextra', (5, 2), 'acc_herbsextraDRY HERBS', sprites_y=2)
    
        for a, i in enumerate([
            "POPPY FLOWER", "JUNIPER BERRIES", "DAISY FLOWER", "BORAGE FLOWER", "OAK LEAF", "BEECH LEAF"]):
            sprites.make_group('flowers', (a, 0), f'acc_herbs{i}')
            sprites.make_group('flowersextra', (a, 0), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "LAUREL LEAVES", "COLTSFOOT FLOWER", "BINDWEED VINE", "TORMENTIL FLOWER"]):
            sprites.make_group('flowers', (a, 1), f'acc_herbs{i}')
            sprites.make_group('flowersextra', (a, 1), f'acc_herbsextra{i}', sprites_y=2)
        for a, i in enumerate([
            "BRIGHT-EYE FLOWER", "LAVENDER FLOWER", "YARROW CLUMP"]):
            sprites.make_group('flowers', (a, 2), f'acc_herbs{i}')
            sprites.make_group('flowersextra', (a, 2), f'acc_herbsextra{i}', sprites_y=2)
        
        for a, i in enumerate([
            "RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"]):
            sprites.make_group('medcatherbs', (a, 2), f'acc_wild{i}')
            sprites.make_group('medcatherbsextra', (a, 2), f'acc_wildextra{i}', sprites_y=2)
        for a, i in enumerate(["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"]):
            sprites.make_group('collars', (a, 0), f'collars{i}')
            sprites.make_group('collarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREEN", "RAINBOW", "BLACK", "SPIKES"]):
            sprites.make_group('collars', (a, 1), f'collars{i}')
            sprites.make_group('collarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINK", "PURPLE", "MULTI"]):
            sprites.make_group('collars', (a, 2), f'collars{i}')
            sprites.make_group('collarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
                "CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL",
                "LIMEBELL"
        ]):
            sprites.make_group('bellcollars', (a, 0), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
            ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL"]):
            sprites.make_group('bellcollars', (a, 1), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKBELL", "PURPLEBELL", "MULTIBELL"]):
            sprites.make_group('bellcollars', (a, 2), f'collars{i}')
            sprites.make_group('bellcollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate([
                "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
                "LIMEBOW"
        ]):
            sprites.make_group('bowcollars', (a, 0), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(
            ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW"]):
            sprites.make_group('bowcollars', (a, 1), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKBOW", "PURPLEBOW", "MULTIBOW"]):
            sprites.make_group('bowcollars', (a, 2), f'collars{i}')
            sprites.make_group('bowcollarsextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)

        for a, i in enumerate(["WHITEYARN", "BLUEYARN", "YELLOWYARN", "PURPLEYARN", "PINKYARN", "MINTYARN"]):
            sprites.make_group('yarn', (a, 0), f'collars{i}')
            sprites.make_group('yarnextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREYYARN", "RAINBOWYARN", "GREENYARN", "REDYARN"]):
            sprites.make_group('yarn', (a, 1), f'collars{i}')
            sprites.make_group('yarnextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["FADEDYARN", "ORANGEYARN", "GRADIENTYARN"]):
            sprites.make_group('yarn', (a, 2), f'collars{i}')
            sprites.make_group('yarnextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
            
        for a, i in enumerate(["REDSCARF", "BLUESCARF", "YELLOWSCARF", "CYANSCARF", "CRIMSONSCARF", "LIMESCARF"]):
            sprites.make_group('scarf', (a, 2), f'collars{i}')
            sprites.make_group('scarfextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREENSCARF", "RAINBOWSCARF", "GREYSCARF", "GOLDSCARF"]):
            sprites.make_group('scarf', (a, 1), f'collars{i}')
            sprites.make_group('scarfextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKSCARF", "PURPLESCARF", "ORANGESCARF"]):
            sprites.make_group('scarf', (a, 2), f'collars{i}')
            sprites.make_group('scarfextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
            
        for a, i in enumerate(["REDSCARFS", "BLUESCARFS", "ORANGESCARFS", "MINTSCARFS", "CRIMSONSCARFS", "GREENSCARFS"]):
            sprites.make_group('scarfstripe', (a, 0), f'collars{i}')
            sprites.make_group('scarfstripeextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["CYANSCARFS", "BLUE2SCARFS", "PURPLESCARFS", "GOLDSCARFS"]):
            sprites.make_group('scarfstripe', (a, 1), f'collars{i}')
            sprites.make_group('scarfstripeextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKSCARFS", "YELLOWSCARFS", "BLACKSCARFS"]):
            sprites.make_group('scarfstripe', (a, 2), f'collars{i}')
            sprites.make_group('scarfstripeextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
            
        for a, i in enumerate(["CRIMSONSPIKE", "BLUESPIKE", "YELLOWSPIKE", "CYANSPIKE", "REDSPIKE", "LIMESPIKE"]):
            sprites.make_group('collarspiky', (a, 0), f'collars{i}')
            sprites.make_group('collarspikyextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["GREENSPIKE", "RAINBOWSPIKE", "BLACKSPIKE", "GOLDSPIKE"]):
            sprites.make_group('collarspiky', (a, 1), f'collars{i}')
            sprites.make_group('collarspikyextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["PINKSPIKE", "PURPLESPIKE", "MULTISPIKE"]):
            sprites.make_group('collarspiky', (a, 2), f'collars{i}')
            sprites.make_group('collarspikyextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)
        
        for a, i in enumerate(["LESBIANBAN", "GAYBAN", "NONBINARYBAN", "BISEXUALBAN", "ASEXUALBAN", "AROMANTICBAN"]):
            sprites.make_group('pride', (a, 0), f'collars{i}')
            sprites.make_group('prideextra', (a, 0),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["AROACEBAN", "OMNISEXUALBAN", "INTERSEXBAN", "RAINBOWBAN"]):
            sprites.make_group('pride', (a, 1), f'collars{i}')
            sprites.make_group('prideextra', (a, 1),
                               f'collarsextra{i}',
                               sprites_y=2)
        for a, i in enumerate(["TRANSGENDERBAN", "GENDERQUEERBAN", "AGENDERBAN"]):
            sprites.make_group('pride', (a, 2), f'collars{i}')
            sprites.make_group('prideextra', (a, 2),
                               f'collarsextra{i}',
                               sprites_y=2)


sprites = Sprites(50)
#tiles = Sprites(64)

for x in [
        'lineart', 'singlecolours', 'speckledcolours', 'tabbycolours',
        'whitepatches', 'eyes', 'singleextra', 'tabbyextra',
        'speckledextra', 'whiteextra', 'eyesextra', 'skin',
        'skinextra', 'scars', 'scarsextra', 'whitenewextra', 'whitepatchesnew',
        'scarsdark', 'scarsdarkextra', 'collars', 'collarsextra',
        'bellcollars', 'bellcollarsextra', 'bowcollars', 'bowcollarsextra',
        'bengalcolours', 'bengalextra', 'marbledcolours', 'marbledextra',
        'rosettecolours', 'rosetteextra', 'smokecolours', 'smokeextra', 'tickedcolors', 'tickedextra',
        'whitepatchesryos', 'whitepatchesryosextra', 'whitepatchesbeejeans', 'whitepatchesbeejeansextra',
        'Newscars', 'Newscarsextra', 'shaders', 'lineartdead',
        'tortiecolourssolid', 'tortiecolourstabby', 'tortiecoloursbengal', 'tortiecoloursmarbled',
        'tortiecoloursticked', 'tortiecolourssmoke', 'tortiecoloursrosette', 'tortiecoloursspeckled',
        'tortiesextrasolid', 'tortiesextratabby', 'tortiesextrabengal', 'tortiesextramarbled', 'tortiesextraticked',
        'tortiesextrasmoke', 'tortiesextrarosette', 'tortiesextraspeckled', 
        'medcatherbs', 'medcatherbsextra', 'doberman', 'dobermanextra', 'ghosttabby', 'ghosttabbyextra',
        'pinstripetabby', 'pinstripetabbyextra', 'tortieghost', 'tortieghostextra', 'tortiepinstripe',
        'tortiepinstripeextra', 'merle', 'merleextra', 'snowflake', 'snowflakeextra', 'abyssinian', 'abyssinianextra',
        'clouded', 'cloudedextra', 'eyes2', 'eyesextra2', 'tortiemerle', 'tortiesnowflake',
        'tortieclouded', 'tortiemerleextra', 'tortiesnowflakeextra', 'tortiecloudedextra', 'spotted', 'spottedextra',
        'singlecolours2', 'singleextra2', 'speckledcolours2', 'speckledextra2', 'tabbycolours2', 'tabbyextra2',
        'bengalcolours2', 'bengalextra2', 'marbledcolours2', 'marbledextra2', 'rosettecolours2', 'rosetteextra2', 'smokecolours2', 'smokeextra2',
        'tickedcolors2', 'tickedextra2', 'tortiecolourssolid2', 'tortiecolourstabby2', 'tortiecoloursbengal2', 'tortiecoloursmarbled2',
        'tortiecoloursticked2', 'tortiecolourssmoke2', 'tortiecoloursrosette2','tortiecoloursspeckled2',
        'tortiesextrasolid2', 'tortiesextratabby2', 'tortiesextrabengal2', 'tortiesextramarbled2',
        'tortiesextraticked2', 'tortiesextrasmoke2', 'tortiesextrarosette2', 'tortiesextraspeckled2', 'yarn',
        'yarnextra', 'lineartdf', 'eyes_df', 'eyesextra_df', 'scarf', 'scarfextra', 'scarfstripe', 'scarfstripeextra', 'collarspiky','collarspikyextra', 'cloudycolours', 'cloudyextra',
        'classic', 'classicextra', 'gradient', 'gradientextra', 'mackerel', 'mackerelextra',
        'sokoke', 'sokokeextra', 'tortieclassic', 'tortieclassicextra', 'tortiemackerel', 'siamese', 'siameseextra',
        'tortiemackerelextra', 'tortiesokoke', 'tortiesokokeextra', 'flowers', 'flowersextra', 'pride', 'prideextra',
        'bengalblue', 'bengalblueextra', 'marbledblue', 'marbledblueextra', 'singleblue', 'singleblueextra',
        'speckledblue', 'speckledblueextra', 'tabbyblue', 'tabbyblueextra', 'tickedblue', 'tickedblueextra',
        'bengalwarm', 'bengalwarmextra', 'marbledwarm', 'marbledwarmextra', 'singlewarm', 'singlewarmextra',
        'speckledwarm', 'speckledwarmextra', 'tabbywarm', 'tabbywarmextra', 'tickedwarm', 'tickedwarmextra',
        'bengalrainbow', 'bengalrainbowextra', 'marbledrainbow', 'marbledrainbowextra', 'singlerainbow', 'singlerainbowextra',
        'speckledrainbow', 'speckledrainbowextra', 'tabbyrainbow', 'tabbyrainbowextra', 'tickedrainbow', 'tickedrainbowextra',
        'skin2', 'skin2extra', 'wp', 'wpextra', 'whitepatchesSter', 'whiteextraSter',
        'whitereverse', 'whiteextrareverse', 'ragdollcolors', 'ragdollcolorsextra', 'shadedcolours', 'shadedextra',
        'sterbengal1', 'sterbengal2', 'sterbengal3', 'sterbengalextra1', 'sterbengalextra2', 'sterbengalextra3',
        'sterclassic1', 'sterclassic2', 'sterclassic3', 'sterclassicextra1', 'sterclassicextra2', 'sterclassicextra3',
        'stermackerel1', 'stermackerel2', 'stermackerel3', 'stermackerelextra1', 'stermackerelextra2', 'stermackerelextra3',
        'stermarbled1', 'stermarbled2', 'stermarbled3', 'stermarbledextra1', 'stermarbledextra2', 'stermarbledextra3',
        'sterrosette1', 'sterrosette2', 'sterrosette3', 'sterrosetteextra1', 'sterrosetteextra2', 'sterrosetteextra3',
        'stersingle1', 'stersingle2', 'stersingle3', 'stersingleextra1', 'stersingleextra2', 'stersingleextra3',
        'stersmoke1', 'stersmoke2', 'stersmoke3', 'stersmokeextra1', 'stersmokeextra2', 'stersmokeextra3',
        'stersokoke1', 'stersokoke2', 'stersokoke3', 'stersokokeextra1', 'stersokokeextra2', 'stersokokeextra3',
        'sterspeckled1', 'sterspeckled2', 'sterspeckled3', 'sterspeckledextra1', 'sterspeckledextra2', 'sterspeckledextra3',
        'stertabby1', 'stertabby2', 'stertabby3', 'stertabbyextra1', 'stertabbyextra2', 'stertabbyextra3',
        'sterticked1', 'sterticked2', 'sterticked3', 'stertickedextra1', 'stertickedextra2', 'stertickedextra3',
        'tonkinesecolours', 'tonkinesecolours2', 'tonkinesecolours3', 'tonkineseextra', 'tonkineseextra2', 'tonkineseextra3',
        'freckledcolours', 'freckledcolours2', 'freckledcolours3', 'freckledextra', 'freckledextra2', 'freckledextra3',
        'bengaldilutecolours', 'bengaldilutecolours2', 'bengaldilutecolours3', 'bengaldiluteextra', 'bengaldiluteextra2', 'bengaldiluteextra3',
        'classicdilutecolours', 'classicdilutecolours2', 'classicdilutecolours3', 'classicdiluteextra', 'classicdiluteextra2', 'classicdiluteextra3',
        'freckleddilutecolours', 'freckleddilutecolours2', 'freckleddilutecolours3', 'freckleddiluteextra', 'freckleddiluteextra2', 'freckleddiluteextra3',
        'mackereldilutecolours', 'mackereldilutecolours2', 'mackereldilutecolours3', 'mackereldiluteextra', 'mackereldiluteextra2', 'mackereldiluteextra3',
        'marbleddilutecolours', 'marbleddilutecolours2', 'marbleddilutecolours3', 'marbleddiluteextra', 'marbleddiluteextra2', 'marbleddiluteextra3',
        'rosettedilutecolours', 'rosettedilutecolours2', 'rosettedilutecolours3', 'rosettediluteextra', 'rosettediluteextra2', 'rosettediluteextra3',
        'sokokedilutecolours', 'sokokedilutecolours2', 'sokokedilutecolours3', 'sokokediluteextra', 'sokokediluteextra2', 'sokokediluteextra3',
        'speckleddilutecolours', 'speckleddilutecolours2', 'speckleddilutecolours3', 'speckleddiluteextra', 'speckleddiluteextra2', 'speckleddiluteextra3',
        'tabbydilutecolours', 'tabbydilutecolours2', 'tabbydilutecolours3', 'tabbydiluteextra', 'tabbydiluteextra2', 'tabbydiluteextra3',
        'tickeddilutecolours', 'tickeddilutecolours2', 'tickeddilutecolours3', 'tickeddiluteextra', 'tickeddiluteextra2', 'tickeddiluteextra3',
        'tonkinesedilutecolours', 'tonkinesedilutecolours2', 'tonkinesedilutecolours3', 'tonkinesediluteextra', 'tonkinesediluteextra2', 'tonkinesediluteextra3',
        'darkbengalcolours', 'darkbengalcolours2', 'darkbengalcolours3', 'darkbengalextra', 'darkbengalextra2', 'darkbengalextra3',
        'darkclassiccolours', 'darkclassiccolours2', 'darkclassiccolours3', 'darkclassicextra', 'darkclassicextra2', 'darkclassicextra3',
        'darkmackerelcolours', 'darkmackerelcolours2', 'darkmackerelcolours3', 'darkmackerelextra', 'darkmackerelextra2', 'darkmackerelextra3',
        'darkmarbledcolours', 'darkmarbledcolours2', 'darkmarbledcolours3', 'darkmarbledextra', 'darkmarbledextra2', 'darkmarbledextra3',
        'darkrosettecolours', 'darkrosettecolours2', 'darkrosettecolours3', 'darkrosetteextra', 'darkrosetteextra2', 'darkrosetteextra3',
        'darksokokecolours', 'darksokokecolours2', 'darksokokecolours3', 'darksokokeextra', 'darksokokeextra2', 'darksokokeextra3',
        'darkspeckledcolours', 'darkspeckledcolours2', 'darkspeckledcolours3', 'darkspeckledextra', 'darkspeckledextra2', 'darkspeckledextra3',
        'darktabbycolours', 'darktabbycolours2', 'darktabbycolours3', 'darktabbyextra', 'darktabbyextra2', 'darktabbyextra3',
        'somalicolours', 'somalicolours2', 'somalicolours3', 'somaliextra', 'somaliextra2', 'somaliextra3',
        'tortiecoloursbengaldilute', 'tortiecoloursbengaldilute2', 'tortiesextrabengaldilute', 'tortiesextrabengaldilute2',
        'tortiecoloursclassicdilute', 'tortiecoloursclassicdilute2', 'tortiesextraclassicdilute', 'tortiesextraclassicdilute2',
        'tortiecoloursfreckled', 'tortiecoloursfreckled2', 'tortiesextrafreckled', 'tortiesextrafreckled2',
        'tortiecoloursfreckleddilute', 'tortiecoloursfreckleddilute2', 'tortiesextrafreckleddilute', 'tortiesextrafreckleddilute2',
        'tortiecoloursmackereldilute', 'tortiecoloursmackereldilute2', 'tortiesextramackereldilute', 'tortiesextramackereldilute2',
        'tortiecoloursmarbleddilute', 'tortiecoloursmarbleddilute2', 'tortiesextramarbleddilute', 'tortiesextramarbleddilute2',
        'tortiecoloursrosettedilute', 'tortiecoloursrosettedilute2', 'tortiesextrarosettedilute', 'tortiesextrarosettedilute2',
        'tortiecolourssomali', 'tortiecolourssomali2', 'tortiesextrasomali', 'tortiesextrasomali2',
        'tortiecolourssokokedilute', 'tortiecolourssokokedilute2', 'tortiesextrasokokedilute', 'tortiesextrasokokedilute2',
        'tortiecoloursspeckleddilute', 'tortiecoloursspeckleddilute2', 'tortiesextraspeckleddilute', 'tortiesextraspeckleddilute2',
        'tortiecolourstabbydilute', 'tortiecolourstabbydilute2', 'tortiesextratabbydilute', 'tortiesextratabbydilute2',
        'tortiecolourstickeddilute', 'tortiecolourstickeddilute2', 'tortiesextratickeddilute', 'tortiesextratickeddilute2',
        'tortiecolourstonkinese', 'tortiecolourstonkinese2', 'tortiesextratonkinese', 'tortiesextratonkinese2',
        'tortiecolourstonkinesedilute', 'tortiecolourstonkinesedilute2', 'tortiesextratonkinesedilute', 'tortiesextratonkinesedilute2'


]:
    sprites.spritesheet(f"sprites/{x}.png", x)

for sprite in [
    'Paralyzed_lineart', 'singleparalyzed', 'speckledparalyzed',
    'tabbyparalyzed', 'whiteallparalyzed', 'eyesparalyzed',
    'tabbyparalyzed', 'tortiesparalyzed', 'scarsparalyzed', 'skinparalyzed',
    'medcatherbsparalyzed'

]:
    sprites.spritesheet(f"sprites/paralyzed/{sprite}.png", sprite)

# for x in ['dithered']:
#     tiles.spritesheet(f"sprites/{x}.png", x)

# Line art
sprites.make_group('lineart', (0, 0), 'lines', sprites_y=5)
sprites.make_group('Paralyzed_lineart', (0, 0),
                   'p_lines',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('shaders', (0, 0), 'shaders', sprites_y=5)
sprites.make_group('lineartdead', (0, 0), 'lineartdead', sprites_y=5)
sprites.make_group('lineartdf', (0, 0), 'lineartdf', sprites_y=5)

for a, i in enumerate(
        ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE']):
    sprites.make_group('eyes', (a, 0), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 0), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHERBLUE', 'SUNLITICE']):
    sprites.make_group('eyes', (a, 1), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 1), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['COPPER', 'SAGE', 'BLUE2', 'PALEBLUE', 'BLUEYELLOW', 'BLUEGREEN']):
    sprites.make_group('eyes', (a, 2), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 2), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['PALEYELLOW', 'GOLD', 'GREENYELLOW', 'PINK', 'SCARLET', 'VIOLET']):
    sprites.make_group('eyes', (a, 3), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 3), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['PALEYELLOW2', 'RED', 'AQUA', 'PALEVIOLET', 'SAGEGREEN', 'PALEBLUE2']):
    sprites.make_group('eyes', (a, 4), f'eyes{i}')
    sprites.make_group('eyesextra', (a, 4), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['BROWN', 'SPRINGGREEN', 'GOLDEN', 'HONEY', 'COPPER2', 'MAGENTA']):
    sprites.make_group('eyes2', (a, 0), f'eyes{i}')
    sprites.make_group('eyesextra2', (a, 0), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['MINT', 'EMERALD2', 'PUMPKIN', 'ROSEGOLD', 'GREENGOLD', 'PINKBLUE']):
    sprites.make_group('eyes2', (a, 1), f'eyes{i}')
    sprites.make_group('eyesextra2', (a, 1), f'eyesextra{i}', sprites_y=2)
for a, i in enumerate(
        ['DANDELION', 'INDIGO', 'AMARANTH', 'CORAL', 'DARKGREEN', 'DARKAMBER']):
    sprites.make_group('eyes2', (a, 2), f'eyes{i}')
    sprites.make_group('eyesextra2', (a, 2), f'eyesextra{i}', sprites_y=2)

for a, i in enumerate(['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANY2']):
    sprites.make_group('whitepatches', (a, 0), f'white{i}')
    sprites.make_group('whiteextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate([
    'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL',
    'LIGHTSONG', 'VITILIGO'
]):
    sprites.make_group('whitepatchesnew', (a, 0), f'white{i}')
    sprites.make_group('whitenewextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate([
    'ANYCREAMY', 'TUXEDOCREAMY', 'LITTLECREAMY', 'COLOURPOINTCREAMY',
    'VANCREAMY', 'ANY2CREAMY'
]):
    sprites.make_group('whitepatches', (a, 1), f'white{i}')
    sprites.make_group('whiteextra', (a, 1), f'whiteextra{i}', sprites_y=2)
# extra
sprites.make_group('whitepatches', (0, 2), 'whiteEXTRA')
sprites.make_group('whiteextra', (0, 2), 'whiteextraEXTRA', sprites_y=2)

# ryos white patches
for a, i in enumerate(
        ['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTS2', 'GOATEE', 'VITILIGO2']):
    sprites.make_group('whitepatchesryos', (a, 0), f'white{i}')
    sprites.make_group('whitepatchesryosextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'PAWS', 'MITAINE']):
    sprites.make_group('whitepatchesryos', (a, 1), f'white{i}')
    sprites.make_group('whitepatchesryosextra', (a, 1), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['FAROFA', 'DAMIEN', 'MISTER', 'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'SCOURGE']):
    sprites.make_group('whitepatchesryos', (a, 2), f'white{i}')
    sprites.make_group('whitepatchesryosextra', (a, 2), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW', 'HONEY']):
    sprites.make_group('whitepatchesryos', (a, 3), f'white{i}')
    sprites.make_group('whitepatchesryosextra', (a, 3), f'whiteextra{i}', sprites_y=2)

#era white patches
for a, i in enumerate(
    ['MOJO', 'STAINS', 'STAINS2', 'HALFHEART', 'FRECKLES2', 'WHITEEAR', 'CRESCENT']):
    sprites.make_group('wp', (a, 0), f'white{i}')
    sprites.make_group('wpextra', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
    ['HUSKY', 'COW', 'MASK', 'S', 'BROWNSPOTS', 'SWIFTPAW']):
    sprites.make_group('wp', (a, 1), f'white{i}')
    sprites.make_group('wpextra', (a, 1), f'whiteextra{i}', sprites_y=2)

#sters white patches
for a, i in enumerate(
        ['REVERSEANY', 'REVERSEANYCREAMY', 'REVERSEANY2', 'REVERSEANY2CREAMY', 'REVERSECURVED', 'REVERSECURVEDCREAMY', 'REVERSEHALFFACE', 'REVERSEHALFFACECREAMY']):
    sprites.make_group('whitereverse', (a, 0), f'white{i}')
    sprites.make_group('whiteextrareverse', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['ANYFADE', 'REVERSEANYFADE', 'ANY2FADE', 'REVERSEANY2FADE', 'REVERSECURVEDFADE', 'CURVEDFADE', 'REVERSEHALFFACEFADE', 'HALFFACEFADE']):
    sprites.make_group('whitereverse', (a, 1), f'white{i}')
    sprites.make_group('whiteextrareverse', (a, 1), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['REVERSEVAN', 'REVERSEVANCREAMY', 'VANFADE', 'LIGHTSONGCREAMY', 'CURVEDCREAMY', 'MOORISHFADE', 'MOORISHCREAMY', 'SKUNKCREAMY']):
    sprites.make_group('whitereverse', (a, 2), f'white{i}')
    sprites.make_group('whiteextrareverse', (a, 2), f'whiteextra{i}', sprites_y=2)

for a, i in enumerate(
        ['BLACKSTAR', 'JASMINE', 'BADGER', 'DILUTEDTUXEDO', 'DILUTEDCOLOURPOINT', 'SNOWBACK', 'REVERSEHEART', 'KARPATILIGO']):
    sprites.make_group('whitepatchesSter', (a, 0), f'white{i}')
    sprites.make_group('whiteextraSter', (a, 0), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['BLACKSTARCREAMY', 'HEARTCREAMY', 'REVERSEHEARTCREAMY', 'TAILCREAMY', 'DILUTEDTAIL', 'CREAMBACK', 'PIEBALDCREAMY', 'GLASSCREAMY']):
    sprites.make_group('whitepatchesSter', (a, 1), f'white{i}')
    sprites.make_group('whiteextraSter', (a, 1), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['DILUTEDPIEBALD', 'DILUTEDGLASS', 'DILUTEDHEART', 'BROKENCREAMY', 'DILUTEDBROKEN', 'RAGDOLLCREAMY', 'LILTWOCREAMY', 'RINGTAILCREAMY']):
    sprites.make_group('whitepatchesSter', (a, 2), f'white{i}')
    sprites.make_group('whiteextraSter', (a, 2), f'whiteextra{i}', sprites_y=2)
for a, i in enumerate(
        ['HALFCREAMY', 'HALFFACECREAMY', 'STARCREAMY', 'TOESTAILCREAMY', 'RAVENPAWCREAMY', 'SPINE', 'SCOURGECREAMY', 'SPINECREAMY']):
    sprites.make_group('whitepatchesSter', (a, 3), f'white{i}')
    sprites.make_group('whiteextraSter', (a, 3), f'whiteextra{i}', sprites_y=2)

# beejeans white patches
for a, i in enumerate(['PANTS', 'REVERSEPANTS', 'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'PIEBALD', 'CURVED']):
    sprites.make_group('whitepatchesbeejeans', (a, 0), 'white' + i)
    sprites.make_group('whitepatchesbeejeansextra', (a, 0), 'whiteextra' + i, sprites_y=2)
for a, i in enumerate(['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'POINTMARK']):
    sprites.make_group('whitepatchesbeejeans', (a, 1), 'white' + i)
    sprites.make_group('whitepatchesbeejeansextra', (a, 1), 'whiteextra' + i, sprites_y=2)

#single (solid)
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('singlecolours', (a, 0), f'single{i}')
    sprites.make_group('singleextra', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('singlecolours', (a, 1), f'single{i}')
    sprites.make_group('singleextra', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('singlecolours', (a, 2), f'single{i}')
    sprites.make_group('singleextra', (a, 2), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('singlecolours2', (a, 0), f'single{i}')
    sprites.make_group('singleextra2', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('singlecolours2', (a, 1), f'single{i}')
    sprites.make_group('singleextra2', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('singlecolours2', (a, 2), f'single{i}')
    sprites.make_group('singleextra2', (a, 2), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPINK', 'PINK', 'DARKPINK', 'LIGHTBG', 'BG', 'DARKBG']):
    sprites.make_group('singlerainbow', (a, 0), f'single{i}')
    sprites.make_group('singlerainbowextra', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['CREAM3', 'PALEGINGER2', 'GINGER2', 'DARKGINGER2']):
    sprites.make_group('singlerainbow', (a, 1), f'single{i}')
    sprites.make_group('singlerainbowextra', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB', 'GB', 'DARKGB', 'LIGHTGREEN', 'GREEN', 'DARKGREEN']):
    sprites.make_group('singlerainbow', (a, 2), f'single{i}')
    sprites.make_group('singlerainbowextra', (a, 2), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPURPLE', 'PURPLE', 'DARKPURPLE']):
    sprites.make_group('singleblue', (a, 0), f'single{i}')
    sprites.make_group('singleblueextra', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['SNOW', 'LIGHTGREY2', 'GREY2', 'DARKGREY2', 'BLACK3', 'EBONY']):
    sprites.make_group('singleblue', (a, 1), f'single{i}')
    sprites.make_group('singleblueextra', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['PALEYELLOW', 'YELLOW', 'GOLD', 'DARKCREAM']):
    sprites.make_group('singlewarm', (a, 0), f'single{i}')
    sprites.make_group('singlewarmextra', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB2', 'GB2', 'DARKGB2', 'LIGHTBROWN2', 'BROWN2', 'DARKBROWN2']):
    sprites.make_group('singlewarm', (a, 1), f'single{i}')
    sprites.make_group('singlewarmextra', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('stersingle1', (a, 0), f'single{i}')
    sprites.make_group('stersingleextra1', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('stersingle1', (a, 1), f'single{i}')
    sprites.make_group('stersingleextra1', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('stersingle1', (a, 2), f'single{i}')
    sprites.make_group('stersingleextra1', (a, 2), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('stersingle2', (a, 0), f'single{i}')
    sprites.make_group('stersingleextra2', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('stersingle2', (a, 1), f'single{i}')
    sprites.make_group('stersingleextra2', (a, 1), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('stersingle2', (a, 2), f'single{i}')
    sprites.make_group('stersingleextra2', (a, 2), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('stersingle3', (a, 0), f'single{i}')
    sprites.make_group('stersingleextra3', (a, 0), f'singleextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('stersingle3', (a, 1), f'single{i}')
    sprites.make_group('stersingleextra3', (a, 1), f'singleextra{i}', sprites_y=2)
#tabby
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('tabbycolours', (a, 0), f'tabby{i}')
    sprites.make_group('tabbyextra', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('tabbycolours', (a, 1), f'tabby{i}')
    sprites.make_group('tabbyextra', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('tabbycolours', (a, 2), f'tabby{i}')
    sprites.make_group('tabbyextra', (a, 2), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('tabbycolours2', (a, 0), f'tabby{i}')
    sprites.make_group('tabbyextra2', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('tabbycolours2', (a, 1), f'tabby{i}')
    sprites.make_group('tabbyextra2', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('tabbycolours2', (a, 2), f'tabby{i}')
    sprites.make_group('tabbyextra2', (a, 2), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPINK', 'PINK', 'DARKPINK', 'LIGHTBG', 'BG', 'DARKBG']):
    sprites.make_group('tabbyrainbow', (a, 0), f'tabby{i}')
    sprites.make_group('tabbyrainbowextra', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['CREAM3', 'PALEGINGER2', 'GINGER2', 'DARKGINGER2']):
    sprites.make_group('tabbyrainbow', (a, 1), f'tabby{i}')
    sprites.make_group('tabbyrainbowextra', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB', 'GB', 'DARKGB', 'LIGHTGREEN', 'GREEN', 'DARKGREEN']):
    sprites.make_group('tabbyrainbow', (a, 2), f'tabby{i}')
    sprites.make_group('tabbyrainbowextra', (a, 2), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPURPLE', 'PURPLE', 'DARKPURPLE']):
    sprites.make_group('tabbyblue', (a, 0), f'tabby{i}')
    sprites.make_group('tabbyblueextra', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['SNOW', 'LIGHTGREY2', 'GREY2', 'DARKGREY2', 'BLACK3', 'EBONY']):
    sprites.make_group('tabbyblue', (a, 1), f'tabby{i}')
    sprites.make_group('tabbyblueextra', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEYELLOW', 'YELLOW', 'GOLD', 'DARKCREAM']):
    sprites.make_group('tabbywarm', (a, 0), f'tabby{i}')
    sprites.make_group('tabbywarmextra', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB2', 'GB2', 'DARKGB2', 'LIGHTBROWN2', 'BROWN2', 'DARKBROWN2']):
    sprites.make_group('tabbywarm', (a, 1), f'tabby{i}')
    sprites.make_group('tabbywarmextra', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('stertabby1', (a, 0), f'tabby{i}')
    sprites.make_group('stertabbyextra1', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('stertabby1', (a, 1), f'tabby{i}')
    sprites.make_group('stertabbyextra1', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('stertabby1', (a, 2), f'tabby{i}')
    sprites.make_group('stertabbyextra1', (a, 2), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('stertabby2', (a, 0), f'tabby{i}')
    sprites.make_group('stertabbyextra2', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('stertabby2', (a, 1), f'tabby{i}')
    sprites.make_group('stertabbyextra2', (a, 1), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('stertabby2', (a, 2), f'tabby{i}')
    sprites.make_group('stertabbyextra2', (a, 2), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('stertabby3', (a, 0), f'tabby{i}')
    sprites.make_group('stertabbyextra3', (a, 0), f'tabbyextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('stertabby3', (a, 1), f'tabby{i}')
    sprites.make_group('stertabbyextra3', (a, 1), f'tabbyextra{i}', sprites_y=2)
# darktabby
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('darktabbycolours', (a, 0), f'darktabby{i}')
    sprites.make_group('darktabbyextra', (a, 0), f'darktabbyextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('darktabbycolours', (a, 1), f'darktabby{i}')
    sprites.make_group('darktabbyextra', (a, 1), f'darktabbyextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('darktabbycolours', (a, 2), f'darktabby{i}')
    sprites.make_group('darktabbyextra', (a, 2), f'darktabbyextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('darktabbycolours2', (a, 0), f'darktabby{i}')
    sprites.make_group('darktabbyextra2', (a, 0), f'darktabbyextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('darktabbycolours2', (a, 1), f'darktabby{i}')
    sprites.make_group('darktabbyextra2', (a, 1), f'darktabbyextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('darktabbycolours2', (a, 2), f'darktabby{i}')
    sprites.make_group('darktabbyextra2', (a, 2), f'darktabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('darktabbycolours3', (a, 0), f'darktabby{i}')
    sprites.make_group('darktabbyextra3', (a, 0), f'darktabbyextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('darktabbycolours3', (a, 1), f'darktabby{i}')
    sprites.make_group('darktabbyextra3', (a, 1), f'darktabbyextra{i}', sprites_y=2)
# dilutedtabby
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('tabbydilutecolours', (a, 0), f'dilutedtabby{i}')
    sprites.make_group('tabbydiluteextra', (a, 0), f'dilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('tabbydilutecolours', (a, 1), f'dilutedtabby{i}')
    sprites.make_group('tabbydiluteextra', (a, 1), f'dilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('tabbydilutecolours', (a, 2), f'dilutedtabby{i}')
    sprites.make_group('tabbydiluteextra', (a, 2), f'dilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('tabbydilutecolours2', (a, 0), f'dilutedtabby{i}')
    sprites.make_group('tabbydiluteextra2', (a, 0), f'dilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('tabbydilutecolours2', (a, 1), f'dilutedtabby{i}')
    sprites.make_group('tabbydiluteextra2', (a, 1), f'dilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('tabbydilutecolours2', (a, 2), f'dilutedtabby{i}')
    sprites.make_group('tabbydiluteextra2', (a, 2), f'dilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('tabbydilutecolours3', (a, 0), f'dilutedtabby{i}')
    sprites.make_group('tabbydiluteextra3', (a, 0), f'dilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('tabbydilutecolours3', (a, 1), f'dilutedtabby{i}')
    sprites.make_group('tabbydiluteextra3', (a, 1), f'dilutedtabbyextra{i}', sprites_y=2)
#marbled
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('marbledcolours', (a, 0), f'marbled{i}')
    sprites.make_group('marbledextra', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('marbledcolours', (a, 1), f'marbled{i}')
    sprites.make_group('marbledextra', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('marbledcolours', (a, 2), f'marbled{i}')
    sprites.make_group('marbledextra', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('marbledcolours2', (a, 0), f'marbled{i}')
    sprites.make_group('marbledextra2', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('marbledcolours2', (a, 1), f'marbled{i}')
    sprites.make_group('marbledextra2', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('marbledcolours2', (a, 2), f'marbled{i}')
    sprites.make_group('marbledextra2', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPINK', 'PINK', 'DARKPINK', 'LIGHTBG', 'BG', 'DARKBG']):
    sprites.make_group('marbledrainbow', (a, 0), f'marbled{i}')
    sprites.make_group('marbledrainbowextra', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['CREAM3', 'PALEGINGER2', 'GINGER2', 'DARKGINGER2']):
    sprites.make_group('marbledrainbow', (a, 1), f'marbled{i}')
    sprites.make_group('marbledrainbowextra', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB', 'GB', 'DARKGB', 'LIGHTGREEN', 'GREEN', 'DARKGREEN']):
    sprites.make_group('marbledrainbow', (a, 2), f'marbled{i}')
    sprites.make_group('marbledrainbowextra', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPURPLE', 'PURPLE', 'DARKPURPLE']):
    sprites.make_group('marbledblue', (a, 0), f'marbled{i}')
    sprites.make_group('marbledblueextra', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['SNOW', 'LIGHTGREY2', 'GREY2', 'DARKGREY2', 'BLACK3', 'EBONY']):
    sprites.make_group('marbledblue', (a, 1), f'marbled{i}')
    sprites.make_group('marbledblueextra', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEYELLOW', 'YELLOW', 'GOLD', 'DARKCREAM']):
    sprites.make_group('marbledwarm', (a, 0), f'marbled{i}')
    sprites.make_group('marbledwarmextra', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB2', 'GB2', 'DARKGB2', 'LIGHTBROWN2', 'BROWN2', 'DARKBROWN2']):
    sprites.make_group('marbledwarm', (a, 1), f'marbled{i}')
    sprites.make_group('marbledwarmextra', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('stermarbled1', (a, 0), f'marbled{i}')
    sprites.make_group('stermarbledextra1', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('stermarbled1', (a, 1), f'marbled{i}')
    sprites.make_group('stermarbledextra1', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('stermarbled1', (a, 2), f'marbled{i}')
    sprites.make_group('stermarbledextra1', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('stermarbled2', (a, 0), f'marbled{i}')
    sprites.make_group('stermarbledextra2', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('stermarbled2', (a, 1), f'marbled{i}')
    sprites.make_group('stermarbledextra2', (a, 1), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('stermarbled2', (a, 2), f'marbled{i}')
    sprites.make_group('stermarbledextra2', (a, 2), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('stermarbled3', (a, 0), f'marbled{i}')
    sprites.make_group('stermarbledextra3', (a, 0), f'marbledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('stermarbled3', (a, 1), f'marbled{i}')
    sprites.make_group('stermarbledextra3', (a, 1), f'marbledextra{i}', sprites_y=2)
# darkmarbled
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('darkmarbledcolours', (a, 0), f'darkmarbled{i}')
    sprites.make_group('darkmarbledextra', (a, 0), f'darkmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('darkmarbledcolours', (a, 1), f'darkmarbled{i}')
    sprites.make_group('darkmarbledextra', (a, 1), f'darkmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('darkmarbledcolours', (a, 2), f'darkmarbled{i}')
    sprites.make_group('darkmarbledextra', (a, 2), f'darkmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('darkmarbledcolours2', (a, 0), f'darkmarbled{i}')
    sprites.make_group('darkmarbledextra2', (a, 0), f'darkmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('darkmarbledcolours2', (a, 1), f'darkmarbled{i}')
    sprites.make_group('darkmarbledextra2', (a, 1), f'darkmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('darkmarbledcolours2', (a, 2), f'darkmarbled{i}')
    sprites.make_group('darkmarbledextra2', (a, 2), f'darkmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('darkmarbledcolours3', (a, 0), f'darkmarbled{i}')
    sprites.make_group('darkmarbledextra3', (a, 0), f'darkmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('darkmarbledcolours3', (a, 1), f'darkmarbled{i}')
    sprites.make_group('darkmarbledextra3', (a, 1), f'darkmarbledextra{i}', sprites_y=2)
# dilutedmarbled
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('marbleddilutecolours', (a, 0), f'dilutedmarbled{i}')
    sprites.make_group('marbleddiluteextra', (a, 0), f'dilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('marbleddilutecolours', (a, 1), f'dilutedmarbled{i}')
    sprites.make_group('marbleddiluteextra', (a, 1), f'dilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('marbleddilutecolours', (a, 2), f'dilutedmarbled{i}')
    sprites.make_group('marbleddiluteextra', (a, 2), f'dilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('marbleddilutecolours2', (a, 0), f'dilutedmarbled{i}')
    sprites.make_group('marbleddiluteextra2', (a, 0), f'dilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('marbleddilutecolours2', (a, 1), f'dilutedmarbled{i}')
    sprites.make_group('marbleddiluteextra2', (a, 1), f'dilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('marbleddilutecolours2', (a, 2), f'dilutedmarbled{i}')
    sprites.make_group('marbleddiluteextra2', (a, 2), f'dilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('marbleddilutecolours3', (a, 0), f'dilutedmarbled{i}')
    sprites.make_group('marbleddiluteextra3', (a, 0), f'dilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('marbleddilutecolours3', (a, 1), f'dilutedmarbled{i}')
    sprites.make_group('marbleddiluteextra3', (a, 1), f'dilutedmarbledextra{i}', sprites_y=2)
#rosette
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('rosettecolours', (a, 0), f'rosette{i}')
    sprites.make_group('rosetteextra', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('rosettecolours', (a, 1), f'rosette{i}')
    sprites.make_group('rosetteextra', (a, 1), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('rosettecolours', (a, 2), f'rosette{i}')
    sprites.make_group('rosetteextra', (a, 2), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('rosettecolours2', (a, 0), f'rosette{i}')
    sprites.make_group('rosetteextra2', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('rosettecolours2', (a, 1), f'rosette{i}')
    sprites.make_group('rosetteextra2', (a, 1), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('rosettecolours2', (a, 2), f'rosette{i}')
    sprites.make_group('rosetteextra2', (a, 2), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('sterrosette1', (a, 0), f'rosette{i}')
    sprites.make_group('sterrosetteextra1', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('sterrosette1', (a, 1), f'rosette{i}')
    sprites.make_group('sterrosetteextra1', (a, 1), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('sterrosette1', (a, 2), f'rosette{i}')
    sprites.make_group('sterrosetteextra1', (a, 2), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('sterrosette2', (a, 0), f'rosette{i}')
    sprites.make_group('sterrosetteextra2', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('sterrosette2', (a, 1), f'rosette{i}')
    sprites.make_group('sterrosetteextra2', (a, 1), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('sterrosette2', (a, 2), f'rosette{i}')
    sprites.make_group('sterrosetteextra2', (a, 2), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('sterrosette3', (a, 0), f'rosette{i}')
    sprites.make_group('sterrosetteextra3', (a, 0), f'rosetteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('sterrosette3', (a, 1), f'rosette{i}')
    sprites.make_group('sterrosetteextra3', (a, 1), f'rosetteextra{i}', sprites_y=2)
# darkrosette
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('darkrosettecolours', (a, 0), f'darkrosette{i}')
    sprites.make_group('darkrosetteextra', (a, 0), f'darkrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('darkrosettecolours', (a, 1), f'darkrosette{i}')
    sprites.make_group('darkrosetteextra', (a, 1), f'darkrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('darkrosettecolours', (a, 2), f'darkrosette{i}')
    sprites.make_group('darkrosetteextra', (a, 2), f'darkrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('darkrosettecolours2', (a, 0), f'darkrosette{i}')
    sprites.make_group('darkrosetteextra2', (a, 0), f'darkrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('darkrosettecolours2', (a, 1), f'darkrosette{i}')
    sprites.make_group('darkrosetteextra2', (a, 1), f'darkrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('darkrosettecolours2', (a, 2), f'darkrosette{i}')
    sprites.make_group('darkrosetteextra2', (a, 2), f'darkrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('darkrosettecolours3', (a, 0), f'darkrosette{i}')
    sprites.make_group('darkrosetteextra3', (a, 0), f'darkrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('darkrosettecolours3', (a, 1), f'darkrosette{i}')
    sprites.make_group('darkrosetteextra3', (a, 1), f'darkrosetteextra{i}', sprites_y=2)
# dilutedrosette
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('rosettedilutecolours', (a, 0), f'dilutedrosette{i}')
    sprites.make_group('rosettediluteextra', (a, 0), f'dilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('rosettedilutecolours', (a, 1), f'dilutedrosette{i}')
    sprites.make_group('rosettediluteextra', (a, 1), f'dilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('rosettedilutecolours', (a, 2), f'dilutedrosette{i}')
    sprites.make_group('rosettediluteextra', (a, 2), f'dilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('rosettedilutecolours2', (a, 0), f'dilutedrosette{i}')
    sprites.make_group('rosettediluteextra2', (a, 0), f'dilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('rosettedilutecolours2', (a, 1), f'dilutedrosette{i}')
    sprites.make_group('rosettediluteextra2', (a, 1), f'dilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('rosettedilutecolours2', (a, 2), f'dilutedrosette{i}')
    sprites.make_group('rosettediluteextra2', (a, 2), f'dilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('rosettedilutecolours3', (a, 0), f'dilutedrosette{i}')
    sprites.make_group('rosettediluteextra3', (a, 0), f'dilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('rosettedilutecolours3', (a, 1), f'dilutedrosette{i}')
    sprites.make_group('rosettediluteextra3', (a, 1), f'dilutedrosetteextra{i}', sprites_y=2)
#smoke
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('smokecolours', (a, 0), f'smoke{i}')
    sprites.make_group('smokeextra', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('smokecolours', (a, 1), f'smoke{i}')
    sprites.make_group('smokeextra', (a, 1), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('smokecolours', (a, 2), f'smoke{i}')
    sprites.make_group('smokeextra', (a, 2), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('smokecolours2', (a, 0), f'smoke{i}')
    sprites.make_group('smokeextra2', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('smokecolours2', (a, 1), f'smoke{i}')
    sprites.make_group('smokeextra2', (a, 1), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('smokecolours2', (a, 2), f'smoke{i}')
    sprites.make_group('smokeextra2', (a, 2), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('stersmoke1', (a, 0), f'smoke{i}')
    sprites.make_group('stersmokeextra1', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('stersmoke1', (a, 1), f'smoke{i}')
    sprites.make_group('stersmokeextra1', (a, 1), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('stersmoke1', (a, 2), f'smoke{i}')
    sprites.make_group('stersmokeextra1', (a, 2), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('stersmoke2', (a, 0), f'smoke{i}')
    sprites.make_group('stersmokeextra2', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('stersmoke2', (a, 1), f'smoke{i}')
    sprites.make_group('stersmokeextra2', (a, 1), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('stersmoke2', (a, 2), f'smoke{i}')
    sprites.make_group('stersmokeextra2', (a, 2), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('stersmoke3', (a, 0), f'smoke{i}')
    sprites.make_group('stersmokeextra3', (a, 0), f'smokeextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('stersmoke3', (a, 1), f'smoke{i}')
    sprites.make_group('stersmokeextra3', (a, 1), f'smokeextra{i}', sprites_y=2)
#ticked
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('tickedcolors', (a, 0), f'ticked{i}')
    sprites.make_group('tickedextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('tickedcolors', (a, 1), f'ticked{i}')
    sprites.make_group('tickedextra', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('tickedcolors', (a, 2), f'ticked{i}')
    sprites.make_group('tickedextra', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('tickedcolors2', (a, 0), f'ticked{i}')
    sprites.make_group('tickedextra2', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('tickedcolors2', (a, 1), f'ticked{i}')
    sprites.make_group('tickedextra2', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('tickedcolors2', (a, 2), f'ticked{i}')
    sprites.make_group('tickedextra2', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPINK', 'PINK', 'DARKPINK', 'LIGHTBG', 'BG', 'DARKBG']):
    sprites.make_group('tickedrainbow', (a, 0), f'ticked{i}')
    sprites.make_group('tickedrainbowextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['CREAM3', 'PALEGINGER2', 'GINGER2', 'DARKGINGER2']):
    sprites.make_group('tickedrainbow', (a, 1), f'ticked{i}')
    sprites.make_group('tickedrainbowextra', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB', 'GB', 'DARKGB', 'LIGHTGREEN', 'GREEN', 'DARKGREEN']):
    sprites.make_group('tickedrainbow', (a, 2), f'ticked{i}')
    sprites.make_group('tickedrainbowextra', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPURPLE', 'PURPLE', 'DARKPURPLE']):
    sprites.make_group('tickedblue', (a, 0), f'ticked{i}')
    sprites.make_group('tickedblueextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['SNOW', 'LIGHTGREY2', 'GREY2', 'DARKGREY2', 'BLACK3', 'EBONY']):
    sprites.make_group('tickedblue', (a, 1), f'ticked{i}')
    sprites.make_group('tickedblueextra', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEYELLOW', 'YELLOW', 'GOLD', 'DARKCREAM']):
    sprites.make_group('tickedwarm', (a, 0), f'ticked{i}')
    sprites.make_group('tickedwarmextra', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB2', 'GB2', 'DARKGB2', 'LIGHTBROWN2', 'BROWN2', 'DARKBROWN2']):
    sprites.make_group('tickedwarm', (a, 1), f'ticked{i}')
    sprites.make_group('tickedwarmextra', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('sterticked1', (a, 0), f'ticked{i}')
    sprites.make_group('stertickedextra1', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('sterticked1', (a, 1), f'ticked{i}')
    sprites.make_group('stertickedextra1', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('sterticked1', (a, 2), f'ticked{i}')
    sprites.make_group('stertickedextra1', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('sterticked2', (a, 0), f'ticked{i}')
    sprites.make_group('stertickedextra2', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('sterticked2', (a, 1), f'ticked{i}')
    sprites.make_group('stertickedextra2', (a, 1), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('sterticked2', (a, 2), f'ticked{i}')
    sprites.make_group('stertickedextra2', (a, 2), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('sterticked3', (a, 0), f'ticked{i}')
    sprites.make_group('stertickedextra3', (a, 0), f'tickedextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('sterticked3', (a, 1), f'ticked{i}')
    sprites.make_group('stertickedextra3', (a, 1), f'tickedextra{i}', sprites_y=2)
# tickeddilute
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('tickeddilutecolours', (a, 0), f'tickeddilute{i}')
    sprites.make_group('tickeddiluteextra', (a, 0), f'tickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('tickeddilutecolours', (a, 1), f'tickeddilute{i}')
    sprites.make_group('tickeddiluteextra', (a, 1), f'tickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('tickeddilutecolours', (a, 2), f'tickeddilute{i}')
    sprites.make_group('tickeddiluteextra', (a, 2), f'tickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('tickeddilutecolours2', (a, 0), f'tickeddilute{i}')
    sprites.make_group('tickeddiluteextra2', (a, 0), f'tickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('tickeddilutecolours2', (a, 1), f'tickeddilute{i}')
    sprites.make_group('tickeddiluteextra2', (a, 1), f'tickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('tickeddilutecolours2', (a, 2), f'tickeddilute{i}')
    sprites.make_group('tickeddiluteextra2', (a, 2), f'tickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('tickeddilutecolours3', (a, 0), f'tickeddilute{i}')
    sprites.make_group('tickeddiluteextra3', (a, 0), f'tickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('tickeddilutecolours3', (a, 1), f'tickeddilute{i}')
    sprites.make_group('tickeddiluteextra3', (a, 1), f'tickeddiluteextra{i}', sprites_y=2)
#speckled
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('speckledcolours', (a, 0), f'speckled{i}')
    sprites.make_group('speckledextra', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('speckledcolours', (a, 1), f'speckled{i}')
    sprites.make_group('speckledextra', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('speckledcolours', (a, 2), f'speckled{i}')
    sprites.make_group('speckledextra', (a, 2), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('speckledcolours2', (a, 0), f'speckled{i}')
    sprites.make_group('speckledextra2', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('speckledcolours2', (a, 1), f'speckled{i}')
    sprites.make_group('speckledextra2', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('speckledcolours2', (a, 2), f'speckled{i}')
    sprites.make_group('speckledextra2', (a, 2), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPINK', 'PINK', 'DARKPINK', 'LIGHTBG', 'BG', 'DARKBG']):
    sprites.make_group('speckledrainbow', (a, 0), f'speckled{i}')
    sprites.make_group('speckledrainbowextra', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['CREAM3', 'PALEGINGER2', 'GINGER2', 'DARKGINGER2']):
    sprites.make_group('speckledrainbow', (a, 1), f'speckled{i}')
    sprites.make_group('speckledrainbowextra', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB', 'GB', 'DARKGB', 'LIGHTGREEN', 'GREEN', 'DARKGREEN']):
    sprites.make_group('speckledrainbow', (a, 2), f'speckled{i}')
    sprites.make_group('speckledrainbowextra', (a, 2), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPURPLE', 'PURPLE', 'DARKPURPLE']):
    sprites.make_group('speckledblue', (a, 0), f'speckled{i}')
    sprites.make_group('speckledblueextra', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['SNOW', 'LIGHTGREY2', 'GREY2', 'DARKGREY2', 'BLACK3', 'EBONY']):
    sprites.make_group('speckledblue', (a, 1), f'speckled{i}')
    sprites.make_group('speckledblueextra', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEYELLOW', 'YELLOW', 'GOLD', 'DARKCREAM']):
    sprites.make_group('speckledwarm', (a, 0), f'speckled{i}')
    sprites.make_group('speckledwarmextra', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB2', 'GB2', 'DARKGB2', 'LIGHTBROWN2', 'BROWN2', 'DARKBROWN2']):
    sprites.make_group('speckledwarm', (a, 1), f'speckled{i}')
    sprites.make_group('speckledwarmextra', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('sterspeckled1', (a, 0), f'speckled{i}')
    sprites.make_group('sterspeckledextra1', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('sterspeckled1', (a, 1), f'speckled{i}')
    sprites.make_group('sterspeckledextra1', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('sterspeckled1', (a, 2), f'speckled{i}')
    sprites.make_group('sterspeckledextra1', (a, 2), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('sterspeckled2', (a, 0), f'speckled{i}')
    sprites.make_group('sterspeckledextra2', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('sterspeckled2', (a, 1), f'speckled{i}')
    sprites.make_group('sterspeckledextra2', (a, 1), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('sterspeckled2', (a, 2), f'speckled{i}')
    sprites.make_group('sterspeckledextra2', (a, 2), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('sterspeckled3', (a, 0), f'speckled{i}')
    sprites.make_group('sterspeckledextra3', (a, 0), f'speckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('sterspeckled3', (a, 1), f'speckled{i}')
    sprites.make_group('sterspeckledextra3', (a, 1), f'speckledextra{i}', sprites_y=2)
# darkspeckled
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('darkspeckledcolours', (a, 0), f'darkspeckled{i}')
    sprites.make_group('darkspeckledextra', (a, 0), f'darkspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('darkspeckledcolours', (a, 1), f'darkspeckled{i}')
    sprites.make_group('darkspeckledextra', (a, 1), f'darkspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('darkspeckledcolours', (a, 2), f'darkspeckled{i}')
    sprites.make_group('darkspeckledextra', (a, 2), f'darkspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('darkspeckledcolours2', (a, 0), f'darkspeckled{i}')
    sprites.make_group('darkspeckledextra2', (a, 0), f'darkspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('darkspeckledcolours2', (a, 1), f'darkspeckled{i}')
    sprites.make_group('darkspeckledextra2', (a, 1), f'darkspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('darkspeckledcolours2', (a, 2), f'darkspeckled{i}')
    sprites.make_group('darkspeckledextra2', (a, 2), f'darkspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('darkspeckledcolours3', (a, 0), f'darkspeckled{i}')
    sprites.make_group('darkspeckledextra3', (a, 0), f'darkspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('darkspeckledcolours3', (a, 1), f'darkspeckled{i}')
    sprites.make_group('darkspeckledextra3', (a, 1), f'darkspeckledextra{i}', sprites_y=2)
# dilutedspeckled
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('speckleddilutecolours', (a, 0), f'dilutedspeckled{i}')
    sprites.make_group('speckleddiluteextra', (a, 0), f'dilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('speckleddilutecolours', (a, 1), f'dilutedspeckled{i}')
    sprites.make_group('speckleddiluteextra', (a, 1), f'dilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('speckleddilutecolours', (a, 2), f'dilutedspeckled{i}')
    sprites.make_group('speckleddiluteextra', (a, 2), f'dilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('speckleddilutecolours2', (a, 0), f'dilutedspeckled{i}')
    sprites.make_group('speckleddiluteextra2', (a, 0), f'dilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('speckleddilutecolours2', (a, 1), f'dilutedspeckled{i}')
    sprites.make_group('speckleddiluteextra2', (a, 1), f'dilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('speckleddilutecolours2', (a, 2), f'dilutedspeckled{i}')
    sprites.make_group('speckleddiluteextra2', (a, 2), f'dilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('speckleddilutecolours3', (a, 0), f'dilutedspeckled{i}')
    sprites.make_group('speckleddiluteextra3', (a, 0), f'dilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('speckleddilutecolours3', (a, 1), f'dilutedspeckled{i}')
    sprites.make_group('speckleddiluteextra3', (a, 1), f'dilutedspeckledextra{i}', sprites_y=2)
#bengal
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('bengalcolours', (a, 0), f'bengal{i}')
    sprites.make_group('bengalextra', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('bengalcolours', (a, 1), f'bengal{i}')
    sprites.make_group('bengalextra', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('bengalcolours', (a, 2), f'bengal{i}')
    sprites.make_group('bengalextra', (a, 2), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE2', 'BLUE', 'CARAMEL', 'LILAC', 'BLACK2', 'DARK']):
    sprites.make_group('bengalcolours2', (a, 0), f'bengal{i}')
    sprites.make_group('bengalextra2', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['PALE', 'CREAM2', 'APRICOT', 'ORANGE']):
    sprites.make_group('bengalcolours2', (a, 1), f'bengal{i}')
    sprites.make_group('bengalextra2', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN', 'CINNAMON', 'CHOCOLATE']):
    sprites.make_group('bengalcolours2', (a, 2), f'bengal{i}')
    sprites.make_group('bengalextra2', (a, 2), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPINK', 'PINK', 'DARKPINK', 'LIGHTBG', 'BG', 'DARKBG']):
    sprites.make_group('bengalrainbow', (a, 0), f'bengal{i}')
    sprites.make_group('bengalrainbowextra', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['CREAM3', 'PALEGINGER2', 'GINGER2', 'DARKGINGER2']):
    sprites.make_group('bengalrainbow', (a, 1), f'bengal{i}')
    sprites.make_group('bengalrainbowextra', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB', 'GB', 'DARKGB', 'LIGHTGREEN', 'GREEN', 'DARKGREEN']):
    sprites.make_group('bengalrainbow', (a, 2), f'bengal{i}')
    sprites.make_group('bengalrainbowextra', (a, 2), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTPURPLE', 'PURPLE', 'DARKPURPLE']):
    sprites.make_group('bengalblue', (a, 0), f'bengal{i}')
    sprites.make_group('bengalblueextra', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['SNOW', 'LIGHTGREY2', 'GREY2', 'DARKGREY2', 'BLACK3', 'EBONY']):
    sprites.make_group('bengalblue', (a, 1), f'bengal{i}')
    sprites.make_group('bengalblueextra', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['PALEYELLOW', 'YELLOW', 'GOLD', 'DARKCREAM']):
    sprites.make_group('bengalwarm', (a, 0), f'bengal{i}')
    sprites.make_group('bengalwarmextra', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGB2', 'GB2', 'DARKGB2', 'LIGHTBROWN2', 'BROWN2', 'DARKBROWN2']):
    sprites.make_group('bengalwarm', (a, 1), f'bengal{i}')
    sprites.make_group('bengalwarmextra', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('sterbengal1', (a, 0), f'bengal{i}')
    sprites.make_group('sterbengalextra1', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('sterbengal1', (a, 1), f'bengal{i}')
    sprites.make_group('sterbengalextra1', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('sterbengal1', (a, 2), f'bengal{i}')
    sprites.make_group('sterbengalextra1', (a, 2), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('sterbengal2', (a, 0), f'bengal{i}')
    sprites.make_group('sterbengalextra2', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('sterbengal2', (a, 1), f'bengal{i}')
    sprites.make_group('sterbengalextra2', (a, 1), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('sterbengal2', (a, 2), f'bengal{i}')
    sprites.make_group('sterbengalextra2', (a, 2), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('sterbengal3', (a, 0), f'bengal{i}')
    sprites.make_group('sterbengalextra3', (a, 0), f'bengalextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('sterbengal3', (a, 1), f'bengal{i}')
    sprites.make_group('sterbengalextra3', (a, 1), f'bengalextra{i}', sprites_y=2)
# darkbengal
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('darkbengalcolours', (a, 0), f'darkbengal{i}')
    sprites.make_group('darkbengalextra', (a, 0), f'darkbengalextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('darkbengalcolours', (a, 1), f'darkbengal{i}')
    sprites.make_group('darkbengalextra', (a, 1), f'darkbengalextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('darkbengalcolours', (a, 2), f'darkbengal{i}')
    sprites.make_group('darkbengalextra', (a, 2), f'darkbengalextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('darkbengalcolours2', (a, 0), f'darkbengal{i}')
    sprites.make_group('darkbengalextra2', (a, 0), f'darkbengalextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('darkbengalcolours2', (a, 1), f'darkbengal{i}')
    sprites.make_group('darkbengalextra2', (a, 1), f'darkbengalextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('darkbengalcolours2', (a, 2), f'darkbengal{i}')
    sprites.make_group('darkbengalextra2', (a, 2), f'darkbengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('darkbengalcolours3', (a, 0), f'darkbengal{i}')
    sprites.make_group('darkbengalextra3', (a, 0), f'darkbengalextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('darkbengalcolours3', (a, 1), f'darkbengal{i}')
    sprites.make_group('darkbengalextra3', (a, 1), f'darkbengalextra{i}', sprites_y=2)
# dilutedbengal
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('bengaldilutecolours', (a, 0), f'dilutedbengal{i}')
    sprites.make_group('bengaldiluteextra', (a, 0), f'dilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('bengaldilutecolours', (a, 1), f'dilutedbengal{i}')
    sprites.make_group('bengaldiluteextra', (a, 1), f'dilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('bengaldilutecolours', (a, 2), f'dilutedbengal{i}')
    sprites.make_group('bengaldiluteextra', (a, 2), f'dilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('bengaldilutecolours2', (a, 0), f'dilutedbengal{i}')
    sprites.make_group('bengaldiluteextra2', (a, 0), f'dilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('bengaldilutecolours2', (a, 1), f'dilutedbengal{i}')
    sprites.make_group('bengaldiluteextra2', (a, 1), f'dilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('bengaldilutecolours2', (a, 2), f'dilutedbengal{i}')
    sprites.make_group('bengaldiluteextra2', (a, 2), f'dilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('bengaldilutecolours3', (a, 0), f'dilutedbengal{i}')
    sprites.make_group('bengaldiluteextra3', (a, 0), f'dilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('bengaldilutecolours3', (a, 1), f'dilutedbengal{i}')
    sprites.make_group('bengaldiluteextra3', (a, 1), f'dilutedbengalextra{i}', sprites_y=2)
# somali
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('somalicolours', (a, 0), f'somali{i}')
    sprites.make_group('somaliextra', (a, 0), f'somaliextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('somalicolours', (a, 1), f'somali{i}')
    sprites.make_group('somaliextra', (a, 1), f'somaliextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('somalicolours', (a, 2), f'somali{i}')
    sprites.make_group('somaliextra', (a, 2), f'somaliextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('somalicolours2', (a, 0), f'somali{i}')
    sprites.make_group('somaliextra2', (a, 0), f'somaliextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('somalicolours2', (a, 1), f'somali{i}')
    sprites.make_group('somaliextra2', (a, 1), f'somaliextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN', 'DARKGOLD', 'HONEY']):
    sprites.make_group('somalicolours2', (a, 2), f'somali{i}')
    sprites.make_group('somaliextra2', (a, 2), f'somaliextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('somalicolours3', (a, 0), f'somali{i}')
    sprites.make_group('somaliextra3', (a, 0), f'somaliextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('somalicolours3', (a, 1), f'somali{i}')
    sprites.make_group('somaliextra3', (a, 1), f'somaliextra{i}', sprites_y=2)
#abyssinian
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('abyssinian', (a, 0), f'abyssinian{i}')
    sprites.make_group('abyssinianextra', (a, 0), f'abyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('abyssinian', (a, 1), f'abyssinian{i}')
    sprites.make_group('abyssinianextra', (a, 1), f'abyssinianextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('abyssinian', (a, 2), f'abyssinian{i}')
    sprites.make_group('abyssinianextra', (a, 2), f'abyssinianextra{i}', sprites_y=2)
#clouded
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('clouded', (a, 0), f'clouded{i}')
    sprites.make_group('cloudedextra', (a, 0), f'cloudedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('clouded', (a, 1), f'clouded{i}')
    sprites.make_group('cloudedextra', (a, 1), f'cloudedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('clouded', (a, 2), f'clouded{i}')
    sprites.make_group('cloudedextra', (a, 2), f'cloudedextra{i}', sprites_y=2)
#ragdoll
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('ragdollcolors', (a, 0), f'ragdoll{i}')
    sprites.make_group('ragdollcolorsextra', (a, 0), f'ragdollextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('ragdollcolors', (a, 1), f'ragdoll{i}')
    sprites.make_group('ragdollcolorsextra', (a, 1), f'ragdollextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('ragdollcolors', (a, 2), f'ragdoll{i}')
    sprites.make_group('ragdollcolorsextra', (a, 2), f'ragdollextra{i}', sprites_y=2)
#shaded
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('shadedcolours', (a, 0), f'shaded{i}')
    sprites.make_group('shadedextra', (a, 0), f'shadedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('shadedcolours', (a, 1), f'shaded{i}')
    sprites.make_group('shadedextra', (a, 1), f'shadedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('shadedcolours', (a, 2), f'shaded{i}')
    sprites.make_group('shadedextra', (a, 2), f'shadedextra{i}', sprites_y=2)
#merle
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('merle', (a, 0), f'merle{i}')
    sprites.make_group('merleextra', (a, 0), f'merleextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('merle', (a, 1), f'merle{i}')
    sprites.make_group('merleextra', (a, 1), f'merleextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('merle', (a, 2), f'merle{i}')
    sprites.make_group('merleextra', (a, 2), f'merleextra{i}', sprites_y=2)
#snowflake
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('snowflake', (a, 0), f'snowflake{i}')
    sprites.make_group('snowflakeextra', (a, 0), f'snowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('snowflake', (a, 1), f'snowflake{i}')
    sprites.make_group('snowflakeextra', (a, 1), f'snowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('snowflake', (a, 2), f'snowflake{i}')
    sprites.make_group('snowflakeextra', (a, 2), f'snowflakeextra{i}', sprites_y=2)
#ghost
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('ghosttabby', (a, 0), f'ghost{i}')
    sprites.make_group('ghosttabbyextra', (a, 0), f'ghostextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('ghosttabby', (a, 1), f'ghost{i}')
    sprites.make_group('ghosttabbyextra', (a, 1), f'ghostextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('ghosttabby', (a, 2), f'ghost{i}')
    sprites.make_group('ghosttabbyextra', (a, 2), f'ghostextra{i}', sprites_y=2)
#pinstripe
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('pinstripetabby', (a, 0), f'pinstripe{i}')
    sprites.make_group('pinstripetabbyextra', (a, 0), f'pinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('pinstripetabby', (a, 1), f'pinstripe{i}')
    sprites.make_group('pinstripetabbyextra', (a, 1), f'pinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('pinstripetabby', (a, 2), f'pinstripe{i}')
    sprites.make_group('pinstripetabbyextra', (a, 2), f'pinstripeextra{i}', sprites_y=2)
#doberman
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('doberman', (a, 0), f'doberman{i}')
    sprites.make_group('dobermanextra', (a, 0), f'dobermanextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('doberman', (a, 1), f'doberman{i}')
    sprites.make_group('dobermanextra', (a, 1), f'dobermanextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('doberman', (a, 2), f'doberman{i}')
    sprites.make_group('dobermanextra', (a, 2), f'dobermanextra{i}', sprites_y=2)
#spotted
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('spotted', (a, 0), f'spotted{i}')
    sprites.make_group('spottedextra', (a, 0), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('spotted', (a, 1), f'spotted{i}')
    sprites.make_group('spottedextra', (a, 1), f'spottedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('spotted', (a, 2), f'spotted{i}')
    sprites.make_group('spottedextra', (a, 2), f'spottedextra{i}', sprites_y=2)
#cloudy
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('cloudycolours', (a, 0), f'cloudy{i}')
    sprites.make_group('cloudyextra', (a, 0), f'cloudyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']):
    sprites.make_group('cloudycolours', (a, 1), f'cloudy{i}')
    sprites.make_group('cloudyextra', (a, 1), f'cloudyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('cloudycolours', (a, 2), f'cloudy{i}')
    sprites.make_group('cloudyextra', (a, 2), f'cloudyextra{i}', sprites_y=2)
#classic
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('classic', (a, 0), f'classic{i}')
    sprites.make_group('classicextra', (a, 0), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('classic', (a, 1), f'classic{i}')
    sprites.make_group('classicextra', (a, 1), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('classic', (a, 2), f'classic{i}')
    sprites.make_group('classicextra', (a, 2), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('sterclassic1', (a, 0), f'classic{i}')
    sprites.make_group('sterclassicextra1', (a, 0), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('sterclassic1', (a, 1), f'classic{i}')
    sprites.make_group('sterclassicextra1', (a, 1), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('sterclassic1', (a, 2), f'classic{i}')
    sprites.make_group('sterclassicextra1', (a, 2), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('sterclassic2', (a, 0), f'classic{i}')
    sprites.make_group('sterclassicextra2', (a, 0), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('sterclassic2', (a, 1), f'classic{i}')
    sprites.make_group('sterclassicextra2', (a, 1), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('sterclassic2', (a, 2), f'classic{i}')
    sprites.make_group('sterclassicextra2', (a, 2), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('sterclassic3', (a, 0), f'classic{i}')
    sprites.make_group('sterclassicextra3', (a, 0), f'classicextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('sterclassic3', (a, 1), f'classic{i}')
    sprites.make_group('sterclassicextra3', (a, 1), f'classicextra{i}', sprites_y=2)
# darkclassic
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('darkclassiccolours', (a, 0), f'darkclassic{i}')
    sprites.make_group('darkclassicextra', (a, 0), f'darkclassicextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('darkclassiccolours', (a, 1), f'darkclassic{i}')
    sprites.make_group('darkclassicextra', (a, 1), f'darkclassicextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('darkclassiccolours', (a, 2), f'darkclassic{i}')
    sprites.make_group('darkclassicextra', (a, 2), f'darkclassicextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('darkclassiccolours2', (a, 0), f'darkclassic{i}')
    sprites.make_group('darkclassicextra2', (a, 0), f'darkclassicextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('darkclassiccolours2', (a, 1), f'darkclassic{i}')
    sprites.make_group('darkclassicextra2', (a, 1), f'darkclassicextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('darkclassiccolours2', (a, 2), f'darkclassic{i}')
    sprites.make_group('darkclassicextra2', (a, 2), f'darkclassicextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('darkclassiccolours3', (a, 0), f'darkclassic{i}')
    sprites.make_group('darkclassicextra3', (a, 0), f'darkclassicextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('darkclassiccolours3', (a, 1), f'darkclassic{i}')
    sprites.make_group('darkclassicextra3', (a, 1), f'darkclassicextra{i}', sprites_y=2)
# dilutedclassic
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('classicdilutecolours', (a, 0), f'dilutedclassic{i}')
    sprites.make_group('classicdiluteextra', (a, 0), f'dilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('classicdilutecolours', (a, 1), f'dilutedclassic{i}')
    sprites.make_group('classicdiluteextra', (a, 1), f'dilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('classicdilutecolours', (a, 2), f'dilutedclassic{i}')
    sprites.make_group('classicdiluteextra', (a, 2), f'dilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('classicdilutecolours2', (a, 0), f'dilutedclassic{i}')
    sprites.make_group('classicdiluteextra2', (a, 0), f'dilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('classicdilutecolours2', (a, 1), f'dilutedclassic{i}')
    sprites.make_group('classicdiluteextra2', (a, 1), f'dilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('classicdilutecolours2', (a, 2), f'dilutedclassic{i}')
    sprites.make_group('classicdiluteextra2', (a, 2), f'dilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('classicdilutecolours3', (a, 0), f'dilutedclassic{i}')
    sprites.make_group('classicdiluteextra3', (a, 0), f'dilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('classicdilutecolours3', (a, 1), f'dilutedclassic{i}')
    sprites.make_group('classicdiluteextra3', (a, 1), f'dilutedclassicextra{i}', sprites_y=2)
#mackerel
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('mackerel', (a, 0), f'mackerel{i}')
    sprites.make_group('mackerelextra', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('mackerel', (a, 1), f'mackerel{i}')
    sprites.make_group('mackerelextra', (a, 1), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('mackerel', (a, 2), f'mackerel{i}')
    sprites.make_group('mackerelextra', (a, 2), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('stermackerel1', (a, 0), f'mackerel{i}')
    sprites.make_group('stermackerelextra1', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('stermackerel1', (a, 1), f'mackerel{i}')
    sprites.make_group('stermackerelextra1', (a, 1), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('stermackerel1', (a, 2), f'mackerel{i}')
    sprites.make_group('stermackerelextra1', (a, 2), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('stermackerel2', (a, 0), f'mackerel{i}')
    sprites.make_group('stermackerelextra2', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('stermackerel2', (a, 1), f'mackerel{i}')
    sprites.make_group('stermackerelextra2', (a, 1), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('stermackerel2', (a, 2), f'mackerel{i}')
    sprites.make_group('stermackerelextra2', (a, 2), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('stermackerel3', (a, 0), f'mackerel{i}')
    sprites.make_group('stermackerelextra3', (a, 0), f'mackerelextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('stermackerel3', (a, 1), f'freckled{i}')
    sprites.make_group('stermackerelextra3', (a, 1), f'freckledextra{i}', sprites_y=2)
# darkmackerel
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('darkmackerelcolours', (a, 0), f'darkmackerel{i}')
    sprites.make_group('darkmackerelextra', (a, 0), f'darkmackerelextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('darkmackerelcolours', (a, 1), f'darkmackerel{i}')
    sprites.make_group('darkmackerelextra', (a, 1), f'darkmackerelextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('darkmackerelcolours', (a, 2), f'darkmackerel{i}')
    sprites.make_group('darkmackerelextra', (a, 2), f'darkmackerelextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('darkmackerelcolours2', (a, 0), f'darkmackerel{i}')
    sprites.make_group('darkmackerelextra2', (a, 0), f'darkmackerelextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('darkmackerelcolours2', (a, 1), f'darkmackerel{i}')
    sprites.make_group('darkmackerelextra2', (a, 1), f'darkmackerelextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('darkmackerelcolours2', (a, 2), f'darkmackerel{i}')
    sprites.make_group('darkmackerelextra2', (a, 2), f'darkmackerelextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('darkmackerelcolours3', (a, 0), f'darkmackerel{i}')
    sprites.make_group('darkmackerelextra3', (a, 0), f'darkmackerelextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('darkmackerelcolours3', (a, 1), f'darkmackerel{i}')
    sprites.make_group('darkmackerelextra3', (a, 1), f'darkmackerelextra{i}', sprites_y=2)
# mackereldilute
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('mackereldilutecolours', (a, 0), f'mackereldilute{i}')
    sprites.make_group('mackereldiluteextra', (a, 0), f'mackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('mackereldilutecolours', (a, 1), f'mackereldilute{i}')
    sprites.make_group('mackereldiluteextra', (a, 1), f'mackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('mackereldilutecolours', (a, 2), f'mackereldilute{i}')
    sprites.make_group('mackereldiluteextra', (a, 2), f'mackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('mackereldilutecolours2', (a, 0), f'mackereldilute{i}')
    sprites.make_group('mackereldiluteextra2', (a, 0), f'mackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('mackereldilutecolours2', (a, 1), f'mackereldilute{i}')
    sprites.make_group('mackereldiluteextra2', (a, 1), f'mackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('mackereldilutecolours2', (a, 2), f'mackereldilute{i}')
    sprites.make_group('mackereldiluteextra2', (a, 2), f'mackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('mackereldilutecolours3', (a, 0), f'mackereldilute{i}')
    sprites.make_group('mackereldiluteextra3', (a, 0), f'mackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('mackereldilutecolours3', (a, 1), f'mackereldilute{i}')
    sprites.make_group('mackereldiluteextra3', (a, 1), f'mackereldiluteextra{i}', sprites_y=2)
# freckled
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('freckledcolours', (a, 0), f'freckled{i}')
    sprites.make_group('freckledextra', (a, 0), f'freckledextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('freckledcolours', (a, 1), f'freckled{i}')
    sprites.make_group('freckledextra', (a, 1), f'freckledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('freckledcolours', (a, 2), f'freckled{i}')
    sprites.make_group('freckledextra', (a, 2), f'freckledextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('freckledcolours2', (a, 0), f'freckled{i}')
    sprites.make_group('freckledextra2', (a, 0), f'freckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('freckledcolours2', (a, 1), f'freckled{i}')
    sprites.make_group('freckledextra2', (a, 1), f'freckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('freckledcolours2', (a, 2), f'freckled{i}')
    sprites.make_group('freckledextra2', (a, 2), f'freckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('freckledcolours3', (a, 0), f'freckled{i}')
    sprites.make_group('freckledextra3', (a, 0), f'freckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('freckledcolours3', (a, 1), f'freckled{i}')
    sprites.make_group('freckledextra3', (a, 1), f'freckledextra{i}', sprites_y=2)
# dilutedfreckled
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('freckleddilutecolours', (a, 0), f'dilutedfreckled{i}')
    sprites.make_group('freckleddiluteextra', (a, 0), f'dilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('freckleddilutecolours', (a, 1), f'dilutedfreckled{i}')
    sprites.make_group('freckleddiluteextra', (a, 1), f'dilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('freckleddilutecolours', (a, 2), f'dilutedfreckled{i}')
    sprites.make_group('freckleddiluteextra', (a, 2), f'dilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('freckleddilutecolours2', (a, 0), f'dilutedfreckled{i}')
    sprites.make_group('freckleddiluteextra2', (a, 0), f'dilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('freckleddilutecolours2', (a, 1), f'dilutedfreckled{i}')
    sprites.make_group('freckleddiluteextra2', (a, 1), f'dilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('freckleddilutecolours2', (a, 2), f'dilutedfreckled{i}')
    sprites.make_group('freckleddiluteextra2', (a, 2), f'dilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('freckleddilutecolours3', (a, 0), f'dilutedfreckled{i}')
    sprites.make_group('freckleddiluteextra3', (a, 0), f'dilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('freckleddilutecolours3', (a, 1), f'dilutedfreckled{i}')
    sprites.make_group('freckleddiluteextra3', (a, 1), f'dilutedfreckledextra{i}', sprites_y=2)
#sokoke
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('sokoke', (a, 0), f'sokoke{i}')
    sprites.make_group('sokokeextra', (a, 0), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('sokoke', (a, 1), f'sokoke{i}')
    sprites.make_group('sokokeextra', (a, 1), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('sokoke', (a, 2), f'sokoke{i}')
    sprites.make_group('sokokeextra', (a, 2), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('stersokoke1', (a, 0), f'sokoke{i}')
    sprites.make_group('stersokokeextra1', (a, 0), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('stersokoke1', (a, 1), f'sokoke{i}')
    sprites.make_group('stersokokeextra1', (a, 1), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('stersokoke1', (a, 2), f'sokoke{i}')
    sprites.make_group('stersokokeextra1', (a, 2), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('stersokoke2', (a, 0), f'sokoke{i}')
    sprites.make_group('stersokokeextra2', (a, 0), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('stersokoke2', (a, 1), f'sokoke{i}')
    sprites.make_group('stersokokeextra2', (a, 1), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('stersokoke2', (a, 2), f'sokoke{i}')
    sprites.make_group('stersokokeextra2', (a, 2), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('stersokoke3', (a, 0), f'sokoke{i}')
    sprites.make_group('stersokokeextra3', (a, 0), f'sokokeextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('stersokoke3', (a, 1), f'sokoke{i}')
    sprites.make_group('stersokokeextra3', (a, 1), f'sokokeextra{i}', sprites_y=2)
# darksokoke
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('darksokokecolours', (a, 0), f'darksokoke{i}')
    sprites.make_group('darksokokeextra', (a, 0), f'darksokokeextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('darksokokecolours', (a, 1), f'darksokoke{i}')
    sprites.make_group('darksokokeextra', (a, 1), f'darksokokeextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('darksokokecolours', (a, 2), f'darksokoke{i}')
    sprites.make_group('darksokokeextra', (a, 2), f'darksokokeextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('darksokokecolours2', (a, 0), f'darksokoke{i}')
    sprites.make_group('darksokokeextra2', (a, 0), f'darksokokeextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('darksokokecolours2', (a, 1), f'darksokoke{i}')
    sprites.make_group('darksokokeextra2', (a, 1), f'darksokokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('darksokokecolours2', (a, 2), f'darksokoke{i}')
    sprites.make_group('darksokokeextra2', (a, 2), f'darksokokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('darksokokecolours3', (a, 0), f'darksokoke{i}')
    sprites.make_group('darksokokeextra3', (a, 0), f'darksokokeextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('darksokokecolours3', (a, 1), f'darksokoke{i}')
    sprites.make_group('darksokokeextra3', (a, 1), f'darksokokeextra{i}', sprites_y=2)
# dilutedsokoke
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('sokokedilutecolours', (a, 0), f'dilutedsokoke{i}')
    sprites.make_group('sokokediluteextra', (a, 0), f'dilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('sokokedilutecolours', (a, 1), f'dilutedsokoke{i}')
    sprites.make_group('sokokediluteextra', (a, 1), f'dilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('sokokedilutecolours', (a, 2), f'dilutedsokoke{i}')
    sprites.make_group('sokokediluteextra', (a, 2), f'dilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('sokokedilutecolours2', (a, 0), f'dilutedsokoke{i}')
    sprites.make_group('sokokediluteextra2', (a, 0), f'dilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('sokokedilutecolours2', (a, 1), f'dilutedsokoke{i}')
    sprites.make_group('sokokediluteextra2', (a, 1), f'dilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('sokokedilutecolours2', (a, 2), f'dilutedsokoke{i}')
    sprites.make_group('sokokediluteextra2', (a, 2), f'dilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('sokokedilutecolours3', (a, 0), f'dilutedsokoke{i}')
    sprites.make_group('sokokediluteextra3', (a, 0), f'dilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('sokokedilutecolours3', (a, 1), f'dilutedsokoke{i}')
    sprites.make_group('sokokediluteextra3', (a, 1), f'dilutedsokokeextra{i}', sprites_y=2)
#gradient
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('gradient', (a, 0), f'gradient{i}')
    sprites.make_group('gradientextra', (a, 0), f'gradientextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('gradient', (a, 1), f'gradient{i}')
    sprites.make_group('gradientextra', (a, 1), f'gradientextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('gradient', (a, 2), f'gradient{i}')
    sprites.make_group('gradientextra', (a, 2), f'gradientextra{i}', sprites_y=2)
# tonkinese
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('tonkinesecolours', (a, 0), f'tonkinese{i}')
    sprites.make_group('tonkineseextra', (a, 0), f'tonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('tonkinesecolours', (a, 1), f'tonkinese{i}')
    sprites.make_group('tonkineseextra', (a, 1), f'tonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('tonkinesecolours', (a, 2), f'tonkinese{i}')
    sprites.make_group('tonkineseextra', (a, 2), f'tonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('tonkinesecolours2', (a, 0), f'tonkinese{i}')
    sprites.make_group('tonkineseextra2', (a, 0), f'tonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('tonkinesecolours2', (a, 1), f'tonkinese{i}')
    sprites.make_group('tonkineseextra2', (a, 1), f'tonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('tonkinesecolours2', (a, 2), f'tonkinese{i}')
    sprites.make_group('tonkineseextra2', (a, 2), f'tonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('tonkinesecolours3', (a, 0), f'tonkinese{i}')
    sprites.make_group('tonkineseextra3', (a, 0), f'tonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('tonkinesecolours3', (a, 1), f'tonkinese{i}')
    sprites.make_group('tonkineseextra3', (a, 1), f'tonkineseextra{i}', sprites_y=2)
# dilutedtonkinese
for a, i in enumerate(['WHITE3', 'PALEGREY2', 'LIGHTGREY3', 'GREY3', 'DARKGREY3', 'STONE']):
    sprites.make_group('tonkinesedilutecolours', (a, 0), f'dilutedtonkinese{i}')
    sprites.make_group('tonkinesediluteextra', (a, 0), f'dilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['COAL', 'OBSIDIAN', 'BLACK4', 'PALECREAM', 'CREAM4', 'DARKCREAM2']):
    sprites.make_group('tonkinesedilutecolours', (a, 1), f'dilutedtonkinese{i}')
    sprites.make_group('tonkinesediluteextra', (a, 1), f'dilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['FAWN2', 'TAN', 'LIGHTBROWN3', 'BROWN3', 'CHOCOLATE2', 'DARKBROWN3']):
    sprites.make_group('tonkinesedilutecolours', (a, 2), f'dilutedtonkinese{i}')
    sprites.make_group('tonkinesediluteextra', (a, 2), f'dilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['EBONY1', 'PALEGINGER3', 'LIGHTGINGER3', 'GINGER3', 'FIRE', 'DARKGINGER3']):
    sprites.make_group('tonkinesedilutecolours2', (a, 0), f'dilutedtonkinese{i}')
    sprites.make_group('tonkinesediluteextra2', (a, 0), f'dilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSET', 'RED', 'AUBURN', 'PALELILAC', 'LIGHTLILAC', 'LILAC2']):
    sprites.make_group('tonkinesedilutecolours2', (a, 1), f'dilutedtonkinese{i}')
    sprites.make_group('tonkinesediluteextra2', (a, 1), f'dilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['DARKLILAC', 'ROSE', 'LIGHTGOLD', 'GOLDEN2', 'DARKGOLD', 'HONEY']):
    sprites.make_group('tonkinesedilutecolours2', (a, 2), f'dilutedtonkinese{i}')
    sprites.make_group('tonkinesediluteextra2', (a, 2), f'dilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTSILVER', 'SILVER2', 'DARKSILVER', 'PALEBLUE', 'LIGHTBLUE', 'BLUE1']):
    sprites.make_group('tonkinesedilutecolours3', (a, 0), f'dilutedtonkinese{i}')
    sprites.make_group('tonkinesediluteextra3', (a, 0), f'dilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['RUSSIAN', 'DARKBLUE']):
    sprites.make_group('tonkinesedilutecolours3', (a, 1), f'dilutedtonkinese{i}')
    sprites.make_group('tonkinesediluteextra3', (a, 1), f'dilutedtonkineseextra{i}', sprites_y=2)
#siamese
for a, i in enumerate(['WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'BLACK']):
    sprites.make_group('siamese', (a, 0), f'siamese{i}')
    sprites.make_group('siameseextra', (a, 0), f'siameseextra{i}', sprites_y=2)
for a, i in enumerate(['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER']):
    sprites.make_group('siamese', (a, 1), f'siamese{i}')
    sprites.make_group('siameseextra', (a, 1), f'siameseextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTBROWN', 'BROWN', 'DARKBROWN']):
    sprites.make_group('siamese', (a, 2), f'siamese{i}')
    sprites.make_group('siameseextra', (a, 2), f'siameseextra{i}', sprites_y=2)
# new torties
# solids
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 0), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 0), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 1), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 1), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 2), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 2), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 3), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 3), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecolourssolid', (a, 4), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid', (a, 4), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssolid2', (a, 0), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid2', (a, 0), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssolid2', (a, 1), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid2', (a, 1), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssolid2', (a, 2), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid2', (a, 2), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecolourssolid2', (a, 3), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid2', (a, 3), f'tortiesolidextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecolourssolid2', (a, 4), f'tortiesolid{i}')
    sprites.make_group('tortiesextrasolid2', (a, 4), f'tortiesolidextra{i}', sprites_y=2)
# tabby
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 0), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 0), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 1), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 1), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 2), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 2), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 3), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 3), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecolourstabby', (a, 4), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby', (a, 4), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourstabby2', (a, 0), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby2', (a, 0), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourstabby2', (a, 1), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby2', (a, 1), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourstabby2', (a, 2), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby2', (a, 2), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecolourstabby2', (a, 3), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby2', (a, 3), f'tortietabbyextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecolourstabby2', (a, 4), f'tortietabby{i}')
    sprites.make_group('tortiesextratabby2', (a, 4), f'tortietabbyextra{i}', sprites_y=2)
# dilutedtabby
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourstabbydilute', (a, 0), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute', (a, 0), f'tortiedilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecolourstabbydilute', (a, 1), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute', (a, 1), f'tortiedilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourstabbydilute', (a, 2), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute', (a, 2), f'tortiedilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecolourstabbydilute', (a, 3), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute', (a, 3), f'tortiedilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecolourstabbydilute', (a, 4), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute', (a, 4), f'tortiedilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourstabbydilute2', (a, 0), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute2', (a, 0), f'tortiedilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourstabbydilute2', (a, 1), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute2', (a, 1), f'tortiedilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourstabbydilute2', (a, 2), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute2', (a, 2), f'tortiedilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecolourstabbydilute2', (a, 3), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute2', (a, 3), f'tortiedilutedtabbyextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecolourstabbydilute2', (a, 4), f'tortiedilutedtabby{i}')
    sprites.make_group('tortiesextratabbydilute2', (a, 4), f'tortiedilutedtabbyextra{i}', sprites_y=2)
# bengal
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 0), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 0), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 1), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 1), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 2), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 2), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 3), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 3), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursbengal', (a, 4), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal', (a, 4), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursbengal2', (a, 0), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal2', (a, 0), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursbengal2', (a, 1), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal2', (a, 1), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursbengal2', (a, 2), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal2', (a, 2), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursbengal2', (a, 3), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal2', (a, 3), f'tortiebengalextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursbengal2', (a, 4), f'tortiebengal{i}')
    sprites.make_group('tortiesextrabengal2', (a, 4), f'tortiebengalextra{i}', sprites_y=2)
# dilutedbengal
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursbengaldilute', (a, 0), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute', (a, 0), f'tortiedilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursbengaldilute', (a, 1), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute', (a, 1), f'tortiedilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursbengaldilute', (a, 2), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute', (a, 2), f'tortiedilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursbengaldilute', (a, 3), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute', (a, 3), f'tortiedilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursbengaldilute', (a, 4), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute', (a, 4), f'tortiedilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursbengaldilute2', (a, 0), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute2', (a, 0), f'tortiedilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursbengaldilute2', (a, 1), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute2', (a, 1), f'tortiedilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursbengaldilute2', (a, 2), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute2', (a, 2), f'tortiedilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursbengaldilute2', (a, 3), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute2', (a, 3), f'tortiedilutedbengalextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursbengaldilute2', (a, 4), f'tortiedilutedbengal{i}')
    sprites.make_group('tortiesextrabengaldilute2', (a, 4), f'tortiedilutedbengalextra{i}', sprites_y=2)
# marbled
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 0), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 0), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 1), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 1), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 2), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 2), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 3), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 3), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursmarbled', (a, 4), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled', (a, 4), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursmarbled2', (a, 0), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled2', (a, 0), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursmarbled2', (a, 1), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled2', (a, 1), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursmarbled2', (a, 2), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled2', (a, 2), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursmarbled2', (a, 3), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled2', (a, 3), f'tortiemarbledextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursmarbled2', (a, 4), f'tortiemarbled{i}')
    sprites.make_group('tortiesextramarbled2', (a, 4), f'tortiemarbledextra{i}', sprites_y=2)
# dilutedmarbled
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute', (a, 0), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute', (a, 0), f'tortiedilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute', (a, 1), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute', (a, 1), f'tortiedilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute', (a, 2), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute', (a, 2), f'tortiedilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute', (a, 3), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute', (a, 3), f'tortiedilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute', (a, 4), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute', (a, 4), f'tortiedilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute2', (a, 0), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute2', (a, 0), f'tortiedilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute2', (a, 1), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute2', (a, 1), f'tortiedilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute2', (a, 2), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute2', (a, 2), f'tortiedilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute2', (a, 3), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute2', (a, 3), f'tortiedilutedmarbledextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursmarbleddilute2', (a, 4), f'tortiedilutedmarbled{i}')
    sprites.make_group('tortiesextramarbleddilute2', (a, 4), f'tortiedilutedmarbledextra{i}', sprites_y=2)
# ticked
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 0), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 0), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 1), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 1), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 2), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 2), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 3), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 3), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursticked', (a, 4), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked', (a, 4), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursticked2', (a, 0), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked2', (a, 0), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursticked2', (a, 1), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked2', (a, 1), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursticked2', (a, 2), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked2', (a, 2), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursticked2', (a, 3), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked2', (a, 3), f'tortietickedextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursticked2', (a, 4), f'tortieticked{i}')
    sprites.make_group('tortiesextraticked2', (a, 4), f'tortietickedextra{i}', sprites_y=2)
# tickeddilute
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourstickeddilute', (a, 0), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute', (a, 0), f'tortietickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecolourstickeddilute', (a, 1), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute', (a, 1), f'tortietickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourstickeddilute', (a, 2), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute', (a, 2), f'tortietickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecolourstickeddilute', (a, 3), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute', (a, 3), f'tortietickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecolourstickeddilute', (a, 4), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute', (a, 4), f'tortietickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourstickeddilute2', (a, 0), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute2', (a, 0), f'tortietickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourstickeddilute2', (a, 1), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute2', (a, 1), f'tortietickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourstickeddilute2', (a, 2), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute2', (a, 2), f'tortietickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecolourstickeddilute2', (a, 3), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute2', (a, 3), f'tortietickeddiluteextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecolourstickeddilute2', (a, 4), f'tortietickeddilute{i}')
    sprites.make_group('tortiesextratickeddilute2', (a, 4), f'tortietickeddiluteextra{i}', sprites_y=2)
# smoke
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 0), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 0), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 1), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 1), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 2), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 2), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 3), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 3), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecolourssmoke', (a, 4), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke', (a, 4), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssmoke2', (a, 0), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke2', (a, 0), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssmoke2', (a, 1), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke2', (a, 1), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssmoke2', (a, 2), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke2', (a, 2), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecolourssmoke2', (a, 3), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke2', (a, 3), f'tortiesmokeextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecolourssmoke2', (a, 4), f'tortiesmoke{i}')
    sprites.make_group('tortiesextrasmoke2', (a, 4), f'tortiesmokeextra{i}', sprites_y=2)
# somali
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourssomali', (a, 0), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali', (a, 0), f'tortiesomaliextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecolourssomali', (a, 1), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali', (a, 1), f'tortiesomaliextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssomali', (a, 2), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali', (a, 2), f'tortiesomaliextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecolourssomali', (a, 3), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali', (a, 3), f'tortiesomaliextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecolourssomali', (a, 4), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali', (a, 4), f'tortiesomaliextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssomali2', (a, 0), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali2', (a, 0), f'tortiesomaliextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssomali2', (a, 1), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali2', (a, 1), f'tortiesomaliextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssomali2', (a, 2), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali2', (a, 2), f'tortiesomaliextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecolourssomali2', (a, 3), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali2', (a, 3), f'tortiesomaliextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecolourssomali2', (a, 4), f'tortiesomali{i}')
    sprites.make_group('tortiesextrasomali2', (a, 4), f'tortiesomaliextra{i}', sprites_y=2)
# rosette
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 0), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 0), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 1), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 1), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 2), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 2), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 3), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 3), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursrosette', (a, 4), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette', (a, 4), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursrosette2', (a, 0), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette2', (a, 0), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursrosette2', (a, 1), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette2', (a, 1), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursrosette2', (a, 2), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette2', (a, 2), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursrosette2', (a, 3), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette2', (a, 3), f'tortierosetteextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursrosette2', (a, 4), f'tortierosette{i}')
    sprites.make_group('tortiesextrarosette2', (a, 4), f'tortierosetteextra{i}', sprites_y=2)
# dilutedrosette
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursrosettedilute', (a, 0), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute', (a, 0), f'tortiedilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursrosettedilute', (a, 1), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute', (a, 1), f'tortiedilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursrosettedilute', (a, 2), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute', (a, 2), f'tortiedilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursrosettedilute', (a, 3), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute', (a, 3), f'tortiedilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursrosettedilute', (a, 4), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute', (a, 4), f'tortiedilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursrosettedilute2', (a, 0), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute2', (a, 0), f'tortiedilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursrosettedilute2', (a, 1), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute2', (a, 1), f'tortiedilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursrosettedilute2', (a, 2), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute2', (a, 2), f'tortiedilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursrosettedilute2', (a, 3), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute2', (a, 3), f'tortiedilutedrosetteextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursrosettedilute2', (a, 4), f'tortiedilutedrosette{i}')
    sprites.make_group('tortiesextrarosettedilute2', (a, 4), f'tortiedilutedrosetteextra{i}', sprites_y=2)
# speckled
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 0), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 0), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 1), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 1), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 2), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 2), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 3), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 3), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursspeckled', (a, 4), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled', (a, 4), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursspeckled2', (a, 0), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled2', (a, 0), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursspeckled2', (a, 1), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled2', (a, 1), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursspeckled2', (a, 2), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled2', (a, 2), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursspeckled2', (a, 3), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled2', (a, 3), f'tortiespeckledextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursspeckled2', (a, 4), f'tortiespeckled{i}')
    sprites.make_group('tortiesextraspeckled2', (a, 4), f'tortiespeckledextra{i}', sprites_y=2)
# dilutedspeckled
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute', (a, 0), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute', (a, 0), f'tortiedilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute', (a, 1), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute', (a, 1), f'tortiedilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute', (a, 2), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute', (a, 2), f'tortiedilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute', (a, 3), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute', (a, 3), f'tortiedilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute', (a, 4), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute', (a, 4), f'tortiedilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute2', (a, 0), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute2', (a, 0), f'tortiedilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute2', (a, 1), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute2', (a, 1), f'tortiedilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute2', (a, 2), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute2', (a, 2), f'tortiedilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute2', (a, 3), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute2', (a, 3), f'tortiedilutedspeckledextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursspeckleddilute2', (a, 4), f'tortiedilutedspeckled{i}')
    sprites.make_group('tortiesextraspeckleddilute2', (a, 4), f'tortiedilutedspeckledextra{i}', sprites_y=2)
#merle
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiemerle', (a, 0), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 0), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiemerle', (a, 1), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 1), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiemerle', (a, 2), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 2), f'tortiemerleextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiemerle', (a, 3), f'tortiemerle{i}')
    sprites.make_group('tortiemerleextra', (a, 3), f'tortiemerleextra{i}', sprites_y=2)
#clouded
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortieclouded', (a, 0), f'tortieclouded{i}')
    sprites.make_group('tortiecloudedextra', (a, 0), f'tortiecloudedextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortieclouded', (a, 1), f'tortieclouded{i}')
    sprites.make_group('tortiecloudedextra', (a, 1), f'tortiecloudedextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortieclouded', (a, 2), f'tortieclouded{i}')
    sprites.make_group('tortiecloudedextra', (a, 2), f'tortiecloudedextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortieclouded', (a, 3), f'tortieclouded{i}')
    sprites.make_group('tortiecloudedextra', (a, 3), f'tortiecloudedextra{i}', sprites_y=2)
#snowflake
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiesnowflake', (a, 0), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 0), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiesnowflake', (a, 1), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 1), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiesnowflake', (a, 2), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 2), f'tortiesnowflakeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiesnowflake', (a, 3), f'tortiesnowflake{i}')
    sprites.make_group('tortiesnowflakeextra', (a, 3), f'tortiesnowflakeextra{i}', sprites_y=2)
#ghost
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortieghost', (a, 0), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 0), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortieghost', (a, 1), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 1), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortieghost', (a, 2), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 2), f'tortieghostextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortieghost', (a, 3), f'tortieghost{i}')
    sprites.make_group('tortieghostextra', (a, 3), f'tortieghostextra{i}', sprites_y=2)
#pinstripe
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiepinstripe', (a, 0), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 0), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiepinstripe', (a, 1), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 1), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiepinstripe', (a, 2), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 2), f'tortiepinstripeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiepinstripe', (a, 3), f'tortiepinstripe{i}')
    sprites.make_group('tortiepinstripeextra', (a, 3), f'tortiepinstripeextra{i}', sprites_y=2)
#sokoke
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiesokoke', (a, 0), f'tortiesokoke{i}')
    sprites.make_group('tortiesokokeextra', (a, 0), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiesokoke', (a, 1), f'tortiesokoke{i}')
    sprites.make_group('tortiesokokeextra', (a, 1), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiesokoke', (a, 2), f'tortiesokoke{i}')
    sprites.make_group('tortiesokokeextra', (a, 2), f'tortiesokokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiesokoke', (a, 3), f'tortiesokoke{i}')
    sprites.make_group('tortiesokokeextra', (a, 3), f'tortiesokokeextra{i}', sprites_y=2)
#mackerel
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiemackerel', (a, 0), f'tortiemackerel{i}')
    sprites.make_group('tortiemackerelextra', (a, 0), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiemackerel', (a, 1), f'tortiemackerel{i}')
    sprites.make_group('tortiemackerelextra', (a, 1), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiemackerel', (a, 2), f'tortiemackerel{i}')
    sprites.make_group('tortiemackerelextra', (a, 2), f'tortiemackerelextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiemackerel', (a, 3), f'tortiemackerel{i}')
    sprites.make_group('tortiemackerelextra', (a, 3), f'tortiemackerelextra{i}', sprites_y=2)
#classic
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortieclassic', (a, 0), f'tortieclassic{i}')
    sprites.make_group('tortieclassicextra', (a, 0), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortieclassic', (a, 1), f'tortieclassic{i}')
    sprites.make_group('tortieclassicextra', (a, 1), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortieclassic', (a, 2), f'tortieclassic{i}')
    sprites.make_group('tortieclassicextra', (a, 2), f'tortieclassicextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortieclassic', (a, 3), f'tortieclassic{i}')
    sprites.make_group('tortieclassicextra', (a, 3), f'tortieclassicextra{i}', sprites_y=2)
# freckled
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursfreckled', (a, 0), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled', (a, 0), f'tortiefreckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursfreckled', (a, 1), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled', (a, 1), f'tortiefreckledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursfreckled', (a, 2), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled', (a, 2), f'tortiefreckledextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursfreckled', (a, 3), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled', (a, 3), f'tortiefreckledextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursfreckled', (a, 4), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled', (a, 4), f'tortiefreckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursfreckled2', (a, 0), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled2', (a, 0), f'tortiefreckledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursfreckled2', (a, 1), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled2', (a, 1), f'tortiefreckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursfreckled2', (a, 2), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled2', (a, 2), f'tortiefreckledextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursfreckled2', (a, 3), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled2', (a, 3), f'tortiefreckledextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursfreckled2', (a, 4), f'tortiefreckled{i}')
    sprites.make_group('tortiesextrafreckled2', (a, 4), f'tortiefreckledextra{i}', sprites_y=2)
# dilutedfreckled
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute', (a, 0), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute', (a, 0), f'tortiedilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute', (a, 1), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute', (a, 1), f'tortiedilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute', (a, 2), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute', (a, 2), f'tortiedilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute', (a, 3), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute', (a, 3), f'tortiedilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute', (a, 4), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute', (a, 4), f'tortiedilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute2', (a, 0), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute2', (a, 0), f'tortiedilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute2', (a, 1), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute2', (a, 1), f'tortiedilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute2', (a, 2), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute2', (a, 2), f'tortiedilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute2', (a, 3), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute2', (a, 3), f'tortiedilutedfreckledextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursfreckleddilute2', (a, 4), f'tortiedilutedfreckled{i}')
    sprites.make_group('tortiesextrafreckleddilute2', (a, 4), f'tortiedilutedfreckledextra{i}', sprites_y=2)
# dilutedclassic
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursclassicdilute', (a, 0), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute', (a, 0), f'tortiedilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursclassicdilute', (a, 1), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute', (a, 1), f'tortiedilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursclassicdilute', (a, 2), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute', (a, 2), f'tortiedilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursclassicdilute', (a, 3), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute', (a, 3), f'tortiedilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursclassicdilute', (a, 4), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute', (a, 4), f'tortiedilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursclassicdilute2', (a, 0), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute2', (a, 0), f'tortiedilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursclassicdilute2', (a, 1), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute2', (a, 1), f'tortiedilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursclassicdilute2', (a, 2), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute2', (a, 2), f'tortiedilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursclassicdilute2', (a, 3), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute2', (a, 3), f'tortiedilutedclassicextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursclassicdilute2', (a, 4), f'tortiedilutedclassic{i}')
    sprites.make_group('tortiesextraclassicdilute2', (a, 4), f'tortiedilutedclassicextra{i}', sprites_y=2)
# dilutedsokoke
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourssokokedilute', (a, 0), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute', (a, 0), f'tortiedilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecolourssokokedilute', (a, 1), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute', (a, 1), f'tortiedilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourssokokedilute', (a, 2), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute', (a, 2), f'tortiedilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecolourssokokedilute', (a, 3), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute', (a, 3), f'tortiedilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecolourssokokedilute', (a, 4), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute', (a, 4), f'tortiedilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourssokokedilute2', (a, 0), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute2', (a, 0), f'tortiedilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourssokokedilute2', (a, 1), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute2', (a, 1), f'tortiedilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourssokokedilute2', (a, 2), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute2', (a, 2), f'tortiedilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecolourssokokedilute2', (a, 3), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute2', (a, 3), f'tortiedilutedsokokeextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecolourssokokedilute2', (a, 4), f'tortiedilutedsokoke{i}')
    sprites.make_group('tortiesextrasokokedilute2', (a, 4), f'tortiedilutedsokokeextra{i}', sprites_y=2)
# mackereldilute
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecoloursmackereldilute', (a, 0), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute', (a, 0), f'tortiemackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecoloursmackereldilute', (a, 1), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute', (a, 1), f'tortiemackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecoloursmackereldilute', (a, 2), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute', (a, 2), f'tortiemackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecoloursmackereldilute', (a, 3), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute', (a, 3), f'tortiemackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecoloursmackereldilute', (a, 4), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute', (a, 4), f'tortiemackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecoloursmackereldilute2', (a, 0), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute2', (a, 0), f'tortiemackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecoloursmackereldilute2', (a, 1), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute2', (a, 1), f'tortiemackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecoloursmackereldilute2', (a, 2), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute2', (a, 2), f'tortiemackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecoloursmackereldilute2', (a, 3), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute2', (a, 3), f'tortiemackereldiluteextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecoloursmackereldilute2', (a, 4), f'tortiemackereldilute{i}')
    sprites.make_group('tortiesextramackereldilute2', (a, 4), f'tortiemackereldiluteextra{i}', sprites_y=2)
# tonkinese
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourstonkinese', (a, 0), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese', (a, 0), f'tortietonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecolourstonkinese', (a, 1), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese', (a, 1), f'tortietonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourstonkinese', (a, 2), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese', (a, 2), f'tortietonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecolourstonkinese', (a, 3), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese', (a, 3), f'tortietonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecolourstonkinese', (a, 4), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese', (a, 4), f'tortietonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourstonkinese2', (a, 0), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese2', (a, 0), f'tortietonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourstonkinese2', (a, 1), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese2', (a, 1), f'tortietonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourstonkinese2', (a, 2), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese2', (a, 2), f'tortietonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecolourstonkinese2', (a, 3), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese2', (a, 3), f'tortietonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecolourstonkinese2', (a, 4), f'tortietonkinese{i}')
    sprites.make_group('tortiesextratonkinese2', (a, 4), f'tortietonkineseextra{i}', sprites_y=2)
# dilutedtonkinese
for a, i in enumerate(['CREAMONE', 'CREAMTWO', 'CREAMTHREE', 'CREAMFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute', (a, 0), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute', (a, 0), f'tortiedilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['LIGHTGOLDONE', 'LIGHTGOLDTWO', 'LIGHTGOLDTHREE', 'LIGHTGOLDFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute', (a, 1), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute', (a, 1), f'tortiedilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['GOLDONE', 'GOLDTWO', 'GOLDTHREE', 'GOLDFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute', (a, 2), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute', (a, 2), f'tortiedilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['HONEYONE', 'HONEYTWO', 'HONEYTHREE', 'HONEYFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute', (a, 3), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute', (a, 3), f'tortiedilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['FIREONE', 'FIRETWO', 'FIRETHREE', 'FIREFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute', (a, 4), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute', (a, 4), f'tortiedilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['PALEONE', 'PALETWO', 'PALETHREE', 'PALEFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute2', (a, 0), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute2', (a, 0), f'tortiedilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['GINGERONE', 'GINGERTWO', 'GINGERTHREE', 'GINGERFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute2', (a, 1), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute2', (a, 1), f'tortiedilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['DARKONE', 'DARKTWO', 'DARKTHREE', 'DARKFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute2', (a, 2), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute2', (a, 2), f'tortiedilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['REDONE', 'REDTWO', 'REDTHREE', 'REDFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute2', (a, 3), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute2', (a, 3), f'tortiedilutedtonkineseextra{i}', sprites_y=2)
for a, i in enumerate(['COCOAONE', 'COCOATWO', 'COCOATHREE', 'COCOAFOUR']):
    sprites.make_group('tortiecolourstonkinesedilute2', (a, 4), f'tortiedilutedtonkinese{i}')
    sprites.make_group('tortiesextratonkinesedilute2', (a, 4), f'tortiedilutedtonkineseextra{i}', sprites_y=2)

# SKINS
sprites.make_group('skin', (0, 0), 'skinBLACK')
sprites.make_group('skin', (1, 0), 'skinRED')
sprites.make_group('skin', (2, 0), 'skinPINK')
sprites.make_group('skin', (3, 0), 'skinDARKBROWN')
sprites.make_group('skin', (4, 0), 'skinBROWN')
sprites.make_group('skin', (5, 0), 'skinLIGHTBROWN')
sprites.make_group('skin', (0, 1), 'skinDARK')
sprites.make_group('skin', (1, 1), 'skinDARKGREY')
sprites.make_group('skin', (2, 1), 'skinGREY')
sprites.make_group('skin', (3, 1), 'skinDARKSALMON')
sprites.make_group('skin', (4, 1), 'skinSALMON')
sprites.make_group('skin', (5, 1), 'skinPEACH')
sprites.make_group('skin', (0, 2), 'skinDARKMARBLED')
sprites.make_group('skin', (1, 2), 'skinMARBLED')
sprites.make_group('skin', (2, 2), 'skinLIGHTMARBLED')
sprites.make_group('skin', (3, 2), 'skinDARKBLUE')
sprites.make_group('skin', (4, 2), 'skinBLUE')
sprites.make_group('skin', (5, 2), 'skinLIGHTBLUE')
sprites.make_group('skin2', (0, 0), 'skinALBINOPINK')
sprites.make_group('skin2', (1, 0), 'skinALBINOBLUE')
sprites.make_group('skin2', (2, 0), 'skinALBINORED')
sprites.make_group('skin2', (3, 0), 'skinALBINOVIOLET')
sprites.make_group('skin2', (0, 1), 'skinMELANISTICLIGHT')
sprites.make_group('skin2', (1, 1), 'skinMELANISTIC')
sprites.make_group('skin2', (2, 1), 'skinMELANISTICDARK')
sprites.make_group('skinparalyzed', (0, 0),
                   'skinparalyzedPINK',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('skinparalyzed', (1, 0),
                   'skinparalyzedRED',
                   sprites_x=1,
                   sprites_y=1)
sprites.make_group('skinparalyzed', (2, 0),
                   'skinparalyzedBLACK',
                   sprites_x=1,
                   sprites_y=1)

sprites.make_group('skinextra', (0, 0), 'skinextraBLACK', sprites_y=2)
sprites.make_group('skinextra', (1, 0), 'skinextraRED', sprites_y=2)
sprites.make_group('skinextra', (2, 0), 'skinextraPINK', sprites_y=2)
sprites.make_group('skinextra', (3, 0), 'skinextraDARKBROWN', sprites_y=2)
sprites.make_group('skinextra', (4, 0), 'skinextraBROWN', sprites_y=2)
sprites.make_group('skinextra', (5, 0), 'skinextraLIGHTBROWN', sprites_y=2)
sprites.make_group('skinextra', (0, 1), 'skinextraDARK', sprites_y=2)
sprites.make_group('skinextra', (1, 1), 'skinextraDARKGREY', sprites_y=2)
sprites.make_group('skinextra', (2, 1), 'skinextraGREY', sprites_y=2)
sprites.make_group('skinextra', (3, 1), 'skinextraDARKSALMON', sprites_y=2)
sprites.make_group('skinextra', (4, 1), 'skinextraSALMON', sprites_y=2)
sprites.make_group('skinextra', (5, 1), 'skinextraPEACH', sprites_y=2)
sprites.make_group('skinextra', (0, 2), 'skinextraDARKMARBLED', sprites_y=2)
sprites.make_group('skinextra', (1, 2), 'skinextraMARBLED', sprites_y=2)
sprites.make_group('skinextra', (2, 2), 'skinextraLIGHTMARBLED', sprites_y=2)
sprites.make_group('skinextra', (3, 2), 'skinextraDARKBLUE', sprites_y=2)
sprites.make_group('skinextra', (4, 2), 'skinextraBLUE', sprites_y=2)
sprites.make_group('skinextra', (5, 2), 'skinextraLIGHTBLUE', sprites_y=2)
sprites.make_group('skin2extra', (0, 0), 'skinextraALBINOPINK', sprites_y=2)
sprites.make_group('skin2extra', (1, 0), 'skinextraALBINOBLUE', sprites_y=2)
sprites.make_group('skin2extra', (2, 0), 'skinextraALBINORED', sprites_y=2)
sprites.make_group('skin2extra', (3, 0), 'skinextraALBINOVIOLET', sprites_y=2)
sprites.make_group('skin2extra', (0, 1), 'skinextraMELANISTICLIGHT', sprites_y=2)
sprites.make_group('skin2extra', (1, 1), 'skinextraMELANISTIC', sprites_y=2)
sprites.make_group('skin2extra', (2, 1), 'skinextraMELANISTICDARK', sprites_y=2)

# tiles.make_group('dithered', (0, 0), 'terrain')
# tiles.make_group('dithered', (1, 0), 'terraintwo')

sprites.load_scars()

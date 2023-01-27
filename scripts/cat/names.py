import random
import os


class Name():
    special_suffixes = {
        "kitten": "kit",
        "apprentice": "paw",
        "medicine cat apprentice": "paw",
        "leader": "star"
    }
    normal_suffixes = [  # common suffixes
        "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", 'fur', 'fur', 'fur',
        "tuft", "tuft", "tuft", "tuft", "tuft", "tooth", "tooth", "tooth", "tooth", "tooth",
        'pelt', "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt",
        "tail", "tail", "tail", "tail", "tail", "tail", "tail", "tail", "claw", "claw", "claw", "claw", "claw", "claw", "claw",
        "foot", "foot", "foot", "foot", "foot", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker",
        "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", 'heart', "fang", "fang", "fang", "fang"

        # regular suffixes
        "acorn", "ash", "aster", "back", "beam", "bee", "belly", "berry", "bite", "bird", "blaze", "blink",
        "blossom", "bloom", "blotch", "bounce", "branch", "breeze", "briar", "bright", "brook", "burr", "bush",
        "call", "cloud", "clover", "coral", "creek", "cry", "dapple", "daisy", "dawn", "drift", "drop",
        "dusk", "dust", "ear", "ears", "eye", "eyes", "face", "fall", "fang", "feather", "fern", "fin", "fire",
        "fish", "flame", "flight", "flood", "flower", "frost", "gaze", "goose", "gorse", "grass", "hail", "hare", 
        "hawk", "haze", "heather", "holly", "hollow", "ivy", "jaw", "jay", "jump", "kite",
        "lake", "larch", "leaf", "leap", "leg", "light", "lilac", "lily", "lotus", "mask", "mist", "moth",
        "moon", "mouse", "needle", "nettle", "night", "noise", "nose", "nut", "pad", "path", "patch",
        "petal", "pond", "pool", "poppy", "pounce", "puddle", "rapid", "rose", "rump", "run", "runner",
        "scar", "seed", "shade", "shadow", "shell", "shine", "sight", "skip", "sky", "slip", "snow", "song", 
        "spark", "speck", "speckle", "spirit", "splash", "spot", "spots", "spring", "stalk", "stem", "step",
        "stone", "storm", "streak", "stream", "strike", "stripe", "sun", "swipe", "swoop",
        "tail", "tree", "throat", "tuft", "watcher", "water", "whisper", "willow", "wind", "wing", "wish"
        'adder', 'alder', 'amble', 'ant', 'antler', 'apple', 'apricot', 'arc', 'arch', 'aspen', 'badger', 'bark',
        'barley', 'bat', 'bay', 'beaver', 'beech', 'beetle', 'belladonna', 'beyond', 'birch', 'blizzard', 'bog',
        'bolt', 'borage', 'bough', 'boulder', 'bound', 'bracken', 'bramble', 'bristle', 'brush', 'buck', 'bug',
        'bumble', 'burdock', 'burn', 'burrow', 'bush', 'buzzard', 'carp', 'catch', 'catcher', 'cedar',
        'char', 'charge', 'chatter', 'cheetah', 'cherry', 'chestnut', 'chive', 'cinder', 'cinnamon', 'clematis',
        'clue', 'cone', 'cress', 'cricket', 'crouch', 'crow', 'curl', 'cypress', 'dance', 'damp', 'dark', 'dash',
        'deer', 'dew', 'ditch', 'doe', 'dog', 'dots', 'dove', 'down', 'dream', 'dreamer', 'dry', 'duck', 'eagle',
        'echo', 'eel', 'elm', 'ember', 'ermine', 'fade', 'fallow', 'fawn', 'fennel', 'ferret', 'finch', 'fir', 'fisher',
        'flake', 'flail', 'flare', 'flash', 'flax', 'flicker', 'flint', 'flip', 'flutter', 'fly', 'fog', 'fox', 'freckle', 'freckles',
        'freeze', 'frog', 'frond', 'fur', 'fuzz', 'gleam', 'glide', 'glimmer', 'glow', 'gravel', 'ground',
        'gull', 'half', 'hare', 'harrier', 'hatch', 'hay', 'hedge', 'hemlock', 'heron', 'hickory', 'hill', 'hills',
        'honey', 'hoot', 'hop', 'hope', 'hopper', 'horse', 'hound', 'hunter', 'ice', 'inferno', 'jackdaw', 'jumper',
        'kestrel', 'kindle', 'knap', 'land', 'lantana', 'lark', 'larkspur', 'laurel', 'lavender', 'leaper', 'lemon', 'leopard',
        'lichen', 'lightning', 'lime', 'lion', 'lizard', 'log', 'lunge', 'lynx', 'maggot', 'mallow', 'maple', 'march', 'marcher',
        'marigold', 'marsh', 'martin', 'meadow', 'midge', 'milk', 'minnow', 'mint', 'mistle', 'mole', 'morning', 'moss',
        'mottle', 'moose', 'mud', 'mumble', 'murmur', 'nectar', 'nightshade', 'newt', 'oak', 'oat', 'oleander', 'olive', 'orange',
        'otter', 'owl', 'panther', 'parsley', 'patches', 'peak', 'pear', 'peat', 'pebble', 'peony', 'perch', 'pheasant', 'pigeon', 'pike',
        'pine', 'plum', 'pod', 'prance', 'prickle', 'primrose', 'python', 'quail', 'rabbit', 'rain', 'rat', 'raven', 'reed', 'ridge',
        'ripple', 'rise', 'river', 'roar', 'robin', 'rock', 'rook', 'root', 'rover', 'rowan', 'rubble', 'rush', 'rusher', 'rust', 'rye', 'sage',
        'salmon', 'sand', 'scamper', 'scorch', 'scramble', 'scuttle', 'sedge', 'seer', 'sheep', 'shimmer', 'shine', 'shrew', 'shy',
        'silence', 'silt', 'skitter', 'slate', 'sleet', 'sloe', 'slope', 'smoke', 'snail', 'snake', 'snap', 'snapper', 'snarl', 'sneeze', 'snip',
        'snout', 'soot', 'sorrel', 'sparrow', 'speckles', 'specks', 'spider', 'spike', 'spire', 'sprint', 'sprout', 'spruce', 'squirrel', 'stag',
        'starling', 'stoat', 'stride', 'stork', 'stump', 'swallow', 'swamp', 'swan', 'sweet', 'swift', 'swirl', 'talon', 'tear', 'thicket', 'thistle',
        'thrift', 'thorn', 'thunder', 'thyme', 'tiger', 'timber', 'tip', 'toe', 'torrent', 'tooth', 'trail', 'traipse', 'travel', 'traveler', 'trot', 'trout',
        'tulip', 'tumble', 'turtle', 'tussock', 'twig', 'twirl', 'vine', 'violet', 'vixen', 'vole', 'walk', 'walker', 'wander', 'wanderer', 'wasp',
        'warren', 'water', 'weasel', 'weed', 'wheat', 'whistle', 'whistler', 'wiggle', 'wither', 'wonder', 'wood', 'wort', 'wound',
        'wounder', 'wren', 'yarrow', 'yew', 'yonder', 'zinnia'
    ]

    pelt_suffixes = {
        'TwoColour': ['patch', 'spot', 'splash', 'patch', 'spots'],
        'Tabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Marbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Speckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'Bengal': ['dapple', 'speckle', 'spots', 'speck', 'freckle'],
        'Tortie': ['dapple', 'speckle', 'spot', 'dapple'],
        'Rosette': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'Calico': ['stripe', 'dapple', 'patch', 'patch'],
        'Smoke': ['fade', 'dusk', 'dawn', 'smoke'],
        'Ticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'Ragdoll': ['mask', 'feather', 'willow', 'patch', 'tail'],
        'Shaded': ['shade', 'tip', 'feather', 'face', 'mask', 'tip'],
        'DarkTabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DilutedTabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DarkMarbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DilutedMarbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DarkSpeckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'DilutedSpeckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'DarkBengal': ['dapple', 'speckle', 'spots', 'speck', 'freckle'],
        'DilutedBengal': ['dapple', 'speckle', 'spots', 'speck', 'freckle'],
        'DarkRosette': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'DilutedRosette': ['dapple', 'speckle', 'spots', 'dapple', 'freckle'],
        'DilutedTicked': ['spots', 'pelt', 'speckle', 'freckle'],
        'Freckled': ['spots', 'pelt', 'speckle', 'freckle'],
        'DilutedFreckled': ['spots', 'pelt', 'speckle', 'freckle'],
        'Sokoke': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DarkSokoke': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DilutedSokoke': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Classic': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DarkClassic': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DilutedClassic': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Mackerel': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DarkMackerel': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'DilutedMackerel': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Tonkinese': ['fade', 'dusk', 'dawn', 'smoke'],
        'DilutedTonkinese': ['fade', 'dusk', 'dawn', 'smoke'],
        'Somali': ['stripe', 'back', 'streak', 'spine', 'line'],
        'Abyssinian': ['fade', 'dusk', 'dawn', 'smoke'],
        'Merle': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'dog', 'hound'],
        'Clouded': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Snowflake': ['dapple', 'speckle', 'spot', 'speck', 'freckle', 'snow', 'snowflake'],
        'Doberman': ['patch', 'spot', 'splash', 'patch', 'spots', 'hound', 'dog'],
        'Ghost': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'ghost'],
        'Pinstripe': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Spotted': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'Cloudy': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Gradient': ['fade', 'dusk', 'dawn', 'smoke'],
        'Ponit': ['fade', 'dusk', 'dawn', 'smoke'],
        'Agouti': ['back', 'pelt', 'fur']
    }

    tortie_pelt_suffixes = {
        'tortiesolid': ['dapple', 'speckle', 'spots', 'splash'],
        'tortietabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiebengal': ['dapple', 'speckle', 'spots', 'speck', 'fern', 'freckle'],
        'tortiemarbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortieticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'tortiesmoke': ['fade', 'dusk', 'dawn', 'smoke'],
        'tortierosette': ['dapple', 'speckle', 'spots', 'dapple', 'fern', 'freckle'],
        'tortiespeckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'tortiemerle': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'dog', 'hound'],
        'tortieclouded': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'tortiesnowflake': ['dapple', 'speckle', 'spot', 'speck', 'freckle', 'snow', 'snowflake'],
        'tortieghost': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'ghost'],
        'tortiepinstripe': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'tortieclassic': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiemackerel': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiesokoke': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiedilutedtabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiedilutedbengal': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiedilutedmarbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortietickeddilute': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiesomali': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiedilutedrosette': ['spots', 'leopard', 'cheetah', 'spot', 'speckle', 'speckles', 'splotch'],
        'tortiedilutedclassic': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiedilutedsokoke': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiemackereldilute': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortietonkinese': ['fade', 'dusk', 'dawn', 'smoke', 'stripe'],
        'tortiedilutedtonkinese': ['fade', 'dusk', 'dawn', 'smoke']
    }

    normal_prefixes = [
        'Acacia', 'Acorn', 'Adder', 'Alder', 'Algae', 'Almond', 'Aloe', 'Amber', 'Ant', 'Antler', 'Apple', 'Apricot', 'Arc', 'Arch', 'Arctic',
        'Ash', 'Ashen', 'Aspen', 'Aster', 'Aster', 'Autumn', 'Badger', 'Bark', 'Barley', 'Barley', 'Basil', 'Bass', 'Bat', 'Bay', 'Bayou', 'Beam',
        'Bear', 'Beaver', 'Bee', 'Beech', 'Beetle', 'Berry', 'Big', 'Birch', 'Bird', 'Bite', 'Bitter', 'Bittern', 'Blaze', 'Bleak', 'Blight',
        'Blink', 'Bliss', 'Bloom', 'Blossom', 'Blotch', 'Bluff', 'Bog', 'Bog', 'Bold', 'Borage', 'Bough', 'Boulder', 'Bounce', 'Bracken', 'Bramble',
        'Branch', 'Brave', 'Breeze', 'Breeze', 'Briar', 'Bright', 'Brindle', 'Bristle', 'Broken', 'Brook', 'Brush', 'Bubble', 'Bubbling', 'Buck',
        'Bug', 'Bumble', 'Burdock', 'Burn', 'Burnt', 'Burr', 'Bush', 'Buzzard', 'Carp', 'Cedar', 'Cedar', 'Chaffinch', 'Char', 'Cheetah', 'Cherry',
        'Chestnut', 'Chive', 'Cicada', 'Cinder', 'Cinnamon', 'Claw', 'Clay', 'Cliff', 'Cloud', 'Clover', 'Clover', 'Coast', 'Cobra', 'Cod', 'Cold',
        'Condor', 'Cone', 'Conifer', 'Copper', 'Cotton', 'Cougar', 'Cow', 'Coyote', 'Crab', 'Crag', 'Crane', 'Creek', 'Cress', 'Crested',
        'Cricket', 'Crooked', 'Crouch', 'Crow', 'Crow', 'Curl', 'Curlew', 'Curly', 'Cypress', 'Dahlia', 'Daisy', 'Damp', 'Dapple', 'Dappled',
        'Dark', 'Dawn', 'Dawn', 'Day', 'Dead', 'Deer', 'Dew', 'Doe', 'Dog', 'Dove', 'Down', 'Downy', 'Drake', 'Drift', 'Drizzle', 'Drought', 'Dry',
        'Duck', 'Dull', 'Dune', 'Dusk', 'Dust', 'Eagle', 'Echo', 'Eel', 'Egret', 'Elk', 'Elm', 'Ember', 'Ermine', 'Faded', 'Faded', 'Fading', 'Falcon',
        'Fallen', 'Fallow', 'Fawn', 'Feather', 'Fennel', 'Fern', 'Ferret', 'Fidget', 'Fierce', 'Fin', 'Finch', 'Fir', 'Fish', 'Flail', 'Flame', 'Flash', 'Flax',
        'Fleck', 'Fleet', 'Flicker', 'Flight', 'Flint', 'Flip', 'Flood', 'Flood', 'Flower', 'Flower', 'Flurry', 'Flutter', 'Fly', 'Foam', 'Forest', 'Fox', 'Freckle',
        'Freeze', 'Fringe', 'Frog', 'Frond', 'Frost', 'Frozen', 'Furled', 'Fuzzy', 'Gander', 'Gannet', 'Gem', 'Giant', 'Gill', 'Gleam', 'Glow',
        'Goose', 'Gorge', 'Gorse', 'Grass', 'Gravel', 'Grouse', 'Gull', 'Gust', 'Hail', 'Half', 'Hare', 'Harvest', 'Hatch', 'Hawk', 'Hay', 'Haze',
        'Heath', 'Heather', 'Heavy', 'Hedge', 'Hen', 'Heron', 'Hickory', 'Hill', 'Hoarse', 'Hollow', 'Holly', 'Hoot', 'Hop', 'Hope', 'Hornet',
        'Hound', 'Ice', 'Icy', 'Iris', 'Ivy', 'Jagged', 'Jasper', 'Jay', 'Jet', 'Jump', 'Juniper', 'Kestrel', 'Kink', 'Kite', 'Lake', 'Larch', 'Lark',
        'Laurel', 'Lavender', 'Leaf', 'Leap', 'Leopard', 'Lichen', 'Light', 'Lightning', 'Lilac', 'Lilac', 'Lily', 'Little', 'Lizard', 'Locust',
        'Log', 'Long', 'Lost', 'Lotus', 'Loud', 'Low', 'Lynx', 'Maggot', 'Mallow', 'Mantis', 'Maple', 'Marigold', 'Marsh', 'Marten', 'Meadow',
        'Mellow', 'Merry', 'Midge', 'Milk', 'Mink', 'Minnow', 'Mint', 'Mist', 'Mistle', 'Misty', 'Mite', 'Mock', 'Mole', 'Mole', 'Moon', 'Moor',
        'Morning', 'Moss', 'Mossy', 'Moth', 'Moth', 'Mottle', 'Mottled', 'Mouse', 'Mouse', 'Mud', 'Mumble', 'Murk', 'Nacre', 'Narrow', 'Nectar',
        'Needle', 'Nettle', 'Newt', 'Night', 'Nut', 'Oak', 'Oat', 'Odd', 'One', 'Orange', 'Osprey', 'Otter', 'Owl', 'Pale', 'Pansy', 'Panther',
        'Parsley', 'Partridge', 'Patch', 'Peak', 'Pear', 'Peat', 'Peat', 'Pebble', 'Pepper', 'Perch', 'Petal', 'Pheasant', 'Pigeon', 'Pike',
        'Pine', 'Piper', 'Plover', 'Pod', 'Pond', 'Pool', 'Poppy', 'Posy', 'Pounce', 'Prance', 'Prickle', 'Prim', 'Puddle', 'Python', 'Quail',
        'Quick', 'Quiet', 'Quill', 'Rabbit', 'Raccoon', 'Ragged', 'Rain', 'Rambling', 'Rat', 'Rattle', 'Raven', 'Reed', 'Ridge', 'Rift',
        'Ripple', 'River', 'Roach', 'Robin', 'Rock', 'Rook', 'Root', 'Rose', 'Rosy', 'Rot', 'Rowan', 'Rubble', 'Running', 'Rush', 'Rust', 'Rye',
        'Sage', 'Sandy', 'Scar', 'Scorch', 'Sea', 'Sedge', 'Seed', 'Shade', 'Shard', 'Sharp', 'Shell', 'Shimmer', 'Short', 'Shrew', 'Shy', 'Silk',
        'Silt', 'Skip', 'Sky', 'Slate', 'Sleek', 'Sleet', 'Slight', 'Sloe', 'Slope', 'Small', 'Smoke', 'Smoky', 'Snail', 'Snake', 'Snap', 'Sneeze',
        'Snip', 'Soft', 'Song', 'Soot', 'Sorrel', 'Spark', 'Sparrow', 'Speckle', 'Spider', 'Spike', 'Spire', 'Splash', 'Spotted', 'Spring',
        'Spruce', 'Squirrel', 'Stag', 'Starling', 'Steam', 'Stoat', 'Stone', 'Stork', 'Storm', 'Stream', 'Strike', 'Stump', 'Swallow', 'Swamp',
        'Swan', 'Sweet', 'Swift', 'Tall', 'Talon', 'Thistle', 'Thorn', 'Thrift', 'Thyme', 'Tiger', 'Timber', 'Tip', 'Toad', 'Torn', 'Trout',
        'Tuft', 'Tulip', 'Tumble', 'Turtle', 'Twig', 'Vine', 'Violet', 'Vixen', 'Vole', 'Warm', 'Wasp', 'Weasel', 'Web', 'Weed', 'Wet', 'Wheat', 'Whirl',
        'Whisker', 'Wild', 'Willow', 'Wind', 'Wisteria', 'Wolf', 'Wood', 'Wren', 'Yarrow', 'Yew', 'Aardvark', 'Aardwolf', 'Agaric', 'Albatross',
        'Alfalfa', 'Algae', 'Almond', 'Aloe', 'Amanita', 'Amber', 'Antler', 'Aphid', 'Apricot', 'Arc', 'Arching', 'Arctic', 'Arid', 'Arnica', 'Ashen',
        'Asphodel', 'Aster', 'Auburn', 'Avocet', 'Azalea', 'Bald', 'Barking', 'Barley', 'Basil', 'Bass', 'Beam', 'Beaming',
        'Bear', 'Bearberry', 'Beck', 'Belladonna', 'Bergamot', 'Betony', 'Beyond', 'Bison', 'Bistort',
        'Biting', 'Bitten', 'Bittern', 'Blaze', 'Bleak', 'Blink', 'Blinking', 'Blooming', 'Blossoming', 'Blotch',
        'Blotched', 'Blotchy', 'Bluebell', 'Boar', 'Bog', 'Bold', 'Bolete', 'Bolt', 'Bone', 'Bough', 'Bouncing',
        'Bounding', 'Brambling', 'Branching', 'Brazen', 'Bream', 'Breeze', 'Breezy', 'Brindled', 'Brine', 'Bristling',
        'Broom', 'Brush', 'Buck', 'Buffalo', 'Bugloss', 'Bumbling', 'Bunchberry', 'Bunting', 'Burn', 'Burned', 'Burnet',
        'Burning', 'Burnt', 'Burr', 'Burrow', 'Bush', 'Bushy', 'Butterbur', 'Buzz', 'Buzzing', 'Calling', 'Campion', 'Cardinal',
        'Carnation', 'Carp', 'Carrot', 'Catamount', 'Catkin', 'Cave', 'Chamomile', 'Chanterelle', 'Char', 'Charlock', 'Charred',
        'Chervil', 'Chick', 'Chickadee', 'Chicken', 'Chicory', 'Chipmunk', 'Chirp', 'Chrysalis', 'Chub', 'Cicada', 'Cindered',
        'Cindering', 'Cinquefoil', 'Clam', 'Clawed', 'Clawing', 'Clematis', 'Clouded', 'Cloudy', 'Coal', 'Comandra', 'Comfrey',
        'Coral', 'Cormorant', 'Cotton', 'Cougar', 'Coyote', 'Crab', 'Crag', 'Crane', 'Cream', 'Cress', 'Crocus', 'Crouched', 'Crouching',
        'Crying', 'Curlew', 'Curling', 'Currant', 'Dace', 'Daffodil', 'Dahlia', 'Damp', 'Dance', 'Dancing', 'Dandelion', 'Dapperling',
        'Dappled', 'Darkened', 'Darkening', 'Darling', 'Darner', 'Darter', 'Dash', 'Dawning', 'Deathcamas', 'Dewy', 'Dill', 'Dipper',
        'Ditch', 'Dock', 'Dog', 'Dot', 'Dotted', 'Downy', 'Dream', 'Dreamy', 'Dreaming', 'Drifted', 'Drifting', 'Driftwood', 'Drizzle',
        'Drop', 'Dropped', 'Dropping', 'Dry', 'Dune', 'Dunlin', 'Echoing', 'Eerie', 'Egg', 'Egret', 'Eider', 'Elder', 'Elk', 'Ermine', 'Evening',
        'Ewe', 'Fade', 'Faded', 'Fading', 'Falcon', 'Falling', 'Fang', 'Feathery', 'Fen', 'Field', 'Fiery', 'Fig', 'Fir', 'Fireweed', 'Fish', 'Fisher',
        'Fishy', 'Flailing', 'Flaming', 'Flare', 'Flashing', 'Flat', 'Flickering', 'Flight', 'Flighty', 'Flipped', 'Flipping', 'Flood', 'Flooded', 'Flooding',
        'Flowering', 'Flowery', 'Flurry', 'Fluttering', 'Fluttery', 'Flying', 'Fogging', 'Foggy', 'Forest', 'Freckled', 'Freeze', 'Freezing', 'Fritillary',
        'Frosted', 'Frosting', 'Frosty', 'Fumitory', 'Funnel', 'Galerina', 'Gannet', 'Garlic', 'Garter', 'Ginger', 'Ginkgo', 'Ginseng', 'Glade', 'Gleam',
        'Gleaming', 'Glimmer', 'Glimmering', 'Glory', 'Glow', 'Glowing', 'Gnarl', 'Gnarled', 'Goat', 'Gorge', 'Goshawk', 'Grackle', 'Grape', 'Grassy',
        'Gravely', 'Grayling', 'Grebe', 'Grisette', 'Grotto', 'Ground', 'Grounded', 'Grouse', 'Grove', 'Gulch', 'Gunnel', 'Gyrfalcon', 'Hailing', 'Halcyon',
        'Harrier', 'Hart', 'Harvest', 'Hatching', 'Hawker', 'Hawthorn', 'Heath', 'Hedge', 'Hedgenettle', 'Hemlock', 'Hen', 'Herring', 'Hilly', 'Hind',
        'Hooting', 'Hopping', 'Hornet', 'Howl', 'Howler', 'Howling', 'Humble', 'Hyacinth', 'Hyssop',
        'Icy', 'Ink', 'Inferno', 'Jackdaw', 'Jagged', 'Jumping', 'Kindle', 'Kinked', 'Knap', 'Koi', 'Labrador',
        'Land', 'Lantana', 'Larkspur', 'Leafy', 'Lemming', 'Lemon', 'Lightened', 'Lightening', 'Lilac', 'Lime',
        'Limpet', 'Lingonberry', 'Loch', 'Loon', 'Lotus', 'Lupine', 'Maggot', 'Magpie', 'Marshy', 'Marmot', 'Marten',
        'Mask', 'Masked', 'Mellow', 'Merlin', 'Mink', 'Minty', 'Misted', 'Misting', 'Mistletoe', 'Moor', 'Moose', 'Mottled',
        'Mountain', 'Muddle', 'Muddled', 'Muddy', 'Mumble', 'Mumbling', 'Murky', 'Nacre', 'Nightshade', 'Noisy', 'Nutty',
        'Oleander', 'Orange', 'Orchid', 'Oriole', 'Osprey', 'Oyster', 'Paling', 'Pasqueflower', 'Patched', 'Patchy', 'Path', 'Peach',
        'Peak', 'Peat', 'Peony', 'Pepper', 'Perching', 'Pheasant', 'Piper', 'Plover', 'Pond', 'Pool', 'Pooling', 'Poplar', 'Pouncing',
        'Prairie', 'Prickly', 'Primrose', 'Ptarmigan', 'Puffin', 'Raining', 'Rainy', 'Rapid', 'Raspberry', 'Reedy', 'Rippling', 'Rocky',
        'Rooster', 'Rooting', 'Rosy', 'Round', 'Runny', 'Rushing', 'Rusting', 'Rusty', 'Sap', 'Sapling', 'Salmon', 'Saxifrage', 'Scallop',
        'Scarred', 'Scarring', 'Scorched', 'Scorching', 'Seal', 'Seedling', 'Seedy', 'Senna', 'Shaded', 'Shadowed', 'Shadowy', 'Shady',
        'Shard', 'Sharpened', 'Shimmering', 'Shimmery', 'Shiny', 'Shining', 'Shrimp', 'Shrub', 'Silent', 'Silt', 'Silvery', 'Singing',
        'Skink', 'Skipper', 'Skipping', 'Skua', 'Skunk', 'Sleet', 'Slither', 'Slithering', 'Slope', 'Slug', 'Smoky', 'Snap',
        'Snapped', 'Snapping', 'Snapper', 'Snappy', 'Snarl', 'Snarling', 'Sneezing', 'Sneezy', 'Snipped', 'Snipping',
        'Snowed', 'Snowing', 'Snowy', 'Sooty', 'Sparking', 'Speckled', 'Splashed', 'Splashing', 'Spurge', 'Sporange',
        'Springing', 'Sprout', 'Spruce', 'Sprung', 'Squashberry', 'Stony', 'Storming', 'Stormy', 'Stream', 'Streaming',
        'Stricken', 'Striking', 'Striped', 'Strong', 'Stump', 'Stumpy', 'Summit', 'Sunning', 'Sunny', 'Swampy', 'Swiping',
        'Swirl', 'Swirling', 'Swooping', 'Tamarack', 'Tea', 'Tear', 'Tearing', 'Tern', 'Thorn', 'Thorny', 'Thundering',
        'Thunderous', 'Toad', 'Torrent', 'Traipse', 'Traipsed', 'Traipsing', 'Travel', 'Traveling', 'Tuft', 'Tufted', 'Tumbling',
        'Tunnel', 'Tussock', 'Twinflower', 'Umbra', 'Vervain', 'Veronica', 'Vulture', 'Walrus', 'Wander', 'Wandering',
        'Warren', 'Webbed', 'Webbing', 'Weedy', 'Wheat', 'Whelk', 'Whirling', 'Whisper', 'Whispering', 'Whistle', 'Wing',
        'Wish', 'Wishing', 'Wither', 'Withered', 'Withering', 'Wonder', 'Wondering', 'Wood', 'Wooded', 'Woody', 'Wort', 'Wound',
        'Wounded', 'Wounding', 'Wren', 'Yonder', 'Zinnia'
    ]

    colour_prefixes = {
        'WHITE': [
            'White', 'White', 'Pale', 'Snow', 'Cloud', 'Cloudy', 'Milk', 'Hail', 'Frost', 'Frozen', 'Freeze', 'Ice', 'Icy', 'Sheep',
            'Blizzard', 'Flurry', 'Moon', 'Star', 'Light', 'Bone', 'Bright', 'Swan', 'Dove', 'Wooly', 'Cotton', 'Warm', 'Arctic'
        ],
        'WHITE2': [
            'White', 'White', 'Pale', 'Snow', 'Cloud', 'Cloudy', 'Milk', 'Hail', 'Frost', 'Frozen', 'Freeze', 'Ice', 'Icy', 'Sheep',
            'Blizzard', 'Flurry', 'Moon', 'Star', 'Light', 'Bone', 'Bright', 'Swan', 'Dove', 'Wooly', 'Cotton', 'Warm', 'Arctic'
        ],
        'PALEGREY': [
            'Grey', 'Silver', 'Pale', 'Light', 'Cloud', 'Cloudy', 'Hail', 'Frost', 'Ice', 'Icy', 'Mouse', 'Bright', "Fog", 'Freeze',
            'Frozen', 'Stone', 'Pebble', 'Dove', 'Sky', 'Cotton', 'Heather', 'Warm', 'Arctic', 'Ashen'
        ],
        'LIGHTGREY2': [
            'Grey', 'Silver', 'Pale', 'Light', 'Cloud', 'Cloudy', 'Hail', 'Frost', 'Ice', 'Icy', 'Mouse', 'Bright', "Fog", 'Freeze',
            'Frozen', 'Stone', 'Pebble', 'Dove', 'Sky', 'Cotton', 'Heather', 'Warm', 'Arctic', 'Ashen'
        ],
        'SILVER': [
            'Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue',
            'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'
        ],
        'SNOW': [
            'Grey', 'Silver', 'Cinder', 'Ice', 'Frost', 'Rain', 'Blue',
            'River', 'Blizzard', 'Bone', 'Icy', 'Frosted', 'Berry', 'White'
        ],
        'LILAC': [
            'Grey', 'Silver', 'Cinder', 'Ice', 'Frost', 'Rain', 'Blue',
            'River', 'Blizzard', 'Bone', 'Icy', 'Lilac', 'Lavender'
        ],
        'GREY': [
            'Grey', 'Grey', 'Ash', 'Ashen', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse', 'Smoke', 'Smokey', 'Shadow', "Fog", 'Bone', 
            'Bleak', 'Rain', 'Storm', 'Soot', 'Pebble', 'Mist', 'Misty', 'Heather'
        ],
        'GREY2': [
            'Grey', 'Grey', 'Ash', 'Ashen', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse', 'Smoke', 'Smokey', 'Shadow', "Fog", 'Bone', 
            'Bleak', 'Rain', 'Storm', 'Soot', 'Pebble', 'Mist', 'Misty', 'Heather'
        ],
        'BLUE': [
            'Grey', 'Grey', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse',
            'Smoke', 'Shadow', 'Fog', 'Bone', 'Blue', 'Mist', 'Misty', 'Thistle',
            'Iris', 'Hyacinth', 'Hydrangea', 'Periwinkle', 'Bluebell'
        ],
        'LIGHTBG': [
            'Grey', 'Grey', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse',
            'Smoke', 'Shadow', 'Fog', 'Bone', 'Blue', 'Mist', 'Misty', 'Thistle',
            'Iris', 'Hyacinth', 'Hydrangea', 'Periwinkle', 'Bluebell'
        ],
        'BG': [
            'Grey', 'Grey', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse',
            'Smoke', 'Shadow', 'Fog', 'Bone', 'Blue', 'Mist', 'Misty', 'Thistle',
            'Iris', 'Hyacinth', 'Hydrangea', 'Periwinkle', 'Bluebell'
        ],
        'DARKBG': [
            'Grey', 'Grey', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse',
            'Smoke', 'Shadow', 'Fog', 'Bone', 'Blue', 'Mist', 'Misty', 'Thistle',
            'Iris', 'Hyacinth', 'Hydrangea', 'Periwinkle', 'Bluebell'
        ],
        'DARKGREY': [
            'Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night', 'Cinder', 'Ash', 'Ashen',
            'Smoke', 'Smokey', 'Shadow', 'Bleak', 'Rain', 'Storm', 'Pebble', 'Mist', 'Misty'
        ],
        'DARKGREY2': [
            'Grey', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night', 'Cinder', 'Ash', 'Ashen',
            'Smoke', 'Smokey', 'Shadow', 'Bleak', 'Rain', 'Storm', 'Pebble', 'Mist', 'Misty'
        ],
        'BLACK': [
            'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'
        ],
        'GHOST': [
            'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Bleak', 'Storm', 'Violet', 'Pepper', 'Bat'
        ],
        'BLACK2': [
            'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'
        ],
        'BLACK3': [
            'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'
        ],
        'EBONY': [
            'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'
        ],
        'LIGHTGREEN': [
            'Green', 'Pale', 'Mint', 'Fern', 'Holly', 'Clover', 'Lime',
            'Thyme', 'Pale', 'Light', 'Grass', 'Parsley', 'Leaf', 'Tansy',
            'Herb', 'Thyme'
        ],
        'GREEN': [
            'Green', 'Fern', 'Herb', 'Holly', 'Clover', 'Olive', 'Calm',
            'Thyme', 'Chervil', 'Tansy', 'Parsley', 'Grass', 'Leaf',
            'Forest', 'Turtle', 'Lime'
        ],
        'DARKGREEN': [
            'Dark', 'Green', 'Forest', 'Leaf', 'Grass', 'Fern', 'Ivy',
            'Vine', 'Thyme', 'Herb', 'Clover', 'Holly', 'Stem', 'Night',
            'Sage', 'Branch', 'Twig', 'Stem'
        ],
        'LIGHTPURPLE': [
            'Purple', 'Magic', 'Magical', 'Moon', 'Violet', 'Lavender',
            'Lilac', 'Amethyst', 'Jewel', 'Gem', 'Gemstone', 'Petal',
            'Flower', 'Blossom'
        ],
        'PURPLE': [
            'Purple', 'Magic', 'Magical', 'Moon', 'Violet', 'Lavender',
            'Lilac', 'Amethyst', 'Jewel', 'Gem', 'Gemstone', 'Petal',
            'Flower', 'Blossom', 'Night', 'Purple', 'Magic', 'Magical',
            'Moon', 'Violet', 'Lavender', 'Lilac', 'Amethyst', 'Jewel',
            'Gem', 'Gemstone', 'Petal', 'Flower', 'Plum'
        ],
        'DARKPURPLE': [
            'Night', 'Purple', 'Magic', 'Magical', 'Moon', 'Violet',
            'Lavender', 'Lilac', 'Amethyst', 'Jewel', 'Gem', 'Gemstone',
            'Petal', 'Flower', 'Plum'
        ],
        'DARK': [
            'Black', 'Black', 'Shade', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Brown', 'Shade', 'Dark', 'Night'
        ],
        'PALEGINGER': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Cream', 'Sandy', 'Creamy', 'Warm', 'Robin'
        ],
        'PALEGINGER2': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Cream', 'Sandy', 'Creamy', 'Warm', 'Robin'
        ],
        'PALE': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Cream', 'Apricot', 'Sandy', 'Creamy', 'Warm', 'Robin'
        ],
        'CREAM': [
            'Sand', 'Sandy', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn'
        ],
        'CREAM2': [
            'Sand', 'Sandy', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn'
        ],
        'CREAM3': [
            'Sand', 'Sandy', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn'
        ],
        'PALEYELLOW': [
            'Sand', 'Sandy', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn'
        ],
        'YELLOW': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Cream', 'Creamy', 'Sandy', 'Gold',
            'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion'
        ],
        'DARKCREAM': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Cream', 'Creamy', 'Sandy', 'Gold',
            'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion'
        ],
        'GOLDEN': [
            'Gold', 'Golden', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Marigold', 'Warm'
        ],
        'GOLD2': [
            'Gold', 'Golden', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Marigold', 'Warm'
        ],
        'LIGHTGB': [
            'Wren', 'Thrasher', 'Finch', 'Pelican', 'Shrike', 'Gold', 'Golden',
            'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Hazel', 'Muddy'
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Brown', 'Pale', 'Light',
            'Mouse', 'Dust', 'Sand', 'Bright', 'Mud'
        ],
        'GB': [
            'Wren', 'Thrasher', 'Finch', 'Pelican', 'Shrike', 'Gold', 'Golden',
            'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Hazel', 'Muddy'
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Brown', 'Pale', 'Light',
            'Mouse', 'Dust', 'Sand', 'Bright', 'Mud'
        ],
        'DARKGB': [
            'Wren', 'Thrasher', 'Finch', 'Pelican', 'Shrike', 'Gold', 'Golden',
            'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Hazel', 'Muddy'
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Brown', 'Pale', 'Light',
            'Mouse', 'Dust', 'Sand', 'Bright', 'Mud'
        ],
        'GINGER': [
            'Ginger', 'Ginger', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Sunny', 'Light', 'Primrose', 'Rose',
            'Rowan', 'Fox', 'Tawny', "Plum", 'Orange', 'Warm', 'Burn', 'Burnt', 'Robin', 'Amber'
        ],
        'GINGER2': [
            'Ginger', 'Ginger', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Sunny', 'Light', 'Primrose', 'Rose',
            'Rowan', 'Fox', 'Tawny', "Plum", 'Orange', 'Warm', 'Burn', 'Burnt', 'Robin', 'Amber'
        ],
        'APRICOT': [
            'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Light', 'Rose',
            'Rowan', 'Fox', 'Tawny', 'Apricot'
        ],
        'ORANGE': [
            'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Light', 'Rose',
            'Rowan', 'Fox', 'Tawny', 'Pumpkin'
        ],
        'DARKGINGER': [
            'Ginger', 'Ginger', 'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Oak', 'Shade', 'Russet',
            'Rowan', 'Fox', 'Orange', 'Copper', 'Cinnamon', 'Burn', 'Burnt', 'Jasper', 'Robin'
        ],
        'DARKGINGER2': [
            'Ginger', 'Ginger', 'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Oak', 'Shade', 'Russet',
            'Rowan', 'Fox', 'Orange', 'Copper', 'Cinnamon', 'Burn', 'Burnt', 'Jasper', 'Robin'
        ],
        'LIGHTPINK': [
            'Petal', 'Hibiscus', 'Lotus', 'Flamingo', 'Sunset', 'Sunrise'
        ],
        'LIGHTBROWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Dusty', 'Sand', 'Sandy', 'Bright', 'Mud',
            'Hazel', 'Vole', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn', 'Bark'
        ],
        'LIGHTBROWN2': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Dusty', 'Sand', 'Sandy', 'Bright', 'Mud',
            'Hazel', 'Vole', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn', 'Bark'
        ],
        'LIGHTGB2': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Mud',
            'Hazel', 'Muddy'
        ],
        'CARAMEL': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Cream',
            'Hazel', 'Fawn'
        ],
        'FAWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Deer',
            'Hazel', 'Fawn'
        ],
        'BROWN': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty' 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag',
            'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'
        ],
        'BROWN2': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty' 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag',
            'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'
        ],
        'GB2': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer'
        ],
        'DARKGB2': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', 'Deer'
        ],
        'CINNAMON': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Cinnamon',
            'Acorn', 'Mud', 'Deer'
        ],
        'CHOCOLATE': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Cocoa',
            'Acorn', 'Mud', 'Deer'
        ],
        'DARKBROWN2': [
            'Brown', 'Dark', 'Shade', 'Night', 'Russet', 'Rowan', 'Mud', 'Oak', 'Stag', 'Elk', 'Twig',
            'Owl', 'Otter', 'Log', 'Hickory', 'Branch', 'Robin', 'Bark'
        ],
        'DARKBROWN': [
            'Brown', 'Dark', 'Shade', 'Night', 'Russet', 'Rowan', 'Mud', 'Oak', 'Stag', 'Elk', 'Twig',
            'Owl', 'Otter', 'Log', 'Hickory', 'Branch', 'Robin', 'Bark'
        ],
        'WHITE3': [
            'White', 'White', 'Pale', 'Snow', 'Cloud', 'Cloudy', 'Milk', 'Hail', 'Frost', 'Frozen', 'Freeze', 'Ice', 'Icy', 'Sheep',
            'Blizzard', 'Flurry', 'Moon', 'Star', 'Light', 'Bone', 'Bright', 'Swan', 'Dove', 'Wooly', 'Cotton', 'Warm', 'Arctic'
        ],
        'PALEGREY2': [
            'Grey', 'Silver', 'Pale', 'Light', 'Cloud', 'Cloudy', 'Hail', 'Frost', 'Ice', 'Icy', 'Mouse', 'Bright', "Fog", 'Freeze',
            'Frozen', 'Stone', 'Pebble', 'Dove', 'Sky', 'Cotton', 'Heather', 'Warm', 'Arctic', 'Ashen'
        ],
        'LIGHTGREY3': [
            'Grey', 'Silver', 'Pale', 'Light', 'Cloud', 'Cloudy', 'Hail', 'Frost', 'Ice', 'Icy', 'Mouse', 'Bright', "Fog", 'Freeze',
            'Frozen', 'Stone', 'Pebble', 'Dove', 'Sky', 'Cotton', 'Heather', 'Warm', 'Arctic', 'Ashen'
        ],
        'LIGHTSILVER': [
            'Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue',
            'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'
        ],
        'BLUE1': [
            'Hail', 'Sky', 'Pond', 'Stream', 'River', 'Storm'
        ],
        'PALEBLUE': [
            'Hail', 'Sky', 'Pond', 'Stream', 'River', 'Storm'
        ],
        'LIGHTBLUE': [
            'Hail', 'Sky', 'Pond', 'Stream', 'River', 'Storm'
        ],
        'DARKBLUE': [
            'Hail', 'Sky', 'Pond', 'Stream', 'River', 'Storm'
        ],
        'RUSSIAN': [
            'Hail', 'Sky', 'Pond', 'Stream', 'River', 'Storm'
        ],
        'SILVER2': [
            'Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue',
            'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'
        ],
        'DARKSILVER': [
            'Grey', 'Silver', 'Cinder', 'Ice', 'Icy', 'Frost', 'Frozen', 'Freeze', 'Rain', 'Blue',
            'River', 'Blizzard', 'Flurry', 'Bone', 'Bleak', 'Stone', 'Pebble', 'Heather', 'Warm', 'Arctic'
        ],
        'GREY3': [
            'Grey', 'Grey', 'Ash', 'Ashen', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse', 'Smoke', 'Smokey', 'Shadow', "Fog", 'Bone', 
            'Bleak', 'Rain', 'Storm', 'Soot', 'Pebble', 'Mist', 'Misty', 'Heather'
        ],
        'DARKGREY3': [
            'Grey', 'Grey', 'Ash', 'Ashen', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse', 'Smoke', 'Smokey', 'Shadow', "Fog", 'Bone', 
            'Bleak', 'Rain', 'Storm', 'Soot', 'Pebble', 'Mist', 'Misty', 'Heather'
        ],
        'STONE': [
            'Grey', 'Grey', 'Ash', 'Ashen', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse', 'Smoke', 'Smokey', 'Shadow', "Fog", 'Bone', 
            'Bleak', 'Rain', 'Storm', 'Soot', 'Pebble', 'Mist', 'Misty', 'Heather'
        ],
        'COAL': [
            'Grey', 'Shade', 'Raven', 'Crow', 'Coal', 'Dark', 'Night',
            'Smoke', 'Shadow', 'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'
        ],
        'BLACK4': [
            'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'
        ],
        'OBSIDIAN': [
            'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt'
        ],
        'PALEGINGER3': [
            'Pale', 'Ginger', 'Sand', 'Sandy', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Warm', 'Robin'
        ],
        'GOLDEN2': [
            'Gold', 'Golden', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Marigold', 'Warm'
        ],
        'LIGHTGOLD': [
            'Gold', 'Golden', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Marigold', 'Warm'
        ],
        'DARKGOLD': [
            'Gold', 'Golden', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Marigold', 'Warm'
        ],
        'HONEY': [
            'Gold', 'Golden', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion', 'Marigold', 'Warm'
        ],
        'LIGHTGINGER3': [
            'Pale', 'Ginger', 'Sand', 'Sandy', 'Yellow', 'Sun', 'Sunny', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy', 'Warm', 'Robin'
        ],
        'GINGER3': [
            'Ginger', 'Ginger', 'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Sunny', 'Light', 'Primrose', 'Rose',
            'Rowan', 'Fox', 'Tawny', "Plum", 'Orange', 'Warm', 'Burn', 'Burnt', 'Robin', 'Amber'
        ],
        'FIRE': [
            'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Light', 'Rose',
            'Rowan', 'Fox', 'Tawny', "Plum"
        ],
        'DARKGINGER3': [
            'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet',
            'Rowan', 'Fox'
        ],
        'RED': [
            'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet',
            'Rowan', 'Fox'
        ],
        'RUSSET': [
            'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet',
            'Rowan', 'Fox'
        ],
        'AUBURN': [
            'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet',
            'Rowan', 'Fox'
        ],
        'LILAC2': [
            'Flower', 'Petal', 'Lilac', 'Lily', 'Pink', 'Heather', 'Rose', 'Lavender'
        ],
        'DARKLILAC': [
            'Flower', 'Petal', 'Lilac', 'Lily', 'Pink', 'Heather', 'Rose', 'Lavender'
        ],
        'PALELILAC': [
            'Flower', 'Petal', 'Lilac', 'Lily', 'Pink', 'Heather', 'Rose', 'Lavender'
        ],
        'LIGHTLILAC': [
            'Flower', 'Petal', 'Lilac', 'Lily', 'Pink', 'Heather', 'Rose', 'Lavender'
        ],
        'ROSE': [
            'Flower', 'Petal', 'Lilac', 'Lily', 'Pink', 'Heather', 'Rose', 'Lavender'
        ],
        'CREAM4': [
            'Sand', 'Sandy', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn'
        ],
        'PALECREAM': [
            'Egg', 'Milk', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Sand', 'Sandy', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn'
        ],
        'DARKCREAM2': [
            'Sand', 'Sandy', 'Yellow', 'Pale', 'Cream', 'Light', 'Milk', 'Fawn',
            'Bone', 'Daisy', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn'
        ],
        'LIGHTBROWN3': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Dusty', 'Sand', 'Sandy', 'Bright', 'Mud',
            'Hazel', 'Vole', 'Branch', 'Warm', 'Robin', 'Almond', 'Acorn', 'Bark'
        ],
        'FAWN2': [
            'Fawn', 'Stag', 'Doe', 'Buck', 'Hind', 'Tan'
        ],
        'TAN': [
            'Tan', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Sand',
            'Hazel'
        ],
        'BROWN3': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Dust', 'Dusty' 'Acorn', 'Mud', 'Deer', 'Fawn', 'Doe', 'Stag',
            'Twig', 'Owl', 'Otter', 'Log', 'Vole', 'Branch', 'Hazel', 'Robin', 'Acorn', 'Bark'
        ],
        'CHOCOLATE2': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', "Deer"
        ],
        'DARKBROWN3': [
            'Brown', 'Dark', 'Shade', 'Night', 'Russet', 'Rowan', 'Mud', 'Oak', 'Stag', 'Elk', 'Twig',
            'Owl', 'Otter', 'Log', 'Hickory', 'Branch', 'Robin', 'Bark'
        ],
        'EBONY1': [
            'Black', 'Black', 'Shade', 'Shaded', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch', 'Midnight', 'Pepper', 'Jet', 'Bat', 'Burnt']}

    eye_prefixes = {
        'YELLOW': ['Yellow', 'Moon', 'Daisy', 'Honey', 'Light'],
        'AMBER': ['Amber', 'Sun', 'Fire', 'Gold', 'Honey', 'Scorch'],
        'HAZEL': ['Tawny', 'Hazel', 'Gold', 'Daisy', 'Sand'],
        'PALEGREEN': ['Green', 'Pale', 'Mint', 'Fern', 'Weed'],
        'GREEN': ['Green', 'Fern', 'Weed', 'Holly', 'Clover', 'Olive'],
        'BLUE': ['Blue', 'Blue', 'Ice', 'Sky', 'Lake', 'Frost', 'Water'],
        'DARKBLUE': ['Blue', 'Sky', 'Lake', 'Berry', 'Dark', 'Water', 'Deep'],
        'BLUEYELLOW': ['Yellow', 'Blue', 'Odd', 'One', 'Moon'],
        'BLUEGREEN': ['Green', 'Blue', 'Odd', 'One', 'Clover'],
        'GREY': ['Grey', 'Stone', 'Silver', 'Ripple', 'Moon', 'Rain', 'Storm', 'Heather'],
        'CYAN': ['Sky', 'Blue', 'River', 'Rapid', 'Green', 'Sea'],
        'EMERALD': ['Emerald', 'Green', 'Shine', 'Blue', 'Pine', 'Weed'],
        'PALEBLUE': ['Pale', 'Blue', 'Sky', 'River', 'Ripple', 'Day', 'Cloud', 'Sea'],
        'PALEYELLOW': ['Pale', 'Yellow', 'Sun', 'Gold', 'Ray'],
        'GOLD': ['Gold', 'Golden', 'Sun', 'Amber', 'Sap', 'Honey'],
        'HEATHERBLUE': ['Heather', 'Blue', 'Lilac', 'Rosemary', 'Lavender', 'Wisteria'],
        'COPPER': ['Copper', 'Red', 'Amber', 'Brown', 'Fire', 'Cinnamon', 'Jasper'],
        'SAGE': ['Sage', 'Leaf', 'Olive', 'Bush', 'Clove', 'Green', 'Weed'],
        'BLUE2': ['Blue', 'Blue', 'Ice', 'Icy', 'Sky', 'Lake', 'Frost', 'Water'],
        'SUNLITICE': ['Sun', 'Ice', 'Icy', 'Frost', 'Sunrise', 'Dawn', 'Dusk', 'Odd', 'Glow'],
        'GREENYELLOW': ['Green', 'Yellow', 'Tawny', 'Hazel', 'Gold', 'Daisy', 'Sand', 'Sandy', 'Weed'],
        'PINK': ['Petal', 'Flower', 'Rose', 'Pale', 'Soft', 'Primrose', 'Bloom', 'Strawberry', 'Blossom', 'Hibiscus', 'Berry', 'Pink', 'Sweet', 'Serene', 'Flower'],
        'SCARLET': ['Red', 'Crimson', 'Fire', 'Amber', 'Scorch', 'Flame', 'Flaming', 'Rose', 'Ember', 'Burnt', 'Burning', 'Scarlet', 'Bright', 'Hidden', 'Cardinal', 'Light'],
        'VIOLET': ['Night', 'Purple', 'Magic', 'Magical', 'Moon', 'Violet', 'Lavender', 'Lilac', 'Amethyst', 'Jewel', 'Gem', 'Gemstone', 'Petal', 'Flower', 'Plum'],
        'PALEYELLOW2': ['Yellow', 'Moon', 'Daisy', 'Honey', 'Light', 'Sun', 'Dandelion', 'Marigold', 'Bee', 'Bumble', 'Sunflower', 'Dandelion', 'Wasp', 'Hive', 'Pale'],
        'RED': ['Red', 'Crimson', 'Fire', 'Blood', 'Scorch', 'Flame', 'Flaming', 'Rose', 'Ember', 'Burnt', 'Burning', 'Poppy', 'Petal', 'Hidden', 'Cardinal', 'Robin'],
        'AQUA': ['Ocean', 'Sea', 'Turtle', 'Blue', 'Splash', 'River', 'Water', 'Stream', 'Aqua', 'River', 'Stream', 'Puddle', 'Turquoise', 'Green', 'Lake', 'Pond'],
        'PALEVIOLET': ['Purple', 'Magic', 'Magical', 'Moon', 'Violet', 'Lavender', 'Lilac', 'Amethyst', 'Jewel', 'Gem', 'Gemstone', 'Petal', 'Flower', 'Blossom'],
        'SAGEGREEN': ['Green', 'Fern', 'Herb', 'Holly', 'Clover', 'Olive', 'Calm', 'Thyme', 'Chervil', 'Tansy', 'Parsley', 'Grass', 'Leaf', 'Forest', 'Sage', 'Serene'],
        'PALEBLUE2': ['Blue', 'Sky', 'Moon', 'Borage', 'Splash', 'Pale', 'Serene', 'Cloud', 'Sapphire', 'Stream', 'River', 'Jay', 'Feather', 'Splash', 'Pale', 'Light'],
        'BROWN': ['Oak', 'Brown', 'Tree', 'Bark', 'Alder', 'Branch', 'Twig', 'Stem', 'Mud', 'Mouse', 'Dust', 'Acorn', 'Timber', 'Log', 'Brown', 'Dusky', 'Dusk', 'Dust'],
        'SPRINGGREEN': ['Green', 'Fern', 'Herb', 'Holly', 'Clover', 'Olive', 'Calm', 'Thyme', 'Chervil', 'Tansy', 'Parsely', 'Bright', 'Spring', 'Light', 'Stem', 'Leaf'],
        'GOLDEN': ['Bright', 'Gold', 'Golden', 'Amber', 'Yellow', 'Orange', 'Sun', 'Sunny', 'Shine', 'Shining', 'Moon', 'Light', 'Bright', 'Honey', 'Spring', 'Shiny'],
        'HONEY': ['Yellow', 'Moon', 'Daisy', 'Honey', 'Light', 'Bright', 'Sun', 'Sunny', 'Shine', 'Shining', 'Gold', 'Golden', 'Spring', 'Shiny', 'Hive', 'Bee', 'Bumble'],
        'COPPER2': ['Copper', 'Brown', 'Orange', 'Redwood', 'Bright', 'Scorch', 'Flame', 'Fire', 'Adder', 'Fox', 'Rust', 'Rusty', 'Oak', 'Brown', 'Ember', 'Shiny', 'Hare'],
        'MAGENTA': ['Petal', 'Flower', 'Bloom', 'Blossom', 'Hibiscus', 'Violet', 'Lavender', 'Lilac', 'Amethyst', 'Jewel', 'Gem', 'Gemstone', 'Magenta', 'Flower', 'Petal'],
        'MINT': ['Mint', 'Minty', 'Cold', 'Blue', 'Splash', 'River', 'Water', 'Stream', 'Breeze', 'River', 'Stream', 'Puddle', 'Serene', 'Mist', 'Misty', 'Pale', 'Sky'],
        'EMERALD2': ['Green', 'Fern', 'Herb', 'Holly', 'Clover', 'Olive', 'Calm', 'Thyme', 'Chervil', 'Tansy', 'Parsely', 'Bright', 'Spring', 'Emerald', 'Jewel', 'Jade'],
        'PUMPKIN': ['Amber', 'Sun', 'Fire', 'Gold', 'Honey', 'Scorch', 'Ember', 'Flame', 'Flaming', 'Orange', 'Butterfly', 'Monarch', 'Pumpkin', 'Carrot', 'Rust', 'Rusty'],
        'ROSEGOLD': ['Rose', 'Pink', 'Coral', 'Gold', 'Golden', 'Bright', 'Shining', 'Sun', 'Light', 'Petal', 'Blooming', 'Flower', 'Spring', 'Shiny', 'Strawberry', 'Berry'],
        'GREENGOLD': ['Gold', 'Golden', 'Sun', 'Sunny', 'Spring', 'Green', 'Bright', 'Dandelion', 'Marigold', 'Herb', 'Clover', 'Emerald', 'Jade', 'Honey', 'Leaf', 'Sapling'],
        'PINKBLUE': ['Petal', 'Flower', 'Rose', 'Pale', 'Soft', 'Strawberry', 'Blossom', 'Pink', 'Flower', 'Stream', 'Sky', 'Blue', 'Sweet', 'Serene', 'Splash', 'Sapphire'],
        'DANDELION': ['Dandelion', 'Yellow', 'Sun', 'Sunny', 'Hazel', 'Tawny', 'Green', 'Spring', 'Bright', 'Clover', 'Marigold', 'Shining', 'Emerald', 'Honey', 'Leaf', 'Light'],
        'INDIGO': ['Ocean', 'Violet', 'Blue', 'Deep', 'Whale', 'Water', 'Dark', 'River', 'Lake', 'Splash', 'Hidden', 'Jewel', 'Sapphire', 'Lapis', 'Moon', 'Night', 'Ebony', 'Raven'],
        'AMARANTH': ['Hibiscus', 'Amaranth', 'Red', 'Pink', 'Bright', 'Light', 'Blossom', 'Strawberry', 'Cherry', 'Apple', 'Rose', 'Crimson', 'Ember', 'Fox', 'Flame', 'Flaming'],
        'CORAL': ['Coral', 'Pink', 'Bright', 'Light', 'Pale', 'Soft', 'Sweet', 'Petal', 'Blossom', 'Strawberry', 'Blooming', 'Primrose', 'Berry', 'Cloud', 'Flower', 'Serene'],
        'DARKGREEN': ['Dark', 'Green', 'Forest', 'Leaf', 'Grass', 'Fern', 'Ivy', 'Vine', 'Thyme', 'Herb', 'Clover', 'Holly', 'Stem', 'Night', 'Sage', 'Branch', 'Twig', 'Stem'],
        'DARKAMBER': ['Amber', 'Copper', 'Fire', 'Bear', 'Hidden', 'Scorch', 'Ember', 'Flame', 'Flaming', 'Dark', 'Butterfly', 'Monarch', 'Pumpkin', 'Brown', 'Rust', 'Rusty']
    }

    loner_names = [
        "Abyss", "Ace", "Ah" ,"Alcina", "Alec", "Alice", "Amber", "Amity", "Amy", "Angel", "Anita", "Anubis", "Armin", "April", "Ash", 
        "Aurora", "Azula", "Aries", "Aquarius", "Bagel", "Bailey", "Bandit", "Baphomet", "Bastet", "Bean", "Beanie Baby", "Beans", "Bede",
        "Belle", "Benny", "Bently", "Bentley", "Beverly", "Big Man", "Birb", "Blu",  "Bluebell", "Bologna", "Bolt", "Bonbon", "Bongo", "Bonnie",
        "Bonny", "Boo", "Broccoli", "Buddy", "Bumblebee", "Bunny", "Burger", "Burm", "Bub", "Cake", "Callie", "Calvin", "Caramel", "Carmen", 
        "Carmin", "Carolina", "Caroline", "Carrie", "Catie", "Catty", "Chance", "Chanel", "Chansey", "Chaos", "Charles", "Charlie", "Charlotte",
        "Charm", "Chase", "Cheese", "Cheesecake", "Cheeto", "Cheetoman", "Chef", "Cherry", "Chester", "Chewie", "Chewy", "Chicco", "Chief", "Chinook",
        "Chip", "Chloe", "Chocolate", "Chocolate Chip", "Chris", "Chrissy", "Cinder", "Cinderblock", "Cloe", "Cloud", "Cocoa", "Cocoa Puff", "Coffee",
        "Conan", "Cookie", "Coral", "Cosmo", "Cowbell", "Cowboy", "Crab", "Cracker", "Cream", "Crispy", "Crow", "Crunchwrap", "Crunchy", "Cupcake", "Cooper",
        "Cancer", "Capricorn", "Dakota", "Dan", "Dave", "Deli", "Delilah", "Della", "Dewey", "Dirk", "Dolly", "Donald", "Dragonfly", "Dreamy", "Duchess", "Dune",
        "Dunnock" "Eclipse", "Daisy Mae",  "Eda", "Eddie", "Eevee", "Egg", "Ember", "Emerald", "Emi", "Emma", "Emy", "Erica", "Espresso", "Eve", "Evelyn", "Evie",
        "Evilface", "Erebus", "Fallow", "Fang", "Fawn", "Feather", "Felix", "Fern", "Ferret", "Ferry", "Finch", "Firefly", "Fishleg", "Fishtail", "Fiver", "Flabby",
        "Flower", "Fluffy", "Flutie", "Fork", "Frank", "Frankie", "Frannie", "Fred", "Freddy", "Free", "French", "French Fry", "Frito", "Fry", "Frye", "Gamble", 
        "Gargoyle", "Garnet", "Geode", "George", "Ghost", "Gibby", "Gir", "Gizmo", "Glass", "Glory", "Goose", "Grace", "Grain", "Grasshopper", "Gravy", "Guinness",
        "Gust", "Gwendoline", "Gwynn", "Gemini", "Habanero", "Haku", "Harvey", "Havoc", "Herc", "Hercules", "Hiccup", "Holly", "Hop", "Hot Sauce", "Hotdog",
        "Hughie", "Human", "Hunter", "Harlequin", "Ice", "Icecube", "Ice Cube", "Icee", "Igor", "Ike", "Indi", "Insect", "Isabel", "Jack", "Jade", "Jaiden",
        "Jake", "James", "Jasper", "Jaxon", "Jay", "Jenny", "Jesse", "Jessica", "Jester", "Jethro", "Jewel","Jewels", "Jimmy", "Jinx", "John", "Johnny",
        "Joker", "Jolly", "Jolly Rancher", "Joob", "Jubie", "Judas", "Jude", "Judy", "Juliet", "June", "Jupiter", "KD", "Kate", "Katy", "Kelloggs", "Ken",
        "Kendra", "Kenny", "Kermit", "Kerry", "Ketchup", "King", "Kingston", "Kip", "Kisha", "Kitty", "Kitty Cat", "Klondike", "Knox", "Kodiak", "Kong", "L", "Lacy",
        "Lakota", "Laku", "Lee", "Leo", "Leon", "Lester", "Lex", "Lilith", "Lily", "Lily", "Loaf", "Lobster", "Lola", "Loona", "Lora", "Louie", "Louis", "Lucky",
        "Lucy", "Lugnut", "Luigi", "Luna", "Lupo", "Loyalty", "Libra", "Madi", "Makwa", "Maleficent", "Manda", "Mange", "Mango", "Marceline", "Matcha", 
        "Maverick", "Max", "May", "McChicken", "McFlurry", "Meatlug", "Melody", "Meow-Meow", "Meowyman", "Mera", "Mew", "Miles", "Millie", "Milo",
        "Milque", "Mimi", "Minette", "Mini", "Minna", "Minnie", "Mint", "Minty", "Missile Launcher", "Mitski", "Mittens", "Mocha", "Mocha", "Mojo", "Mollie",
        "Molly", "Molly Murder Mittens", "Monika", "Monster", "Monte", "Monzi", "Moon", "Mop", "Moxie", "Mr. Kitty", "Mr. Kitty Whiskers", "Mr. Whiskers",
        "Mr. Wigglebottom", "Mucha", "Murder", "Mushroom", "Mitaine", "Myko", "Neel", "Nagi", "Nakeena", "Neil", "Nemo", "Nessie", "Nick", "Nightmare", "Nikki",
        "Niles", "Ninja", "Nintendo", "Nisha", "Nitro", "Noodle", "Norman" "Nova", "Nugget", "Nuggets", "Nuka", "Nutella", "O'Leary", "Oakley", "Oapie", "Obi Wan",
        "Old Man Sam", "Oleander", "Olga", "Oliver", "Oliva", "Ollie", "Omelet", "Onyx", "Oops", "Ophelia", "Oreo", "Orion", "Oscar", "Owen", "Peach", "Peanut",
        "Peanut Wigglebottom",  "Peanut Wigglebutt", "Pear", "Pearl", "Pecan", "Penny", "Peony", "Pepper", "Pichi", "Pickles", "Pikachu", "Ping", "Ping Pong",
        "Pip", "Piper", "Pipsqueak", "Pocket", "Poki", "Polly", "Pong", "Porsche", "Potato", "Prickle", "Princess", "Pumpernickel", "Punk", "Purdy",
        "Purry", "Pisces", "Pushee", "Quagmire", "Quake", "Queen", "Queenie", "Queeny", "Queso", "Queso Ruby", "Quest", "Quickie", "Quimby",
        "Quinn", "Quino", "Quinzee", "Quesadilla", "Ramble", "Randy", "Rarity", "Rat", "Ray", "Reese", "Reeses Puff", "Ren", "Rio", "Riot", "River",
        "Riya", "Rocket", "Rolo", "Roman", "Roomba", "Rooster", "Rory", "Rose", "Roselie", "Ruby", "Rudolph", "Rue", "Ruffnut", "Rum", "Sadie", "Saki",
        "Salmon", "Salt", "Sam", "Samantha", "Sandwich", "Sandy", "Sausage", "Schmidt", "Scotch", "Scrooge", "Seamus", "Sekhmet", "Seri", "Shampoo", "Shay",
        "Shimmer", "Shiver", "Silva", "Silver", "Skrunkly", "Sloane", "Slug", "Slushie", "Smoothie", "Smores", "Sneakers", "Snek", "Snotlout", "Socks", 
        "Sofa", "Sol", "Sonic", "Sophie", "Sorbet", "Sox", "Spam", "Sparky", "Spots", "Stan", "Star", "Starfish", "Stella", "Steve", "Steven", "Stinky",
        "Stolas", "Stripes", "Sundae", "Sunny", "Sunset", "Sweet", "Sweetie", "Scorpio", "Sagittarius", "Tabatha", "Tabby", "Tabbytha", "Taco", "Taco Bell",
        "Tasha", "Tempest", "Tetris", "Teufel", "Tiny", "Toast", "Toffee", "Tom", "Tomato", "Tomato Soup", "Toni", "Toothless", "Torque", "Tortilla", 
        "Treasure", "Triscuit", "Trixie", "Trouble", "Tucker", "Tuffnut", "Tumble", "Turbo", "Twilight", "Twister", "Twix", "Toastee", "Taurus", "Ula", "Union",
        "Uriel", "Vanilla", "Vaxx", "Venture", "Via", "Vida", "Viktor", "Vinnie", "Vinyl", "Violet", "Vivienne", "Void", "Voltage", "Vox", "Virgo", "Wanda", "Webby",
        "Wendy", "Whiskers", "Whisper", "Wigglebottom", "Wigglebutt", "Windy", "Wishbone", "Wisp", "Wisteria", "Worm", "X'ek", "Zelda", "Zim", "Zoe", "Fetber", "Snip-Snap",
        "Callisto", "Era", "Noro", "Ryos", "Magi", "Lover", "Chrome", "Ryos", "Scribble", "Haunted"
    ]

    if os.path.exists('saves/prefixlist.txt'):
        with open('saves/prefixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_prefixes.append(new_name)

    if os.path.exists('saves/suffixlist.txt'):
        with open('saves/suffixlist.txt', 'r') as read_file:
            name_list = read_file.read()
            if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_suffixes.append(new_name)

    def __init__(self,
                 status="warrior",
                 prefix=None,
                 suffix=None,
                 colour=None,
                 eyes=None,
                 pelt=None,
                 tortiepattern=None):
        self.status = status
        self.prefix = prefix
        self.suffix = suffix
        
        # Set prefix
        if prefix is None:
            named_after_appearance = not random.getrandbits(3)  # Chance for True is '1/8'.
            # Add possible prefix categories to list.
            possible_prefix_categories = []
            if eyes in self.eye_prefixes:
                possible_prefix_categories.append(self.eye_prefixes[eyes])
            if colour in self.colour_prefixes:
                possible_prefix_categories.append(self.colour_prefixes[colour])
            # Choose appearance-based prefix if possible and named_after_appearance because True.
            if named_after_appearance and possible_prefix_categories:
                prefix_category = random.choice(possible_prefix_categories)
                self.prefix = random.choice(prefix_category)
            else:
                self.prefix = random.choice(self.normal_prefixes)
                    
        # Set suffix
        while self.suffix is None or self.suffix == self.prefix.casefold():
            if pelt is None or pelt == 'SingleColour':
                self.suffix = random.choice(self.normal_suffixes)
            else:
                named_after_pelt = not random.getrandbits(3) # Chance for True is '1/8'.
                # Pelt name only gets used if there's an associated suffix.
                if (named_after_pelt
                    and pelt in ["Tortie", "Calico"]
                    and tortiepattern in self.tortie_pelt_suffixes):
                    self.suffix = random.choice(self.tortie_pelt_suffixes[tortiepattern])
                elif named_after_pelt and pelt in self.pelt_suffixes:
                    self.suffix = random.choice(self.pelt_suffixes[pelt])
                else:
                    self.suffix = random.choice(self.normal_suffixes)

    def __repr__(self):
        if self.status in ["deputy", "warrior", "medicine cat", "elder"]:
            return self.prefix + self.suffix
        else:
            return self.prefix + self.special_suffixes[self.status]


names = Name()

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
        'pelt', "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt",
        "tail", "tail", "tail", "tail", "tail", "tail", "tail", "tail", "claw", "claw", "claw", "claw", "claw", "claw", "claw",
        "foot","foot", "foot","foot", "foot", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker",
        "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", 'heart',

        # regular suffixes
        "back", "berry", "bite", "blaze", "blossom", "bloom", "branch", "breeze", "briar",
        "bush", "call", "cloud", "creek", "cry", "dapple", "daisy",
        "dawn", "dusk", "dust", "face", "fall", "fang", "feather", "fern", "fire", "flame", "flight", "flower",
        "frost", "gaze", "hawk", "haze", "heather", "holly", "jump", "leaf", "leap", "light", "lily", "mask", 
        "mist", "moon", "needle", "night", "nose", "oak", "path", "petal", "pond", "pool", "poppy",
        "pounce", "puddle", "ripple", "shade", "shadow", "shine", "sight", "sky", "song", "splash",
        "spring", "stalk", "step", "stone", "storm", "streak", "stream", "strike", 
        "swoop", "tail", "throat", "tuft", "thorn", "watcher", "willow", "wind", "wing"]


    pelt_suffixes = {
        'TwoColour': ['patch', 'spot', 'splash', 'patch', 'spots'],
        'Tabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Spotted': ['dapple', 'speckle', 'spots'],
        'Tortie': ['dapple', 'speckle',  'dapple'],
        'Calico': ['stripe', 'dapple', 'patch', 'patch'],
        'Smoke': ['dusk', 'dawn', 'smoke'],
        'Ticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'Patternless': ['spots', 'pelt', 'speckle', 'freckle'],
        'Speckled': ['speckle', 'pelt', 'freckle'],
        'Classic': ['stripe', 'feather', 'fern', 'shade'],
        'Broken': ['stripe', 'spots', 'fern', 'feather']
    }

    tortie_pelt_suffixes = {
        'tortiesolid': ['dapple', 'speckle', 'spots', 'splash'],
        'tortietabby': ['stripe', 'feather', 'stripe', 'shade', 'fern'],
        'tortiepatternless': ['pelt', 'shade'],
        'tortieticked': ['spots', 'pelt', 'speckle', 'freckle'],
        'tortiesmoke': ['dusk', 'dawn', 'smoke'],
        'tortiespotted': ['dapple', 'speckle', 'spots', 'dapple', 'fern', 'freckle'],
        'tortiespeckled': ['dapple', 'speckle', 'spots', 'pelt', 'fern', 'freckle'],
        'tortieclassic': ['dapple', 'stripe', 'spots', 'dapple', 'fern', 'feather'],
        'tortiebroken': ['stripe', 'feather', 'spots', 'shade', 'fern', 'dapple']
    }

    normal_prefixes = [
        'Bayou', 'Birch', 'Blossom', 'Bluff', 'Bog', 'Boulder', 
        'Branch', 'Breeze', 'Breeze', 'Briar', 
        'Bristle', 'Brook', 'Brush', 'Burn', 'Bush',
        'Cedar', 'Cedar', 'Chestnut', 'Clay', 'Cliff', 'Cloud',
        'Conifer', 'Crag', 'Creek', 'Cress', 'Cypress', 'Drift', 'Drizzle', 
        'Drought', 'Dry', 'Dune', 'Elm', 'Ember', 'Feather', 
        'Fern', 'Fir', 'Flint', 'Forest', 'Gorge', 'Gorse', 'Grass', 'Heath', 
        'Heather', 'Hickory', 'Hill', 'Marsh', 'Meadow', 'Mist',
        'Moor', 'Peak', 'Pine', 'Small', 'Little', 'Tiny', 'Curly', 'Creek', 
        'Feather', 'Fern', 'Lake', 'Ice', 'Light', 'Moth', 'Hail', 'Birch',
        'Pine', 'Oak', 'Aspen', 'Mountain', 'Peak', 'Sand', 'Wood', 'Mist', 
        'Fog', 'Leaf', 'Thorn', 'Bramble', 'River', 'Swamp', 'Marsh', 'Fen', 
        'Moor', 'Meadow', 'Fall', 'Stone', 'Plain', 'Prairie'
    ]

    colour_prefixes = {
        'WHITE': [
            'White', 'White', 'Pale', 'Snow', 'Cloud', 'Hail', 'Frost', 'Ice', 'Bright', 'Crane',
            'Sheep', 'Blizzard', 'Moon', 'Light', 'Egret', 'Campion', 'Yarrow', 'Fringe', 'Bergamot', 'Cress', 
            'Magnolia', 'Catalpa', 'Phlox', 'Cottonwood', 'Clover', 'Kite', 'Lily', 'Aster', 'Mimosa', 'Cornus', 
            'Lightning', 'Opossum', 'Moth', 'Mallow', 'Mist', 'Parsley', 'Patch', 'Pear', 'Geranium', 'Plum',
            'Pebble', 'Shell', 'Sorrel', 'Sage', 'Swan', 'Sweet', 'Penstemon', 'Goldenseal', 'Germander',
            'Ibis', 'Laurel', 'Blackhaw', 'Aralia', 'Mistle', 'Comfrey', 'Boneset', 'Tephrosia', 'Hydrangea', 
            'Clematis', 'Chamomile', 'Milkweed', 'Vervain', 'Nettle', 'Azalea', 'Trillium'
        ],
        'PALEGREY': [
            'Grey', 'Birch', 'Aspen', 'Silver', 'Pale', 'Cloud', 'Hail', 'Frost', 'Ice', 'Mouse', 
            'Dew', 'Bright', 'Fog', 'Catalpa', 'Opossum', 'Quiet', 'Small', 'Pebble', 'Stone', 
            'Rock', 'Shell', 'Kite', 'Fringe', 'Lightning', 'Moth', 'Mist', 'Patch', 'Azalea', 'Trillium',
            'Sky', 'Willow', 'Comfrey', 'Boneset', 'Tephrosia', 'Hydrangea', 'Clematis', 'Chamomile', 
            'Milkweed', 'Vervain', 'Nettle'
        ],
        'SILVER': [
            'Grey', 'Birch', 'Aspen', 'Silver', 'Cinder', 'Ice', 'Frost', 'Rain', 'Blue', 'River', 'Dew',
            'Blizzard', 'Campion', 'Fringe', 'Fog', 'Boulder', 'Brook', 'Cedar', 'Lightning', 
            'Shell', 'Kite', 'Sky', 'Pebble', 'Minnow', 'Silver', 'Silver', 'Azalea', 'Plum', 'Trillium',
            'Mockingbird', 'Nuthatch', 'Shiner', 'Shad', 'Wigeon', 'Creek', 'Mist', 'Opossum',
            'Flint', 'Pebble', 'Plover', 'Comfrey', 'Boneset', 'Tephrosia', 'Hydrangea', 'Clematis', 
            'Chamomile', 'Milkweed', 'Vervain', 'Nettle'
        ],
        'GREY': [
            'Gray', 'Gray', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Boulder', 
            'Mouse', 'Smoke', 'Shadow', 'Fog', 'Heron', 'Cedar', 'Dove', 'Gadwall', 'Falcon', 
            'Mockingbird', 'Violet', 'Sky', 'Slate', 'River', 'Borage', 'Aster', 'Bluet', 'Comfrey', 
            'Jay', 'Juniper', 'Gravel', 'Lizard', 'Raccoon', 'Mint', 'Rain', 'Rubble', 'Shell',
            'Snail', 'Swamp', 'Sweet', 'Squirrel', 'Storm', 'Thistle', 'Timber', 'Thorn',
            'Bunting', 'Nuthatch', 'Chickadee', 'Kite', 'Shiner', 'Shad', 'Gar', 'Crane',
            'Shrike', 'Dew', 'Pigeon', 'Kestrel', 'Flint'
        ],
        'DARKGREY': [
            'Gray', 'Shade', 'Raven', 'Heron', 'Crow', 'Stone', 'Dark', 'Night', 'Smoke',
            'Shadow', 'Ant', 'Boulder', 'Ash', 'Rock', 'Mouse', 'Cricket', 
            'Slate', 'Falcon', 'Chickadee', 'Nuthatch', 'Mockingbird', 'Grackle',
            'Storm', 'Shrike', 'Jay', 'Holly', 'Moth', 'Pigeon', 'Pine', 'Snake', 'Thorn', 'Prickle',
            'Pebble', 'Swift', 'Walnut', 'Timber', 'Mole', 'Goose', 'Soot', 'Spider'
        ],
        'BLACK': [
            'Black', 'Black', 'Buzzard', 'Shade', 'Crow', 'Raven', 'Ebony', 'Dark', 'Night',
            'Shadow', 'Scorch', 'Walnut', 'Locust', 'Ant', 'Spider', 'Badger', 'Beetle', 'Cricket', 
            'Bear', 'Boar', 'Soot', 'Mole', 'Towhee', 'Grackle', 'Skunk',
            'Mulberry', 'Salamander', 'Patch', 'Snake', 'Swallow', 'Starling', 'Swift', 'Prickle',
            'Woodpecker', 'Bumelia', 'Fly'
        ],
        'PALEGINGER': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright', 'Honey', 'Daisy', 'Apple',
            'Acorn', 'Dove', 'Lantana', 'Senna', 'Shiner', 'Woodpecker', 'Plover', 
            'Dawn', 'Dusk', 'Rabbit', 'Dust', 'Fallow', 'Deer', 'Fern', 'Ginger', 'Plantain', 'Fawn', 
            'Grass', 'Flicker', 'Flint', 'Hawk', 'Lark', 'Quail', 'Pebble', 'Rye', 'Rush', 'Snail',
            'Spider', 'Shell', 'Oat', 'Leaf', 'Meadow', 'Aralia', 'Coyote', 'Apricot'
        ],
        'GOLDEN': [
            'Golden', 'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder', 'Honey', 'Tawny',
            'Lion', 'Dandelion', 'Warbler', 'Persimmon', 'Hazel', 'Mallow', 'Apple', 'Acorn', 
            'Berry', 'Finch', 'Dawn', 'Dusk', 'Grass', 'Rye', 'Rush', 'Reed', 'Agrimony', 'Lotus',
            'Lark', 'Leopard', 'Copper', 'Puma', 'Chipmunk', 'Meadow', 'Melilot', 'Parsnip', 'Mullein', 
            'Bracken', 'Bramble', 'Copper', 'Lantana', 'Senna', 'Marigold', 'Bee', 'Coyote', 'Primrose', 
            'Goldenrod', 'Tansy', 'Thistle', 'Poppy', 'Sorrel', 'Clover', 'Ginger', 'Plantain', 'Apricot'
        ],
        'GINGER': [
            'Red', 'Fire', 'Rust', 'Flame', 'Ember', 'Sun', 'Light', 'Rose', 'Rowan', 'Fox', 
            'Tawny', 'Plum', 'Oriole', 'Cardinal', 'Persimmon', 'Alder', 'Mallow', 'Spice',
            'Sumac', 'Apple', 'Acorn', 'Berry', 'Cedar', 'Bracken', 'Bramble', 'Copper', 
            'Cypress', 'Hawk', 'Mulberry', 'Sassafras', 'Tupelo', 'Lantana', 'Towhee', 
            'Tanager', 'Chipmunk', 'Buckeye', 'Cherry', 'Holly', 'Woodpecker', 'Cinnamon', 
            'Needle', 'Clover', 'Mistle', 'Poppy', 'Marigold', 'Nettle', 'Lily', 'Spindle',
            'Azalea', 'Yew', 'Ivy', 'Robin', 'Spark', 'Squirrel', 'Newt', 'Mayhaw', 'Hawthorn', 
            'Wasp', 'Tiger', 'Creeper', 'Ginger', 'Plantain', 'Apricot'
        ],
        'DARKGINGER': [
            'Red', 'Red', 'Fire', 'Rust', 'Flame', 'Oak', 'Shade', 'Russet', 'Rowan', 'Fox', 
            'Cardinal', 'Alder', 'Berry', 'Beetle', 'Cedar', 'Cypress', "Mulberry", 'Sassafras', 
            'Tupelo', 'Sumac', 'Lantana', 'Buckeye', 'Cherry', 'Holly', 'Woodpecker', 
            'Cinnamon', 'Needle', 'Clover', 'Mistle', 'Poppy', 'Lily', 'Spindle', 'Creeper',
            'Marigold', 'Azalea', 'Yew', 'Ivy', 'Robin', 'Spark', 'Squirrel', 'Newt', 'Tanager', 
            'Mayhaw', 'Hawthorn', 'Wasp', 'Tiger', 'Plum'
        ],
        'CREAM': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright', 'Honey', 'Daisy', 'Apple',
            'Acorn', 'Dove', 'Lantana', 'Senna', 'Shiner', 'Woodpecker', 'Plover', 
            'Dawn', 'Dusk', 'Rabbit', 'Dust', 'Fallow', 'Deer', 'Fern', 'Ginger', 'Plantain', 'Fawn', 
            'Grass', 'Flicker', 'Flint', 'Hawk', 'Lark', 'Quail', 'Pebble', 'Rye', 'Rush', 'Snail',
            'Spider', 'Shell', 'Oat', 'Leaf', 'Meadow', 'Aralia', 'Coyote', 'Apricot'
        ],
        'APRICOT': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright', 'Honey', 'Daisy', 'Apple',
            'Acorn', 'Dove', 'Lantana', 'Senna', 'Shiner', 'Woodpecker', 'Plover', 
            'Dawn', 'Dusk', 'Rabbit', 'Dust', 'Fallow', 'Deer', 'Fern', 'Ginger', 'Plantain', 'Fawn', 
            'Grass', 'Flicker', 'Flint', 'Hawk', 'Lark', 'Quail', 'Pebble', 'Rye', 'Rush', 'Snail',
            'Spider', 'Shell', 'Oat', 'Leaf', 'Meadow', 'Aralia', 'Coyote', 'Apricot'
        ],
        'LIGHTBROWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Mud', 'Hazel', 'Thrasher', 
            'Warbler', 'Ash', 'Spider', 'Cedar', 'Wigeon', 'Mallard', 'Roadrunner', 'Flicker', 
            'Plover', 'Pipit', 'Moss', 'Creeper', 'Shiner', 'Shad', 'Gar', 'Puma', 'Chipmunk', 
            'Acorn', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 'Bramble', 'Briar', 'Cedar',
            'Cone', 'Dove', 'Dust', 'Eagle', 'Elm', 'Duck', 'Fern', 'Flicker', 'Flint', 'Fir', 'Frog', 
            'Goose', 'Grass', 'Gravel', 'Larch', 'Lavender', 'Leaf', 'Lichen', 'Moth', 'Coyote', 
            'Lizard', 'Hawk', 'Mole', 'Mouse', 'Oat', 'Oak', 'Plantain', 'Hemlock', 'Poplar', 
            'Owl', 'Prickle', 'Pear', 'Pebble', 'Quail', 'Rabbit', 'Rat', 'Robin', 'Rush', 'Snail', 
            'Sparrow', 'Wren', 'Deer', 'Squirrel', 'Trout', 'Timber', 'Thorn', 'Twig', 'Pecan', 
            'Skink', 'Heather'
        ],
        'BROWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Mud', 'Hazel', 'Thrasher', 
            'Warbler', 'Ash', 'Spider', 'Cedar', 'Wigeon', 'Mallard', 'Roadrunner', 'Flicker', 
            'Plover', 'Pipit', 'Moss', 'Creeper', 'Shiner', 'Shad', 'Gar', 'Puma', 'Chipmunk', 
            'Acorn', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 'Bramble', 'Briar', 'Cedar',
            'Cone', 'Dove', 'Dust', 'Eagle', 'Elm', 'Duck', 'Fern', 'Flicker', 'Flint', 'Fir', 'Frog', 
            'Goose', 'Grass', 'Gravel', 'Larch', 'Lavender', 'Leaf', 'Lichen', 'Moth', 'Coyote', 
            'Lizard', 'Hawk', 'Mole', 'Mouse', 'Oat', 'Oak', 'Plantain', 'Hemlock', 'Poplar', 
            'Owl', 'Prickle', 'Pear', 'Pebble', 'Quail', 'Rabbit', 'Rat', 'Robin', 'Rush', 'Snail', 
            'Sparrow', 'Wren', 'Deer', 'Squirrel', 'Trout', 'Timber', 'Thorn', 'Twig', 'Pecan', 
            'Skink', 'Heather'
        ],
        'DARKBROWN': [
            'Buzzard', 'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Acorn', 'Mud', 'Deer', 
            'Hickory', 'Sycamore', 'Pecan', 'Walnut', 'Spider', 'Beetle', 'Cedar', 'Bramble', 
            'Chestnut', 'Hawk', 'Roadrunner', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 
            'Bramble', 'Briar', 'Cedar', 'Cone', 'Lizard', 'Hawk', 'Plantain', 'Hemlock', 'Torreya', 
            'Mole', 'Eagle', 'Elm', 'Duck', 'Fir', 'Frog', 'Goose', 'Larch', 'Leaf', 'Oak', 'Owl', 
            'Rabbit', 'Rat', 'Sparrow', 'Wren', 'Trout', 'Timber', 'Thorn', 'Twig', 'Skink', 'Poplar', 
            'Whippoorwill', 'Creeper', 'Pelican', 'Ant', 'Shad', 'Gar', 'Mink', 'Puma', 'Beaver', 
            'Gopher', 'Chipmunk', 'Coypu', 'Chinquapin', 'Bittern', 'Swamp', 'Pine', 'Prickle', 
            'Snake', 'Snail', 'Swallow', 'Sparrow', 'Turtle'
        ],
        'DARKCHOC': [
            'Buzzard', 'Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud', 'Thrasher', 
            'Pecan', 'Hickory', 'Walnut', 'Ant', 'Spider', 'Beetle', 'Bramble', 'Briar', 'Cedar', 
            'Cone', 'Lizard', 'Hawk', 'Mole', 'Eagle', 'Elm', 'Bark', 'Hemlock', 'Torreya', 'Poplar', 
            'Duck', 'Fir', 'Frog', 'Goose', 'Larch', 'Leaf', 'Oak', 'Owl', 'Rat', 'Sparrow', 'Wren', 
            'Trout', 'Timber', 'Thorn', 'Twig', 'Skink', 'Whippoorwill', 'Creeper', 'Pelican', 
            'Mink', 'Beaver', 'Coypu', 'Alligator', 'Chinquapin', 'Bittern', 'Swamp', 'Pine', 
            'Prickle', 'Snake', 'Snail', 'Swallow', 'Sparrow', 'Turtle', 'Sycamore', 'Yew'
        ],
        'TAUPE': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Mud', 'Hazel', 'Thrasher', 
            'Warbler', 'Ash', 'Spider', 'Cedar', 'Wigeon', 'Mallard', 'Roadrunner', 'Flicker', 
            'Plover', 'Pipit', 'Moss', 'Creeper', 'Shiner', 'Shad', 'Gar', 'Puma', 'Chipmunk', 
            'Acorn', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 'Bramble', 'Briar', 'Cedar',
            'Cone', 'Dove', 'Dust', 'Eagle', 'Elm', 'Duck', 'Fern', 'Flicker', 'Flint', 'Fir', 'Frog', 
            'Goose', 'Grass', 'Gravel', 'Larch', 'Lavender', 'Leaf', 'Lichen', 'Moth', 'Coyote', 
            'Lizard', 'Hawk', 'Mole', 'Mouse', 'Oat', 'Oak', 'Plantain', 'Hemlock', 'Poplar', 
            'Owl', 'Prickle', 'Pear', 'Pebble', 'Quail', 'Rabbit', 'Rat', 'Robin', 'Rush', 'Snail', 
            'Sparrow', 'Wren', 'Deer', 'Squirrel', 'Trout', 'Timber', 'Thorn', 'Twig', 'Pecan', 
            'Skink', 'Heather'
        ],
        'LIGHTTAUPE': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Mud', 'Hazel', 'Thrasher', 
            'Warbler', 'Ash', 'Spider', 'Cedar', 'Wigeon', 'Mallard', 'Roadrunner', 'Flicker', 
            'Plover', 'Pipit', 'Moss', 'Creeper', 'Shiner', 'Shad', 'Gar', 'Puma', 'Chipmunk', 
            'Acorn', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 'Bramble', 'Briar', 'Cedar',
            'Cone', 'Dove', 'Dust', 'Eagle', 'Elm', 'Duck', 'Fern', 'Flicker', 'Flint', 'Fir', 'Frog', 
            'Goose', 'Grass', 'Gravel', 'Larch', 'Lavender', 'Leaf', 'Lichen', 'Moth', 'Coyote', 
            'Lizard', 'Hawk', 'Mole', 'Mouse', 'Oat', 'Oak', 'Plantain', 'Hemlock', 'Poplar', 
            'Owl', 'Prickle', 'Pear', 'Pebble', 'Quail', 'Rabbit', 'Rat', 'Robin', 'Rush', 'Snail', 
            'Sparrow', 'Wren', 'Deer', 'Squirrel', 'Trout', 'Timber', 'Thorn', 'Twig', 'Pecan', 
            'Skink', 'Heather'
        ],
        'FAWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Mud', 'Hazel', 'Thrasher', 
            'Warbler', 'Ash', 'Spider', 'Cedar', 'Wigeon', 'Mallard', 'Roadrunner', 'Flicker', 
            'Plover', 'Pipit', 'Moss', 'Creeper', 'Shiner', 'Shad', 'Gar', 'Puma', 'Chipmunk', 
            'Acorn', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 'Bramble', 'Briar', 'Cedar',
            'Cone', 'Dove', 'Dust', 'Eagle', 'Elm', 'Duck', 'Fern', 'Flicker', 'Flint', 'Fir', 'Frog', 
            'Goose', 'Grass', 'Gravel', 'Larch', 'Lavender', 'Leaf', 'Lichen', 'Moth', 'Coyote', 
            'Lizard', 'Hawk', 'Mole', 'Mouse', 'Oat', 'Oak', 'Plantain', 'Hemlock', 'Poplar', 
            'Owl', 'Prickle', 'Pear', 'Pebble', 'Quail', 'Rabbit', 'Rat', 'Robin', 'Rush', 'Snail', 
            'Sparrow', 'Wren', 'Deer', 'Squirrel', 'Trout', 'Timber', 'Thorn', 'Twig', 'Pecan', 
            'Skink', 'Heather'
        ],
        'LIGHTFAWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Mud', 'Hazel', 'Thrasher', 
            'Warbler', 'Ash', 'Spider', 'Cedar', 'Wigeon', 'Mallard', 'Roadrunner', 'Flicker', 
            'Plover', 'Pipit', 'Moss', 'Creeper', 'Shiner', 'Shad', 'Gar', 'Puma', 'Chipmunk', 
            'Acorn', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 'Bramble', 'Briar', 'Cedar',
            'Cone', 'Dove', 'Dust', 'Eagle', 'Elm', 'Duck', 'Fern', 'Flicker', 'Flint', 'Fir', 'Frog', 
            'Goose', 'Grass', 'Gravel', 'Larch', 'Lavender', 'Leaf', 'Lichen', 'Moth', 'Coyote', 
            'Lizard', 'Hawk', 'Mole', 'Mouse', 'Oat', 'Oak', 'Plantain', 'Hemlock', 'Poplar', 
            'Owl', 'Prickle', 'Pear', 'Pebble', 'Quail', 'Rabbit', 'Rat', 'Robin', 'Rush', 'Snail', 
            'Sparrow', 'Wren', 'Deer', 'Squirrel', 'Trout', 'Timber', 'Thorn', 'Twig', 'Pecan', 
            'Skink', 'Heather'
        ],
        'CINNAMON': [
            'Buzzard', 'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Acorn', 'Mud', 'Deer', 
            'Hickory', 'Sycamore', 'Pecan', 'Walnut', 'Spider', 'Beetle', 'Cedar', 'Bramble', 
            'Chestnut', 'Hawk', 'Roadrunner', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 
            'Bramble', 'Briar', 'Cedar', 'Cone', 'Lizard', 'Hawk', 'Plantain', 'Hemlock', 'Torreya', 
            'Mole', 'Eagle', 'Elm', 'Duck', 'Fir', 'Frog', 'Goose', 'Larch', 'Leaf', 'Oak', 'Owl', 
            'Rabbit', 'Rat', 'Sparrow', 'Wren', 'Trout', 'Timber', 'Thorn', 'Twig', 'Skink', 'Poplar', 
            'Whippoorwill', 'Creeper', 'Pelican', 'Ant', 'Shad', 'Gar', 'Mink', 'Puma', 'Beaver', 
            'Gopher', 'Chipmunk', 'Coypu', 'Chinquapin', 'Bittern', 'Swamp', 'Pine', 'Prickle', 
            'Snake', 'Snail', 'Swallow', 'Sparrow', 'Turtle', 'Cinnamon', 'Needle', 'Spindle', 'Creeper',
            'Mayhaw', 'Hawthorn', 'Wasp', 'Tiger', 'Plum'
        ],
        'DARKCINNAMON': [
            'Buzzard', 'Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud', 'Thrasher', 
            'Pecan', 'Hickory', 'Walnut', 'Ant', 'Spider', 'Beetle', 'Bramble', 'Briar', 'Cedar', 
            'Cone', 'Lizard', 'Hawk', 'Mole', 'Eagle', 'Elm', 'Bark', 'Hemlock', 'Torreya', 'Poplar', 
            'Duck', 'Fir', 'Frog', 'Goose', 'Larch', 'Leaf', 'Oak', 'Owl', 'Rat', 'Sparrow', 'Wren', 
            'Trout', 'Timber', 'Thorn', 'Twig', 'Skink', 'Whippoorwill', 'Creeper', 'Pelican', 
            'Mink', 'Beaver', 'Coypu', 'Alligator', 'Chinquapin', 'Bittern', 'Swamp', 'Pine', 
            'Prickle', 'Snake', 'Snail', 'Swallow', 'Sparrow', 'Turtle', 'Sycamore', 'Yew',
            'Cinnamon', 'Needle', 'Spindle', 'Creeper', 'Mayhaw', 'Hawthorn', 'Wasp', 'Tiger', 'Plum'
        ],
        'CARAMEL': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Mud', 'Hazel', 'Thrasher', 
            'Warbler', 'Ash', 'Spider', 'Cedar', 'Wigeon', 'Mallard', 'Roadrunner', 'Flicker', 
            'Plover', 'Pipit', 'Moss', 'Creeper', 'Shiner', 'Shad', 'Gar', 'Puma', 'Chipmunk', 
            'Acorn', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 'Bramble', 'Briar', 'Cedar',
            'Cone', 'Dove', 'Dust', 'Eagle', 'Elm', 'Duck', 'Fern', 'Flicker', 'Flint', 'Fir', 'Frog', 
            'Goose', 'Grass', 'Gravel', 'Larch', 'Lavender', 'Leaf', 'Lichen', 'Moth', 'Coyote', 
            'Lizard', 'Hawk', 'Mole', 'Mouse', 'Oat', 'Oak', 'Plantain', 'Hemlock', 'Poplar', 
            'Owl', 'Prickle', 'Pear', 'Pebble', 'Quail', 'Rabbit', 'Rat', 'Robin', 'Rush', 'Snail', 
            'Sparrow', 'Wren', 'Deer', 'Squirrel', 'Trout', 'Timber', 'Thorn', 'Twig', 'Pecan', 
            'Skink', 'Heather'
        ],
        'LIGHTCARAMEL': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Mud', 'Hazel', 'Thrasher', 
            'Warbler', 'Ash', 'Spider', 'Cedar', 'Wigeon', 'Mallard', 'Roadrunner', 'Flicker', 
            'Plover', 'Pipit', 'Moss', 'Creeper', 'Shiner', 'Shad', 'Gar', 'Puma', 'Chipmunk', 
            'Acorn', 'Bark', 'Beech', 'Boulder', 'Bracken', 'Branch', 'Bramble', 'Briar', 'Cedar',
            'Cone', 'Dove', 'Dust', 'Eagle', 'Elm', 'Duck', 'Fern', 'Flicker', 'Flint', 'Fir', 'Frog', 
            'Goose', 'Grass', 'Gravel', 'Larch', 'Lavender', 'Leaf', 'Lichen', 'Moth', 'Coyote', 
            'Lizard', 'Hawk', 'Mole', 'Mouse', 'Oat', 'Oak', 'Plantain', 'Hemlock', 'Poplar', 
            'Owl', 'Prickle', 'Pear', 'Pebble', 'Quail', 'Rabbit', 'Rat', 'Robin', 'Rush', 'Snail', 
            'Sparrow', 'Wren', 'Deer', 'Squirrel', 'Trout', 'Timber', 'Thorn', 'Twig', 'Pecan', 
            'Skink', 'Heather'
        ]
        }

    loner_names = [
        "Haku", "Pichi", "Poki", "Nagi", "Jubie", "Bonbon", "Beans", "Aurora",
        "Maleficent", "Luna", "Eclipse", "Sol", "Star", "George", "Nightmare",
        "Bagel", "Monster", "Gargoyle", "Missile Launcher", "Rolo", "Rocket",
        "Void", "Abyss", "Vox", "Princess", "Noodle", "Duchess", "Cheesecake",
        "Callie", "Randy", "Ace", "Queeny", "Freddy", "Stella", "Rooster",
        "Sophie", "Maverick", "Seamus", 'Meowyman', "Pickles", "Lacy", "Lucy",
        "Knox", "Lugnut", "Bailey", "Azula", "Lucky", "Sunny", "Sadie", "Sox",
        "Bandit", "Onyx", "Quinn", "Grace", "Fang", "Ike", "Flower",
        "Whiskers", "Gust", "Peony", 'Human', "Minnie", "Buddy", "Mollie",
        "Jaxon", "Dunnock", "Firefly", "Cheese", "Sandwich", "Spam",
        "Broccoli", "Prickle", "Insect", "Grasshopper", "Coral", "Windy",
        "Sofa", "McChicken", "Purry", "Katy", "Mop", "Fishtail", "Roman",
        "Wishbone", "Nova", "Quimby", "Quest", "Nessie", "Niles", "Neil",
        "Nutella", "Nakeena", "Nuka", "Hughie", "Harvey", "Herc", "French",
        "Finch", "Frannie", "Flutie", "Purdy", "Free", "Glory", "Snek", "Indi",
        "Igor", "Jupiter", "Nintendo", "Jesse", "James", "Jethro", "Shampoo",
        "Joker", "Jinx", "Chaos", "Havoc", "Trouble", "Kingston", "King",
        "Kip", "Kong", "Ken", "Kendra", "Kisha", "Kermit", "Kelloggs",
        "Kodiak", "Klondike", "Ketchup", "KD", "Lupo", "Luigi", "Lily", "Lora",
        "Lee", "Lex", "Lester", "Makwa", "Madi", "Minna", "Moxie", "Mucha",
        "Manda", "Monte", "Riya", "Monzi", "Nisha", "Nemo", "Nitro", "Oops",
        "O'Leary", "Ophelia", "Olga", "Oscar", "Owen", "Porsche", "Ping",
        "Pong", "Quinzee", "Quickie", "Quagmire", "Quake", "Quinoa", "Roomba",
        "Riot", "Peanut Wigglebutt", "Ramble", "Rudolph", "Rum", "Reese",
        "Scotch", "Sneakers", "Schmidt", "Espresso", "Cocoa Puff", "Sonic",
        "Teufel", "Toni", "Torque", "Tempest", "Turbo", "Tetris", "Triscuit",
        "Tumble", "Voltage", "Vinnie", "Vaxx", "Venture", "Vida", "Guinness",
        "Polly", "Piper", "Pepper", "Lakota", "Dakota", "Bently", "Chinook",
        "Tiny", "Ula", "Union", "Uriel", "Orion", "Oakley", "Roselie",
        "Belle", "Benny", "Bumblebee", "Bluebell", "Chip", "Chocolate",
        "Cracker", "Dave", "Dolly", "Egg", "Frito", "Frank", "Gibby", "Jack",
        "Jenny", "Juliet", "Joob", "John", "Jimmy", "Jude", "Kenny", "Tom",
        "Oreo", "Mocha", "Ninja", "Cinderblock", "Pip", "Pipsqueak", "Milque",
        "Toast", "Molly Murder Mittens", "Flabby", "Crunchy", "Sorbet",
        "Vanilla", "Mint", "Nikki", "Pocket", "Tabbytha", "Gravy",
        "Potato", "Chewy", "Pumpernickel", "Pecan", "Old Man Sam", "Icecube",
        "Queso Ruby", "Pearl", "Jasper", "Stan", "Rose", "Mojo", "Kate",
        "Carmen", "Mange", "Chase", "Socks", "Tabby", "Jay", "Charlie", "L",
        "Poopy", "Crunchwrap", "Meow-meow", "Bede", "Smores", "Evilface",
        "Nick", "Mitski", "Ash", "Ah", "Violet", "Alcina", "Worm", "Monika",
        "Rat", "Bongo", "Bunny", "Viktor", "Steve", "Jewels", "Blu", "Rue",
        "Stinky", "Garnet", "Anita", "Sloane", "Emi", "Vivienne", "Amber",
        "Moon", "Twilight", "River", "Glass", "Goose", "Hunter", "Amity",
        "Stripes", "Cowbell", "Rory", "Lobster", "Slug", "Starfish", "Salmon",
        "Judy", "Johnny", "Kerry", "Evelyn", "Holly", "Bolt", "Millie",
        "Jessica", "Laku", "Dragonfly", "X'ek", "Silva", "Dreamy", "Decay",
        "Jessica", "Laku", "Dragonfly", "X'ek", "Silva", "Dreamy", "Decay",
        "Twister", "Shay", "Louis", "Oleander", "Spots", "Cream", "Omelet",
        "Gizmo", "Feather", "Twix", "Silver", "Ghost", "Wisp", "Obi Wan",
        "Pikachu", "Mango", "Via", "Olivia", "Mr. Whiskers", "Fluffy",
        "Shimmer", "Mimi", "Melody", "Leon", "Punk", "Mew", "Fern",
        "Marceline", "Whisper", "Skrunkly", "Stolas", "Rio", "Steven", "Pear",
        "Sekhmet", "Melon", "Ember", "Loona", "Saki", "Tiny", "Sandy",
        "Miles", "Mini", "Judas", "Zim", "Vinyl", "Rarity", "Trixie", "Sunset",
        "Anubis", "Armin", "Amy", "Alice", "Alec", "Baphomet", "Bean",
        "Bastet", "Birb", "Burm", "Chrissy", "Cherry", "Chief", "Crow",
        "Carrie", "Calvin", "Cookie", "Catie", "Charm", "Crab", "Charles",
        "Caroline", "Conan", "Cloud", "Charlie", "Cowboy", 'Burger', "Dune",
        "Dan", "Delilah", "Emerald", "Emy", "Erica", "Eddie", "Eda", "Ferret",
        "Fawn", "Fiver", "Fallow", "Ferry", "Gamble", "Grain", "Gir", "Hop",
        "Hot Sauce", "Habanero", "Taco Bell", "Cheetoman", "Queso", "Ruby",
        "Molly", "Murder", "Mittens", "Tabatha", "Sam", "Samantha", "Peanut",
        "Wigglebutt", "Zoe", "Cheeto", "Taco", "Max", "Sparky", "Cosmo", "Fred", 
        "Leo", "Tucker", "Minette", "Milo", "Fork", "Penny", "Zelda", "Jake", 
        "Felix", "Oliver", "Kitty", "Chloe", "Angel", "Samantha", "Muschi", 
        "Chicco", "Caramel", "Charlotte", "Chanel", "Lola", "Ollie", "Boo", 
        "Frankie", "Hotdog", "Beverly", "Mera", "Tasha"
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
        loop = False
        
        # Set prefix
        if prefix is None:
            named_after_appearance = True  # Chance for True is '1/8'.
            # Add possible prefix categories to list.
            possible_prefix_categories = []
            if colour in self.colour_prefixes:
                possible_prefix_categories.append(self.colour_prefixes[colour])
            # Choose appearance-based prefix if possible and named_after_appearance because True.
            if named_after_appearance and possible_prefix_categories:
                prefix_category = random.choice(possible_prefix_categories)
                self.prefix = random.choice(prefix_category)
            else:
                self.prefix = random.choice(self.normal_prefixes)
        if suffix is None:
            loop = True
            while loop:
                if pelt is None or pelt == 'SingleColour':
                    self.suffix = random.choice(self.normal_suffixes)


    def __repr__(self):
        if self.status in ["deputy", "warrior", "medicine cat", "elder"]:
            return self.prefix + self.suffix
        else:
            return self.prefix + self.special_suffixes[self.status]


names = Name()

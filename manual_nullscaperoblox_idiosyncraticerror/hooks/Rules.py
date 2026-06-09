from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def checkWin(world: World, character: str):
    """returns require string based on region of goal level"""
    region_reqs = [
        "|Business License| and |Swiftness Ring:2|",
        "|Grace Wings| and |Double Jump|",
        "|Ninja Belt| and |Helmet| and {OptOne(|Defuse Kit:3|)}",
        "|Sports Shoes| and |Matrix Tetrahedron| and |Shark Tail|",
        "{OptOne(|Subspacial Barrier|)} and |Miniature Hourglass|",
        "|Gift Magnet:3| and |Shield|",
        "|Gift Idol:2|"
    ]

    win_lvl = world.options.level_win_requirement.value
    requires = "|" + character + " Unlock| and "

    if win_lvl >= 10:
        requires += region_reqs[0] + " and " + region_reqs[1]
    if win_lvl >= 15:
        requires += " and " + region_reqs[2]
    if win_lvl >= 20:
        requires += " and " + region_reqs[3]
    if win_lvl >= 25:
        requires += " and " + region_reqs[4]
    if win_lvl >= 30:
        requires += " and " + region_reqs[5]
    if win_lvl >= 40:
        requires += " and " + region_reqs[6]
    #keeps adding region requires depending on the win level set by option
    #done this way bcs this location would have to change region based on that option, and i dont want to deal with that
    
    return requires

def checkPrisoner(world: World):
    """returns require string based on region of goal level"""
    region_reqs = [
        "|Business License| and |Swiftness Ring:2|",
        "|Grace Wings| and |Double Jump|",
        "|Ninja Belt| and |Helmet| and {OptOne(|Defuse Kit:3|)}",
        "|Sports Shoes| and |Matrix Tetrahedron| and |Shark Tail|",
        "{OptOne(|Subspacial Barrier|)} and |Miniature Hourglass|",
        "|Gift Magnet:3| and |Shield|",
        "|Gift Idol:2|"
    ]

    win_lvl = world.options.level_win_requirement.value
    requires = "|Prisoner Unlock| and "

    if win_lvl >= 10:
        requires += region_reqs[0] + " and " + region_reqs[1]
    if win_lvl >= 15:
        requires += " and " + region_reqs[2]
    #accessible starting from round 15
    #but i guess it doesnt matter if you dont have universal tracker on lol
    
    return requires

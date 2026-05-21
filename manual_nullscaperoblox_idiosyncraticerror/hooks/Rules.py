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

def checkWin(world: World, character: str, state: CollectionState):
    """checks if class has reached level or not"""
    win_lvl = world.options.level_win_requirement.value
    check_lvl = 0
    if win_lvl%10 == 1 or win_lvl%10 == 7 or win_lvl%10 == 9:
        check_lvl = win_lvl - 1
        
    completed_levels = (check_lvl//10)*7
    if check_lvl%10 >= 2:
        completed_levels += 1
    elif check_lvl%10 >= 3:
        completed_levels += 2
    elif check_lvl%10 >= 4:
        completed_levels += 3
    elif check_lvl%10 >= 5:
        completed_levels += 4
    elif check_lvl%10 >= 6:
        completed_levels += 5
    elif check_lvl%10 >= 8:
        completed_levels += 6
        
    #if state.count(item, player) >= int(level):
    #    return True
    #return False
    #vro i think we gotta make copy locations for every fucking level dude
    #shmuck this shit we're only implementing multiple classes, fuck custom level selection
    
    
    #uhh how is this going to incorporate meeting/beating celestial LOL
    #i guess that can be the victory choice option - between levels and celestial

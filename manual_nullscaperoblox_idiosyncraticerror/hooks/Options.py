# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class ClassWinRequirement(Range):
    """
    Number of classes that have to reach goal level to progress the win condition
    """
    display_name = "Number of classes to goal on"
    range_start = 1
    range_end = 7
    default = 3

class LevelWinRequirement(Range):
    """
    What level each class must reach to progress the win condition
    Logic will treat Prisoner's goal level as 15 at the highest. If you manage to go higher send me proof and I'll change the logic lol
    !!! If you select Celestial as a goal, set level win requirement to at least 40 or the logic might be broken !!!
    !!! If you selected a level as a goal, you will need to remember what level you chose (this is the best I can do I Think) !!!
    """
    display_name = "Goal level"
    range_start = 10
    range_end = 50
    default = 15

class StartingClass(Choice):
    """
    Randomclass: See number of starting random classes
    Prisoner: Start on Prisoner
    Vanilla: Start with Diver and Charger
    If on Prisoner or Vanilla, Prisoner or Diver+Charger MUST be enabled
    """
    display_name = "Starting Classes"
    option_randomclass = 0
    option_prisoner = 1
    option_vanilla = 2
    default = 0

class RandomClassStart(Range):
    """
    How many classes you will start with if you pick random
    """
    display_name = "Number of random starting classes"
    range_start = 1
    range_end = 7
    default = 1

class FillerCount(Range):
    """
    What percentage of your locations should be filler?
    Note: 0 = none, 100 = include all locations
    """
    display_name = "Proportion of Filler"
    range_start = 0
    range_end = 100
    default = 30

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["class_win_requirement"] = ClassWinRequirement
    options["level_win_requirement"] = LevelWinRequirement
    options["start_type"] = StartingClass
    options["random_class_start"] = RandomClassStart
    options["filler_percent"] = FillerCount

    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups

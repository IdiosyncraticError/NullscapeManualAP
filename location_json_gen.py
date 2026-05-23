import json

enemies = [
    ["Bell", [1]],
    ["Mart", [1]],
    ["Baby", [1]],
    ["Springer", [1]],
    ["Husk", [1]],
    ["ICBM", [1]],
    ["Flesh", [5]],
    #["NIL", [5]],
    ["Operator", [5]],
    ["Guardian", [8]],
    ["Telefragger", [8]],
    ["Kolona", [10]],
    ["Voidbreaker", [15]],
    ["Cadence", [15]],
    ["Sigil", [15]],
    ["Voidbound Baby", [10]],
    ["Voidbound Guardian", [20]],
    ["Scrapmaw", [25]]
    #["???", [""]]
]

curses = [
    ["Lower Gravity", [1]],
    ["Random Spawn", [1]],
    ["Savory Ring", [5]],
    ["Scattered Gifts", [5]],
    ["Weaker Jump Pads", [1]],
    ["Beacon Mirage", [25]],
    ["Bigger Tripmines", [5]],
    ["High Roller", [5]],
    ["Tweaked Odds", [5]],
    ["Jackpot", [12]], #level unconfirmed
    ["Lap 2", [8]],
    ["Fragile Gifts", [8]],
    ["More Tripmines", [5]],
    ["Fake Count", [8]],
    ["Nothing?", [8]],
    ["Barotrauma", [15]],
    ["Minefield", [15]],

    ["More Ringing", [1, "Bell"]],
    ["Mighty Gong", [1, "Bell"]],
    ["Concussion", [1, "Bell"]],
    ["Mart Infection", [8, "Mart"]],
    ["Mart Slide", [8, "Mart"]],
    ["Bigger Marts", [1, "Mart"]],
    ["Closer Husk", [1, "Husk"]],
    ["Further Husk", [1, "Husk"]],
    ["Taller Husk", [1, "Husk"]],
    ["Random Husk", [15, "Husk"]],
    ["Husk Express", [8, "Husk"]],
    ["Conga Line", [10, "Husk"]],
    ["Springloaded", [5, "Springer"]],
    ["Resonating Shockwaves", [1, "Springer"]],
    ["Ambush", [8, "Telefragger"]],
    ["Accurate Telefragger", [8, "Telefragger"]],
    ["Bloodier Meat", [5, "Flesh"]],
    ["Blighted Jump Pads", [5, "Flesh"]],
    #["Cognitive Dissonance", [5, "NIL"]],
    ["Bigger Blast", [5, "ICBM"]],
    ["Scorched Earth", [1, "ICBM"]],
    ["Pacifier", [1, "Baby"]],
    ["Problem Child", [5, "Baby"]],
    ["Shotgun", [5, "Guardian"]],
    ["Camouflage", [5, "Guardian"]],
    ["Burning Bouquet", [10, "Kolona"]],
    ["Lost Embers", [10, "Kolona"]],
    ["Blade Carousel", [15, "Voidbreaker"]],
    ["Deadly Melody", [15, "Cadence"]],
    ["Blueprint: Cross Beams", [25, "Scrapmaw"]],
]

greater_curses = [
    ["Trap Card", [15]],
    ["Run", [15]],
    ["One Less Choice", [10]],
    ["Inverse Destruction", [15]],
    ["Void Implosions", [10]],
    ["Oblivion", [10]],
    ["Razorbloom", [10]],

    ["Tantrum", [10, "Baby"]],
    ["Hollow Tiles", [10, "ICBM"]],
    ["Destroyer", [15, "Husk"]],
    ["Mass Infection", [10, "Flesh"]],
    ["Ballet of Blades", [15, "Voidbreaker"]],
    ["Blade Bombardment", [15, "Voidbreaker"]],
    ["Malfunction", [10, "Operator"]],
]

rounds = [
    1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 14, 15, 16, 18, 20, 22, 23, 24, 25, 26, 28, 30
]

victory_rounds = [
    "Reach a Level", "Meet Celestial", "Beat Celestial"
]

classes = [
    "Diver",
    "Charger",
    "Grappler",
    "Spirit",
    "Glider",
    "Wanted",
    "Prisoner"
]

output = []

for i in rounds:
    obj = {}
    obj["name"] = "Level " + str(i)
    if i < 5:
        obj["region"] = "lvl 0"
    elif i < 10:
        obj["region"] = "lvl 5"
    elif i < 15:
        obj["region"] = "lvl 10"
    elif i < 20:
        obj["region"] = "lvl 15"
    elif i < 25:
        obj["region"] = "lvl 20"
    else:
        obj["region"] = "lvl 25"
    obj["category"] = "Levels"
    output.append(obj)

for i in enemies:
    obj = {}
    obj["name"] = i[0]
    
    if i[1][0] < 5:
        obj["region"] = "lvl 0"
    elif i[1][0] < 10:
        obj["region"] = "lvl 5"
    elif i[1][0] < 15:
        obj["region"] = "lvl 10"
    elif i[1][0] < 20:
        obj["region"] = "lvl 15"
    elif i[1][0] < 25:
        obj["region"] = "lvl 20"
    else:
        obj["region"] = "lvl 25"
    
    cat_list = ["Level " + str(i[1][0]) + "+"]
    cat_list.append("Enemies")
    obj["category"] = cat_list
    output.append(obj)

for i in curses:
    obj = {}
    obj["name"] = i[0]

    if i[1][0] < 5:
        obj["region"] = "lvl 0"
    elif i[1][0] < 10:
        obj["region"] = "lvl 5"
    elif i[1][0] < 15:
        obj["region"] = "lvl 10"
    elif i[1][0] < 20:
        obj["region"] = "lvl 15"
    elif i[1][0] < 25:
        obj["region"] = "lvl 20"
    else:
        obj["region"] = "lvl 25"

    cat_list = []
    cat_list.append("Level " + str(i[1][0]) + "+")
    if len(i[1]) > 1:
        cat_list.append(i[1][1]) #will need to change to accomodate more categories in the future but this is fine for now
    cat_list.append("Curses")
    obj["category"] = cat_list
    output.append(obj)

for i in greater_curses:
    obj = {}
    obj["name"] = i[0]

    if i[1][0] < 5:
        obj["region"] = "lvl 0"
    elif i[1][0] < 10:
        obj["region"] = "lvl 5"
    elif i[1][0] < 20:
        obj["region"] = "lvl 15"
    elif i[1][0] < 25:
        obj["region"] = "lvl 20"
    else:
        obj["region"] = "lvl 25"

    cat_list = []
    cat_list.append("Level " + str(i[1][0]) + "+")
    if len(i[1]) > 1:
        cat_list.append(i[1][1]) #will need to change to accomodate more categories in the future but this is fine for now
    cat_list.append("Greater Curses")
    obj["category"] = cat_list
    obj["prehint"] = True
    output.append(obj)

for l in victory_rounds:
    obj = {}
    obj["name"] = l
    #i could lowkey just make a region for the class tracker locations and make the requires the req func theyre using rn but tme bro + connections
    obj["victory"] = True
    obj["requires"] = "{OptionCount(@Win Progression, class_win_requirement)}"
    output.append(obj)

for i in classes:
    obj = {}
    obj["name"] = i + " Win Requirement"
    obj["category"] = "Class Win Tracker"
    obj["place_item"] = [i + " Win Progression Flag"]
    if i == "Prisoner":
        obj["requires"] = "{checkPrisoner()}"
    else:
        obj["requires"] = "{checkWin(" + i + ")}"
    output.append(obj)
    

with open("data.json", "w") as file:
    json.dump(output, file, indent=4)
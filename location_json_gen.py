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
    ["Voidbound ICBM", [15]],
    ["Sigil", [20]],
    ["Voidbound Baby", [10]],
    ["Voidbound Guardian", [20]],
    ["Scrapmaw", [20]]
    #["???", [""]]
]

curses = [
    ["Lower Gravity", [1]],
    ["Higher Gravity", [1]],
    ["Random Spawn", [1]],
    ["Savory Ring", [5]],
    ["Scattered Gifts", [5]],
    ["Weaker Jump Pads", [1]],
    ["Beacon Mirage", [25]],
    ["Bigger Tripmines", [5, "Standard+"]],
    ["High Roller", [5]],
    ["Tweaked Odds", [5]],
    ["Lap 2", [8]],
    ["Fragile Gifts", [8]],
    ["More Tripmines", [5, "Standard+"]],
    ["Nothing?", [8]],
    ["Jackpot", [10]],
    ["Concussive Blast", [10]],
    ["Barotrauma", [15]],
    ["Minefield", [15]],
    ["Run", [15]],
    ["Volatile Implosions", [15]],

    ["More Ringing", [1, "Bell"]],
    ["Mighty Gong", [1, "Bell"]],
    ["Concussion", [1, "Bell"]],
    ["Mart Infection", [8, "Mart"]],
    #["Mart Slide", [8, "Mart"]],
    ["Bigger Marts", [1, "Mart"]],
    ["Red Marts", [1, "Mart"]],
    ["Beacon Imp", [18, "Mart"]],
    ["Closer Husk", [1, "Husk"]],
    ["Further Husk", [1, "Husk"]],
    ["Taller Husk", [1, "Husk"]],
    ["Random Husk", [15, "Husk"]],
    ["Husk Express", [8, "Husk"]],
    ["Conga Line", [10, "Husk"]],
    ["Springloaded", [5, "Springer"]],
    ["Resonating Shockwaves", [1, "Springer"]],
    ["Seahorse", [15, "Springer"]],
    ["Horse Skipping", [5, "Springer"]],
    ["Ambush", [8, "Telefragger"]],
    ["Accurate Telefragger", [8, "Telefragger"]],
    ["Bloodier Meat", [5, "Flesh"]],
    ["Airborne Flesh", [5, "Flesh"]],
    #["Cognitive Dissonance", [5, "NIL"]],
    ["Bigger Blast", [5, "ICBM"]],
    ["Scorched Earth", [1, "ICBM"]],
    ["Magic Missile", [1, "ICBM"]],
    ["Incendiary Shrapnel", [1, "ICBM"]],
    ["Problem Child", [5, "Baby"]],
    ["Big Baby", [1, "Baby"]],
    ["Baby Steps", [5, "Baby"]],
    ["Shotgun", [8, "Guardian"]],
    ["Camouflage", [8, "Guardian"]],
    ["Burning Bouquet", [10, "Kolona"]],
    ["Lost Embers", [10, "Kolona"]],
    ["Angry Bird", [10, "Razorbloom"]],
    ["Smart Little Bird", [25, "Razorbloom", "Oblivion"]],
    ["Stronger Wings", [10, "Razorbloom"]],
    ["Blade Carousel", [15, "Voidbreaker"]],
    ["Corrupted Blades", [15, "Voidbreaker"]],
    ["Deadly Melody", [15, "Cadence"]],
    ["Jumping Instruments", [15, "Cadence", "Springer"]],
    ["Encore", [15, "Cadence"]],
    ["Alluring Arrangement", [15, "Cadence"]],
    ["Leo", [20, "Sigil"]],
    ["Sagittarius", [20, "Sigil"]],
    ["Blueprint: Cross Beams", [25, "Scrapmaw"]],
    ["Blueprint: Supersonic Lasers", [25, "Scrapmaw"]],
    ["Blueprint: Efficient Coolant", [25, "Scrapmaw"]]
]

greater_curses = [
    ["Trap Card", [15]],
    ["One Less Choice", [10]],
    ["Void Implosions", [10]],
    ["Oblivion", [10]],
    ["Razorbloom", [10]],
    ["Mania", [20]],

    ["Water Planet", [10, "Mart"]],
    ["Tantrum", [10, "Baby"]],
    ["Hollow Tiles", [10, "ICBM"]],
    ["Destroyer", [10, "Husk"]],
    ["Ouroboros", [10, "Husk"]],
    ["Mass Infection", [10, "Flesh"]],
    ["Joined Symphony", [15, "Bell", "Cadence"]],
    ["Ballet of Blades", [15, "Voidbreaker"]],
    ["Blade Bombardment", [15, "Voidbreaker"]],
    ["Malfunction", [10, "Operator"]],
    ["Blueprint: Dimensional Beams", [25, "Scrapmaw"]]
]
rounds = [
    1, 3, 5, 8, 10, 13, 15, 18, 20, 23, 25, 28, 30, 33, 35, 38, 40
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
    spec_lvl_cat = ""
    if i < 5:
        obj["region"] = "lvl 0"
        spec_lvl_cat = "Level 1+"
    elif i < 10:
        obj["region"] = "lvl 5"
        spec_lvl_cat = "Level 5+"
    elif i < 15:
        obj["region"] = "lvl 10"
        spec_lvl_cat = "Level 10+"
    elif i < 18:
        obj["region"] = "lvl 15"
        spec_lvl_cat = "Level 15+"
    elif i < 20:
        obj["region"] = "lvl 15"
        spec_lvl_cat = "Level 18+"
    elif i < 25:
        obj["region"] = "lvl 20"
        spec_lvl_cat = "Level 20+"
    elif i < 30:
        obj["region"] = "lvl 25"
        spec_lvl_cat = "Level 25+"
    elif i < 40:
        obj["region"] = "lvl 30"
        spec_lvl_cat = "Level 30+"
    else:
        obj["region"] = "lvl 40"
        spec_lvl_cat = "Level 30+"
    obj["category"] = ["Levels", spec_lvl_cat]
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
    
    if i[1][0] == 10:
        obj["region"] = "lvl 10"
    elif i[1][0] == 15:
        obj["region"] = "lvl 15"
    elif i[1][0] == 20:
        obj["region"] = "lvl 20"
    elif i[1][0] == 25:
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
    

with open("locations.json", "w") as file:
    json.dump(output, file, indent=4)
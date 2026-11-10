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

upgrades = [
    ["Adrenaline", 1, ["Solo"], 3],
    ["Swiftness Ring", 3, [], 3],
    ["Business License", 2, [], 3],
    ["Paycheck", 5, [], 3],
    ["Medal", 1, [], 5],
    ["Radar", 1, [], 5],
    ["Better Jump Pads", 1, [], 5],
    ["Tria Orbs", 1, [], 5],
    ["Grapple Points", 1, [], 5],
    ["Double Jump", 1, [], 5],
    ["Defuse Kit", 3, ["Standard+"], 5],
    ["Grace Wings", 1, ["Standard+"], 5],
    ["Pocket Bell", 1, [], 8, "|Double Jump|"],
    ["Ice Skates", 1, [], 8],
    ["Helmet", 1, [], 8],
    ["Fanny Pack", 1, [], 8],
    ["Health Insurance", 1, ["Party", "Extreme-"], 8, "|Paycheck:1|"], #not in extreme or <4 players
    ["Altar Boons", 1, [], 8],
    ["Radar Module Enemies", 1, [], 8, "|Radar|"],
    ["Radar Module Altars", 1, [], 8, "|Radar|"],
    ["Radar Module Tripmines", 1, ["Standard+"], 8, "|Radar|"],
    ["Final Stand", 1, ["Party"], 8],
    ["Advanced Gravity Coil", 1, [], 8],
    ["Star Marts", 1, [], 8],
    ["Spring Shoes", 1, [], 8],
    ["More Altars", 1, [], 10],
    ["Birthday Pony", 1, [], 10],
    ["Subspacial Barrier", 2, ["Standard+"], 10, "|Defuse Kit:3|"],
    ["Larger Grapple Points", 1, [], 13, "|Grapple Points|"],
    ["Ninja Belt", 1, [], 13],
    ["Soul Tracers", 1, ["Extreme-"], 13], #not in extreme mode
    ["Shark Tail", 1, [], 15, "|Ninja Belt|"],
    ["Propeller Hat", 1, [], 15, "|Helmet|"],
    ["Shadow Cloak", 1, [], 15],
    ["Gift Magnet", 3, [], 15],
    ["Matrix Tetrahedron", 1, [], 15],
    ["Sports Shoes", 1, [], 15],
    ["Shield", 1, [], 15],
    ["Radar Module Instruments", 1, [], 15, "|Radar|"],
    ["Panic Necklace", 1, [], 18, "|Shield|"],
    ["Fleeting Fate", 1, [], 18],
    ["Aggro Magnet", 1, [], 18, "|Gift Magnet:1|"],
    ["Debuff Magnet", 1, [], 18, "|Gift Magnet:1|"],
    ["Miniature Hourglass", 1, ["Standard+"], 20, "|Ninja Belt|"],
    ["Gift Idol", 5, [], 20, "|Gift Magnet:1|"],
    ["Drowned Aegis", 1, [], 20, "|More Altars|"],
    ["Jet Boosters", 1, [], 25],
    ["Magnified Levels", 1, [], 30],
    ["Quixotic Wing", 1, [], 30],
    ["Transient Pennon", 1, [], 30]
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

for i in upgrades:
    for j in range(i[1]):
        obj = {}
        if i[1] > 1:
            obj["name"] = "Buy " + i[0] + " " + str(j + 1)
        else:
            obj["name"] = "Buy " + i[0]

        cat_list = ["Buy Upgrades"]
        if i[3] == 3:
            obj["region"] = "lvl 0"
            cat_list.append("Level 3+")
        elif i[3] == 5:
            obj["region"] = "lvl 5"
            cat_list.append("Level 5+")
        elif i[3] == 8:
            obj["region"] = "lvl 5"
            cat_list.append("Level 8+")
        elif i[3] == 10:
            obj["region"] = "lvl 10"
            cat_list.append("Level 10+")
        elif i[3] == 13:
            obj["region"] = "lvl 10"
            cat_list.append("Level 13+")
        elif i[3] == 15:
            obj["region"] = "lvl 15"
            cat_list.append("Level 15+")
        elif i[3] == 18:
            obj["region"] = "lvl 15"
            cat_list.append("Level 18+")
        elif i[3] == 20:
            obj["region"] = "lvl 20"
            cat_list.append("Level 20+")
        elif i[3] == 25:
            obj["region"] = "lvl 25"
            cat_list.append("Level 25+")
        elif i[3] == 30:
            obj["region"] = "lvl 30"
            cat_list.append("Level 30+")
        obj["category"] = cat_list

        if i[1] > 1:
            if len(i) == 5:
                require_len = len(i[0])
                obj["requires"] = i[4] + " and |" + i[0] + ":" + str(j + 1) + "|"
            else:
                require_len = len(i[0])
                obj["requires"] = "|" + i[0] + ":" + str(j + 1) + "|"
        else:
            if len(i) == 5:
                obj["requires"] = i[4] + " and |" + i[0] + "|"
            else:
                obj["requires"] = "|" + i[0] + "|"

        output.append(obj)

    

with open("locations.json", "w") as file:
    json.dump(output, file, indent=4)
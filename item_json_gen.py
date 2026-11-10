import json

upgrades = [
    ["Adrenaline", 1, ["Solo", "Level 3+"], 2],
    ["Swiftness Ring", 3, ["Level 3+"], 4],
    ["Business License", 2, ["Level 3+"], 4],
    ["Paycheck", 5, ["Level 3+"], 4],
    ["Medal", 1, ["Level 5+"], 4],
    ["Radar", 1, ["Level 5+"], 4],
    ["Better Jump Pads", 1, ["Level 5+"], 2],
    ["Tria Orbs", 1, ["Level 5+"], 3],
    ["Grapple Points", 1, ["Level 5+"], 3],
    ["Double Jump", 1, ["Level 5+"], 4],
    ["Defuse Kit", 3, ["Level 5+", "Standard+"], 4],
    ["Grace Wings", 1, ["Level 8+", "Standard+"], 4],
    ["Pocket Bell", 1, ["Level 8+"], 4],
    ["Ice Skates", 1, ["Level 8+"], 4],
    ["Helmet", 1, ["Level 8+"], 4],
    ["Fanny Pack", 1, ["Level 8+"], 4],
    ["Health Insurance", 1, ["Level 8+", "Party", "Extreme-"], 3], #not in extreme or <4 players
    ["Altar Boons", 1, ["Level 8+"], 2],
    ["Radar Module Enemies", 1, ["Level 8+"], 4],
    ["Radar Module Altars", 1, ["Level 8+"], 2],
    ["Radar Module Tripmines", 1, ["Level 8+", "Standard+"], 3],
    ["Final Stand", 1, ["Level 8+", "Party"], 3],
    ["Advanced Gravity Coil", 1, ["Level 8+"], 4],
    ["Star Marts", 1, ["Level 8+"], 2],
    ["Spring Shoes", 1, ["Level 8+"], 2],
    ["More Altars", 1, ["Level 10+"], 2],
    ["Birthday Pony", 1, ["Level 10+"], 2],
    ["Subspacial Barrier", 2, ["Level 10+", "Standard+"], 4],
    ["Larger Grapple Points", 1, ["Level 13+"], 2],
    ["Ninja Belt", 1, ["Level 13+"], 4],
    ["Soul Tracers", 1, ["Level 13+", "Extreme-"], 2], #not in extreme mode
    ["Shark Tail", 1, ["Level 15+"], 4],
    ["Propeller Hat", 1, ["Level 15+"], 4],
    ["Shadow Cloak", 1, ["Level 15+"], 4],
    ["Gift Magnet", 3, ["Level 15+"], 4],
    ["Matrix Tetrahedron", 1, ["Level 15+"], 4],
    ["Sports Shoes", 1, ["Level 15+"], 4],
    ["Shield", 1, ["Level 15+"], 4],
    ["Radar Module Instruments", 1, ["Level 15+"], 3],
    ["Panic Necklace", 1, ["Level 18+"], 2],
    ["Fleeting Fate", 1, ["Level 18+"], 3],
    ["Aggro Magnet", 1, ["Level 18+"], 3],
    ["Debuff Magnet", 1, ["Level 18+"], 2],
    ["Miniature Hourglass", 1, ["Level 20+", "Standard+"], 4],
    ["Gift Idol", 5, ["Level 20+"], 4],
    ["Drowned Aegis", 1, ["Level 20+"], 3],
    ["Jet Boosters", 1, ["Level 25+"], 4],
    ["Magnified Levels", 1, ["Level 30+"], 4],
    ["Quixotic Wing", 1, ["Level 30+"], 3],
    ["Transient Pennon", 1, ["Level 30+"], 3]
]

delusions = [
    ["Conceit", 2],
    ["Arrogance", 2],
    ["Dependence", 4],
    ["Hope", 4],
    ["Corrosion", 4],
    ["Vandalism", 4],
    ["Ignorance", 4],
    ["Overconfidence", 2],
    ["Burnout", 2],
    ["Gambling", 2],
    ["Assurance", 2],
    ["Perseverance", 4],
    ["Hoarding", 2],
    ["Desire", 2],
    ["Greed", 2]
]

class_unlock = [
    "Diver",
    "Charger",
    "Grappler",
    "Spirit",
    "Glider",
    "Wanted",
    "Prisoner"
]

output = []
for i in upgrades:
    obj = {}

    obj["count"] = i[1]
    obj["name"] = i[0]
    
    cat_list = i[2]
    cat_list.append("Upgrades")
    obj["category"] = cat_list
    
    if i[3] == 1:
        obj["filler"] = True
    elif i[3] == 2:
        obj["useful"] = True
    elif i[3] == 3:
        obj["progression_skip_balancing"] = True
    elif i[3] == 4:
        obj["progression"] = True

    output.append(obj)

for i in delusions:
    obj = {}

    obj["count"] = 1
    obj["name"] = i[0]
    obj["category"] = ["Delusions", "Level 15+"]
    if i[1] == 2:
        obj["useful"] = True
    elif i[1] == 4:
        obj["progression"] = True
    output.append(obj)

for i in class_unlock:
    obj = {}
    obj["count"] = 1
    obj["name"] = i + " Unlock"
    
    obj["category"] = ["Class Unlock"]

    obj["progression"] = True

    output.append(obj)

for i in class_unlock:
    obj = {}
    obj["count"] = 1
    obj["name"] = i + " Win Progression Flag"
    obj["category"] = ["Win Progression"]
    obj["progression"] = True
    output.append(obj)
    

with open("items.json", "w") as file:
    json.dump(output, file, indent=4)
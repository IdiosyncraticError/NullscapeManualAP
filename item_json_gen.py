import json

upgrades = [
    ["Adrenaline", "1", ["Solo", "Level 3+"], 2],
    ["Swiftness Ring", "3", ["Level 3+"], 4],
    ["Business License", "2", ["Level 3+"], 4],
    ["Paycheck", "5", ["Level 3+"], 4],
    ["Medal", "1", ["Level 5+"], 2],
    ["Radar", "1", ["Level 5+"], 2],
    ["Better Jump Pads", "1", ["Level 5+"], 2],
    ["Tria Orbs", "1", ["Level 5+"], 2],
    ["Grapple Points", "1", ["Level 5+"], 2],
    ["Double Jump", "1", ["Level 5+"], 4],
    ["Defuse Kit", "3", ["Level 5+", "Standard+"], 3],
    ["Grace Wings", "1", ["Level 8+"], 4],
    ["Pocket Bell", "1", ["Level 8+"], 4],
    ["Ice Skates", "1", ["Level 8+"], 3],
    ["Helmet", "1", ["Level 8+"], 3],
    ["Fanny Pack", "1", ["Level 8+"], 4],
    ["Radar Module: Enemies", "1", ["Level 8+"], 3],
    ["Radar Module: Altars", "1", ["Level 8+"], 2],
    ["Radar Module: Tripmines", "1", ["Level 8+", "Standard+"], 3],
    ["Radar Module: Players", "1", ["Level 8+", "Multiplayer"], 2],
    ["Last Man Standing", "1", ["Level 8+", "Multiplayer"], 3],
    ["Advanced Gravity Coil", "1", ["Level 8+"], 3],
    ["More Altars", "1", ["Level 10+"], 2],
    ["Subspacial Barrier", "2", ["Level 10+", "Standard+"], 4],
    ["Larger Grapple Points", "1", ["Level 13+"], 2],
    ["Ninja Belt", "1", ["Level 13+"], 4],
    ["Shark Tail", "1", ["Level 15+"], 4],
    ["Gift Magnet", "3", ["Level 15+"], 4],
    ["Matrix Tetrahedron", "1", ["Level 15+"], 4],
    ["Sports Shoes", "1", ["Level 15+"], 4],
    ["Shield", "1", ["Level 15+"], 4],
    ["Radar Module: Instruments", "1", ["Level 15+"], 3],
    ["Panic Necklace", "1", ["Level 18+"], 2],
    ["Miniature Hourglass", "1", ["Level 20+"], 3],
    ["Gift Idol", "5", ["Level 20+"], 3],
    ["Drowned Aegis", "1", ["Level 20+"], 3]
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

traps = [
    "Purgatory Trap", #use the next purgatory altar you see
    "Echo Trap" #use the next echo altar you see
    "Purification Trap" #use the next purification altar you see
    "No Reroll Trap" #not allowed to reroll until next intermission phase
]

output = []
for i in upgrades:
    obj = {}

    obj["count"] = i[1]
    obj["name"] = i[0]
    
    obj["category"] = i[2]
    
    if i[3] == 1:
        obj["filler"] = True
    elif i[3] == 2:
        obj["useful"] = True
    elif i[3] == 3:
        obj["progression_skip_balancing"] = True
    elif i[3] == 4:
        obj["progression"] = True

    output.append(obj)

for i in class_unlock:
    obj = {}
    obj["count"] = "1"
    obj["name"] = i + " Unlock"

    if i == "Wanted":
        obj["category"] = ["Wanted"]
    elif i == "Prisoner":
        obj["category"] = ["Prisoner"]

    obj["progression"] = True
    

with open("data.json", "w") as file:
    json.dump(output, file, indent=4)
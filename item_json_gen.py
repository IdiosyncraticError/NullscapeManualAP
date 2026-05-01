import json

upgrades = [
    ["Adrenaline", "1", "Solo", 2],
    ["Swiftness Ring", "3", "", 4],
    ["Business License", "2", "", 4],
    ["Paycheck", "5", "", 4],
    ["Orb", "1", "Casual", 2],
    ["Medal", "1", "", 2],
    ["Radar", "1", "", 2],
    ["Better Jump Pads", "1", "", 2],
    ["Tria Orbs", "1", "", 2],
    ["Grapple Points", "1", "", 2],
    ["Double Jump", "1", "", 4],
    ["Defuse Kit", "3", "Standard+", 3],
    ["Grace Wings", "1", "", 4],
    ["Pocket Bell", "1", "", 4],
    ["Larger Grapple Points", "1", "", 2],
    ["Ice Skates", "1", "", 3],
    ["Helmet", "1", "", 3],
    ["Fanny Pack", "1", "", 4],
    ["Advanced Gravity Coil", "1", "", 3],
    ["More Altars", "1", "", 2],
    ["Last Man Standing", "1", "Multiplayer", 3],
    ["Radar Module: Enemies", "1", "", 3],
    ["Radar Module: Altars", "1", "", 2],
    ["Radar Module: Players", "1", "Multiplayer", 2],
    ["Radar Module: Tripmines", "1", "Standard+", 3],
    ["Ninja Belt", "1", "", 4],
    ["Subspacial Barrier", "2", "Standard+", 4],
    ["Shark Tail", "1", "", 4],
    ["Gift Magnet", "3", "", 4],
    ["Matrix Tetrahedron", "1", "", 4],
    ["Shield", "1", "", 4],
    ["Radar Module: Instruments", "1", "", 3],
    ["Panic Necklace", "1", "", 2],
    ["Miniature Hourglass", "1", "", 3],
    ["Gift Idol", "5", "", 3],
    ["Drowned Aegis", "1", "", 3]
]

output = []
for i in upgrades:
    obj = {}
    category = [] #for if theres multiple categories

    obj["count"] = i[1]
    obj["name"] = i[0]
    
    if i[2] != "":
        obj["category"] = [i[2]]
    
    if i[3] == 1:
        obj["filler"] = True
    elif i[3] == 2:
        obj["useful"] = True
    elif i[3] == 3:
        obj["progression_skip_balancing"] = True
    elif i[3] == 4:
        obj["progression"] = True

    output.append(obj)
    

with open("data.json", "w") as file:
    json.dump(output, file, indent=4)
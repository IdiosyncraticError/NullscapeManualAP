import json

enemies = [
    ["Bell", ["Level 1+"]],
    ["Mart", ["Level 1+"]],
    ["Baby", ["Level 1+"]],
    ["Springer", ["Level 1+"]],
    ["Husk", ["Level 1+"]],
    ["ICBM", ["Level 1+"]],
    ["Flesh", ["Level 5+"]],
    ["NIL", ["Level 5+"]],
    ["Operator", ["Level 5+"]],
    ["Guardian", ["Level 8+"]],
    ["Telefragger", ["Level 8+"]],
    ["Kolona", ["Level 10+"]],
    ["Voidbreaker", ["Level 15+"]],
    ["Cadence", ["Level 15+"]],
    ["Voidbound Baby", ["Level 10+"]],
    ["Voidbound Guardian", ["Level 20+"]],
    ["Scrapmaw", ["Level 25+"]]
    #["???", [""]]
]

curses = [
    ["Lower Gravity", ["Level 1+"]],
    ["Random Spawn", ["Level 1+"]],
    ["Savory Ring", ["Level 5+"]],
    ["Scattered Gifts", ["Level 5+"]],
    ["Weaker Jump Pads", ["Level 1+"]],
    ["Beacon Mirage", ["Level 25+"]],
    ["Bigger Tripmines", ["Level 5+"]],
    ["High Roller", ["Level 5+"]],
    ["Tweaked Odds", ["Level 5+"]],
    ["Jackpot", ["Level 12+"]], #level unconfirmed
    ["Lap 2", ["Level 8+"]],
    ["Fragile Gifts", ["Level 8+"]],
    ["More Tripmines", ["Level 5+"]],
    ["Fake Count", ["Level 8+"]],
    ["Nothing?", ["Level 8+"]],
    ["Barotrauma", ["Level 15+"]],
    ["Minefield", ["Level 15+"]],

    ["More Ringing", ["Level 1+", "Bell"]],
    ["Mighty Gong", ["Level 1+", "Bell"]],
    ["Concussion", ["Level 1+", "Bell"]],
    ["Mart Infection", ["Level 1+", "Mart"]],
    ["Mart Slide", ["Level 1+", "Mart"]],
    ["Bigger Marts", ["Level 1+", "Mart"]],
    ["Closer Husk", ["Level 1+", "Husk"]],
    ["Further Husk", ["Level 1+", "Husk"]],
    ["Taller Husk", ["Level 1+", "Husk"]],
    ["Random Husk", ["Level 15+", "Husk"]],
    ["Husk Express", ["Level 8+", "Husk"]],
    ["Conga Line", ["Level 10+", "Husk"]],
    ["Springloaded", ["Level 5+", "Springer"]],
    ["Resonating Shockwaves", ["Level 1+", "Springer"]],
    ["Ambush", ["Level 8+", "Telefragger"]],
    ["Accurate Telefragger", ["Level 8+", "Telefragger"]],
    ["Bloodier Meat", ["Level 5+", "Flesh"]],
    ["Blighted Jump Pads", ["Level 5+", "Flesh"]],
    ["Cognitive Dissonance", ["Level 5+", "NIL"]],
    ["Bigger Blast", ["Level 5+", "ICBM"]],
    ["Scorched Earth", ["Level 1+", "ICBM"]],
    ["Pacifier", ["Level 1+", "Baby"]],
    ["Problem Child", ["Level 5+", "Baby"]],
    ["Shotgun", ["Level 5+", "Guardian"]],
    ["Camouflage", ["Level 5+", "Guardian"]],
    ["Burning Bouquet", ["Level 10+", "Kolona"]],
    ["Lost Embers", ["Level 10+", "Kolona"]],
    ["Blade Carousel", ["Level 15+", "Voidbreaker"]],
    ["Deadly Melody", ["Level 15+", "Cadence"]],
    ["Blueprint: Cross Beams", ["Level 25+", "Scrapmaw"]],
]

greater_curses = [
    ["Trap Card", ["Level 15+"]],
    ["Run", ["Level 15+"]],
    ["One Less Choice", ["Level 10+"]],
    ["Inverse Destruction", ["Level 15+"]],
    ["Void Implosions", ["Level 10+"]],
    ["Oblivion", ["Level 10+"]],
    ["Razorbloom", ["Level 10+"]],

    ["Tantrum", ["Level 10+", "Baby"]],
    ["Hollow Tiles", ["Level 10+", "ICBM"]],
    ["Destroyer", ["Level 15+", "Husk"]],
    ["Mass Infection", ["Level 10+", "Flesh"]],
    ["Ballet of Blades", ["Level 15+", "Voidbreaker"]],
    ["Blade Bombardment", ["Level 15+", "Voidbreaker"]],
    ["Malfunction", ["Level 10+", "Operator"]],
]

rounds = [
    1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 14, 15, 16, 18, 20, 22, 23, 24, 25, 26, 28, 30
]

output = []
for i in rounds:
    obj = {}
    obj["name"] = "Level " + str(i)
    obj["category"] = "Levels"
    output.append(obj)

for i in enemies:
    obj = {}
    obj["name"] = i[0]
    
    cat_list = i[1]
    cat_list.append("Enemies")
    obj["category"] = cat_list
    output.append(obj)

for i in curses:
    obj = {}
    obj["name"] = i[0]
    cat_list = i[1]
    cat_list.append("Curses")
    obj["category"] = cat_list
    output.append(obj)

for i in greater_curses:
    obj = {}
    obj["name"] = i[0]
    cat_list = i[1]
    cat_list.append("Greater Curses")
    obj["category"] = cat_list
    output.append(obj)
    

with open("data.json", "w") as file:
    json.dump(output, file, indent=4)
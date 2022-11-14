import json

with open('_.json') as f:
    asdf = json.load(f)

"""
{
    "MapName": "bhop_citnez",
    "RowID": 6,
    "MapID": 3,
    "Type": 1,
    "point00": -2176,
    "point01": -3296,
    "point02": 1089.03125,
    "point10": -1984,
    "point11": -3616,
    "point12": 1217.03125,
    "unrestrict": 0,
    "ezhop": 0,
    "autohop": 0,
    "nolimit": 0,
    "actype": 0
}
"""

def FillBoxMinMax(a, b):
    for i in range(3):
        y,u = a[i],b[i]
        a[i] = float(min(y,u))
        b[i] = float(max(y,u))

d = {}
freestyles = {}
for row in asdf:
    mapname = row["MapName"].lower()
    if not mapname in d:
        d[mapname] = []
    del row["MapName"]
    row["id"] = row["RowID"]
    del row["RowID"]
    del row["MapID"]
    
    row["point_a"] = []
    row["point_a"].append(row["point00"])
    row["point_a"].append(row["point01"])
    row["point_a"].append(row["point02"])
    del row["point00"]
    del row["point01"]
    del row["point02"]
    row["point_b"] = []
    row["point_b"].append(row["point10"])
    row["point_b"].append(row["point11"])
    row["point_b"].append(row["point12"])
    del row["point10"]
    del row["point11"]
    del row["point12"]
    
    FillBoxMinMax(row["point_a"], row["point_b"])
    
    type = row["Type"]
    del row["Type"]
    if type == 0:
        row["type"] = "start"
        row["track"] = 0
    elif type == 1:
        row["type"] = "end"
        row["track"] = 0
    elif type == 2:
        row["type"] = "start"
        row["track"] = 1
    elif type == 3:
        row["type"] = "end"
        row["track"] = 1
    elif type == 4:
        row["type"] = "stop"
        row["track"] = 0
    elif type == 5:
        row["type"] = "freestyle"
        row["track"] = 0
        ### TODO: FUCK THIS HONESTLY
        if not mapname in freestyles:
            freestyles[mapname] = []
        freestyles[mapname].append(row)
        continue
    elif type == 6:
        row["type"] = "slide"
        row["track"] = 0

    # TODO:
    del row["autohop"]
    del row["ezhop"]
    del row["nolimit"]
    del row["unrestrict"]

    actype = row["actype"]
    del row["actype"]
    if actype == 3 or actype == 1:
        row["type"] = "stop"
        row["track"] = 0
        d[mapname].append(row)
    elif actype == 3 or actype == 2:
        row["type"] = "stop"
        row["track"] = 1
        d[mapname].append(row)
    else:
        d[mapname].append(row)

for map in d:
    with open(map + ".json", "w") as f:
        json.dump(d[map], f, sort_keys=True, indent='\t', separators=(',', ': '))

for map in freestyles:
    with open("todofreestyle/" + map + ".json", "w") as f:
        json.dump(freestyles[map], f, sort_keys=True, indent='\t', separators=(',', ': '))


factorsF = {"benzin": 2.33, "diesel": 2.64, "lpg": 1.64}
factorsE = 0.58
decode = ["benzin", "diesel", "lpg"]
timespan = 360  # Days


def main():
    datalist = crawlinput()
    # to#do aufloesen der datalist
    for i in datalist:
        data = calculate(i)
        # to#do evtl data type (data[3]) aufloesen
        if data[2] != None:
            saveinrank(data[0], data[2], data[3])


def saveinrank(id, co2val, type):
    co2perts = co2val * timespan
    if type == "e":
        # write
        pass
    elif type == "f":
        # write
        pass
        # calculate added values


def crawlinput():
    alllist = []  # todo crawl here
    return alllist


def calculate(data):
    id = data["ID"]
    time = data["time"]
    datatype = data["type"]
    if datatype == "f":  ##fuel
        factor = factorsF[decode[data["definition"]]]
        co2temp = data["value"] * factor
        refL, refTime = getref(id, "f")
        co2val = None
        if refL == None:
            setref(id, co2temp, time, "f")
        elif time > refTime:
            co2val = refL / (time - refTime)
    elif datatype == "e":  ##energy
        val = calcEnergy(id, data["value"], time)
        if val == None:
            co2val = None
        else:
            co2val = val * factorsE
    else:
        co2val = None
    return id, time, co2val, datatype


def calcEnergy(id, ZS, time):
    refZS, refTime = getref(id, "e")
    if refZS == None:
        setref(id, ZS, time, "e")
        return None
    verbrauch = None
    if time > refTime and ZS > refZS:
        setref(id, ZS, time, "e")
        verbrauch = (ZS - refZS) / (time - refTime)
    return verbrauch  # to#do safe if v = 0


def getref(id, typ):
    data = crawlref(id)
    val = None
    time = None
    # todo crawl
    if typ == "e":
        val = data["kwh"]
        time = data["timekwh"]
    elif typ == "f":
        val = data["l"]
        time = data["timel"]
    return val, time


def setref(id, val, time, typ):
    if typ == "e":
        pass
        # todo set reference
    elif typ == "f":
        pass
        # todo set reference


def crawlref(id):
    pass
    # todo add reference crawler

    # To#do getref(id, typ) and setref(id, Zaehler, Zeit, typ)

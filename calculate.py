factorsTS={"benzin":2.33,"diesel":2.64,"lpg":1.64}
factorsE=0.58
decode = ["benzin","diesel","lpg"]

def main():
    datalist=crawlinput()
    #to#do auflösen der datalist
    for i in datalist:
        data=calculate(i)
        if data[2] != None:
            saveinrank(data[0],data[1],data[2],data[3])

def saveinrank(id, time, co2val, type):


def crawlinput():
    alllist=[] #todo crawl here
    return alllist

def calculate(data):
    id = data["ID"]
    time = data["time"]
    if data["type"]=="l":
        factor=factorsTS[decode[data["definition"]]]
        co2temp=data["value"]*factor
        refL, refTime = getref(id,"f")
        co2val=None
        if refL==None:
            setref(id,co2temp,time,"f")
        elif time > refTime:
            co2val=refL/(time-refTime)
    elif data["type"]=="kwh":
        val=calcEnergy(id, data["value"], time)
        if val == None:
            co2val=None
        else:
            co2val=val*factorsE
    else:
        co2val=None
    return id, time, co2val, data["type"]

def calcEnergy(id, ZS, time):
    refZS, refTime = getref(id, "e")
    if refZS == None:
        setref(id, ZS, time, "e")
        return None
    verbrauch=None
    if time > refTime and ZS > refZS:
        setref(id, ZS, time, "e")
        verbrauch = (ZS-refZS)/(time-refTime)
    return verbrauch #to#do safe if v = 0

def getref(id, typ):
    val = None
    time = None
    #todo crawl
    if typ=="e":
        val=data["kwh"]
        time=data["timekwh"]
    elif typ=="f":
        val=data["l"]
        time=data["timel"]
    return val, time

def setref(id, val, time, typ):
    if typ=="e":

    elif typ == "f":


#Todo getref(id, typ) and setref(id, Zähler, Zeit, typ)

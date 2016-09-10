import random

def rint():
    return "'"+str(random.randint(0,20000))+"'"

def rstr():
    return "'"+random_id(random.randint(1,10))+"'"

def random_id(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id

for i in range(150):
    a = rint()
    b = rstr()
    c = rstr()
    d = rint()
    e = rint()
    f = rint()

    #out = {"id":a,"name":b,"email":c,"co2value":d,"co2energy":e,"co2fuel":f}

    code = ("INSERT INTO sf_user(id,name,email,co2value,co2energy,co2fuel) VALUES ("+a+","+b+","+c+","+d+","+e+","+f+");")

    print code

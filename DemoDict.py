# DemoDict.py

color = {"apple":"red", "banana":"yellow"}
color["kiwi"]="green"
print(color)
print(color["apple"])

del color["apple"]
print(color)

print("---형식변경---")

a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)

device = {"iphon":5, "ipad":10, "window":20}
device["macbook"]=15

for item in device.items():
    print(item)

for k,v in device.items():
    print(k,v)


phone = {"kim":"111", "lee":"222", "park":"333"}
print( "park" in phone)
print("kang" not in phone)
p = phone
p["kang"]="444"
print(phone)
print(p)
print( id(phone), id(p))
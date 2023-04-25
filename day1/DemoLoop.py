# DemoLoop.py

value = 5
while value > 0:
    print(value)
    value -= 1

lst = [100,200,300]
fruit = {"apple":100,"banana":200}
for item in fruit.items():
    print(item)


print("---break 구문---")
lst = list(range(1,11))
for i in lst:
    if i > 5:
        break
    print("item:{0}".format(i))

print("--- continue 구문---")
lst = list(range(1,11))
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))

print("--- range() 함수 test ---")
print(list(range(2000,2024)))
print(list(range(1,32)))

lst = list(range(1,11))
print("--- 리스트 컴프리헨션---")
print([i**2 for i in lst if i>5])
fruits = {100:"apple", 200:"orange"}
print([v.upper() for v in fruits.values()])

# 필터링함수
lst = [10,25,40]
def getBiggerThan20(i):
    return i > 20
itemL = filter(getBiggerThan20, lst)
for i in itemL:
    print(i)

# 람다함수
lst = [10,25,40]
itemL = filter(lambda x : x>20, lst)
for i in itemL:
    print(i)

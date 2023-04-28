# DemoRandom.py

import random
from os.path import *
from os import *
import glob

print(random.random())
print(random.random())
print(random.uniform(2.0, 5.0))

print([random.randrange(20) for i in range(10)]) # 중복된것도 나옴
print([random.randrange(20) for i in range(10)])

print(random.sample(range(20),10)) # unique한거 봅고싶을때
print(random.sample(range(20),10))

print("---file info---")

print(abspath("python.exe"))  # --> :\WORK\python.exe
print(basename("C:\\Phthon310\\python.exe")) # --> python.exe
if exists("C:\\Phthon310\\python.exe"):
    print(getsize("C:\\Phthon310\\python.exe"))
else:
    print("no file")

# 특정 파일을 실행
# system("notepad.exe") # -> notepad 뜸

print("운영체제이름:{0}".format(name))

lst = glob.glob("C:\\WORK\\*.py")
#print(lst)
for item in lst:
    print(item)
# DemoFileIO.py

# 쓰기
#f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f = open(r"c:\WORK\demo.txt", "wt", encoding="utf-8")
f.write("first\nsecond\nthird\n")
f.close()

# 읽기
f = open(r"c:\WORK\demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
f.close()
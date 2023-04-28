# DemoFormat.py

#URL = "http://www.credu.com/?page=" + 1  # 형식 일치 안해서 에러남
URL = "http://www.credu.com/?page=" + str(1)
print(URL)

for x in range(1,6):
    print(x, "*", x, "=", x*x)
# 오른쪽 정렬
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))
# 0으로 채우기
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).zfill(5))

# 서식 지정 문자
print("{0:x}".format(10)) # 10진수 10을 16진수로
print("{0:b}".format(10)) #             2진수로
print("{0:,}".format(150000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
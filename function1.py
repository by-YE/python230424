# function1.py

# 1)함수 정의
def times(a,b):
    return a*b
# 2) 함수 호출
result = times(3,4)
print(result)

def setValue(newValue):
    #지역변수
    x = newValue
    print("함수내부:", x)


# 호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

print(swap(3,4))


# 디버깅 연습
def intersect(prelist, postlist):
    #교집합 문자를 모아둘 리스트 초기화(지역변수)
    result = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        # x라는 글자가 postlist에 있고 x 아직 result에 없으면
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출(디버깅시에 중단점 red dot)
print(intersect("HAM","SPAM"))


#지역변수와 전역번수

x = 5 #전역변수
def func(a):
    return x+a
print(func(1))

def func2(a):
    x=10  #지역변수
    return x+a
print(func2(1))


def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

# 키워드 인자 방식
def connectURI(server, port):
    strURL = "http://"+server+":"+port
    return strURL
print(connectURI("credu.com","80"))
print(connectURI(port="8080", server ="credu.com"))

#선택한 행들을 주석처리: ctrl +/
# print(dir())
# print(globals())
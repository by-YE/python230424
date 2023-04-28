# web1.py

# 크롤링을 위한 선언
from bs4 import BeautifulSoup

# 페이지를 로딩
page = open(r"C:/WORK/day3/test01.html","rt",encoding="utf-8").read() 
# .read() 첨부터 쭉 읽어서 문자열로 전송

#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())

# <p> 태그 전부 검색
#print(soup.find_all("p"))

# <p> 하나만 검색
#print(soup.find("p")) #첫번째꺼 찾고 빠져나옴

# <p> class="outer-text"> 조건이 있는경우 (조건 걸어서 검색)
#print(soup.find_all("p",class_="outer-text"))  #class 가 쓰이는거라 class_ 언더바 붙임
#print(soup.find_all("p", attrs={"class":"outer-text"}))  # attrs attribute

for item in soup.find_all("p"):
    # 태그는 버리고 컨텐츠만 사용
    title = item.text.strip()
    title = title.replace("\n","")
    print(title)



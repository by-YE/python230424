# DemoForm2.py
# DemoForm2.ui(화면을 디자인한 파일) + DemoForm2.py(실제 로직이 저장됨)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#웹서버와 통신
import requests
# 당근마켓 크롤링
from bs4 import BeautifulSoup

#디자인한 파일을 로딩
form_class = uic.loadUiType("C:/WORK/day4/DemoForm2.ui")[0]
#윈도우(폼)클래스 정의(QMainWindow상속)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    def firstClick(self):
        #self.label.setText("첫번째 버튼~~")
        self.label.setText("당근마켓 크롤링 완료~~")
        # 크롤링하는 부분 추가
        url = "https://www.daangn.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        f = open("C:/WORK/day4/daangn.txt", "wt", encoding="utf-8")

        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            title = post.find("h2", attrs={"class":"card-title"})
            price = post.find("div", attrs={"class":"card-price"})
            title = title.text.replace("\n","")
            price = price.text.replace("\n","")
            print("{0}, {1}".format(title, price))
            result = f"매물:{title} 가격: {price} \n"
            f.write(result)
        f.close()


    def secondClick(self):
        self.label.setText("두번째 버튼~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼~~")

#직접 모듈을 실행한 경우 인스턴스 생성
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm() 
    demoForm.show() 
    app.exec_() 
# db1.py  # DB SQLite 

import sqlite3

#연결객체 생성(메모리에서 연습)
con = sqlite3.connect(":memory:") #연습을 위한
#SQL 구문을 실행할 커서 객체
cur = con.cursor()
#테이블 구조(스키마) 생성
cur.execute(" create table if not exists PhoneBook " +
            " (id integer primary key autoincrement, name text, phoneNum text); ")
#1건 입력
cur.execute(" insert into PhoneBook (name, phoneNum) values " + 
            " ('홍길동', '010-2334-2345'); ")

#입력 파라메터 처리
name = "이순신"
phoneNumber = "010-2333-5454"
cur.execute(" insert into PhoneBook (name, phoneNum) values " + 
            " (?, ?);", (name, phoneNumber) )


# 다중의 데이터를 입력(2차원배열)
datalist = (("전우치","010-3121-3532"), ("박문수","010-2231-3982"))
cur.executemany(" insert into PhoneBook (name, phoneNum) values " + 
            " (?, ?);", datalist )

#검색
cur.execute(" select * from PhoneBook; ")
for row in cur:
    print(row)




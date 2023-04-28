# db2.py  # DB SQLite 

import sqlite3

#연결객체 생성(파일에 저장)
#con = sqlite3.connect("test.db")  #경로 지정안하면 작업 폴더에 저장됨
con = sqlite3.connect("c:/WORK/day3/sample.db")  # con.commit() 마지막에 해줘야함

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
# print("--fetchone()---")
# print(cur.fetchone()) # 하나 보여주고 버퍼에서 지움
# print("--fetchmany(2)---")
# print(cur.fetchmany(2))
cur.execute(" select * from PhoneBook; ") #다시 버퍼에 채움
print("--fetchall()---")
print(cur.fetchall())

#작업 정상 종료 (중요!)
con.commit()

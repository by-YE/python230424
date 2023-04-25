# 부모 클래스 정의
class Person: #class Person(object): object 안적어도 됨
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

# 자식 클래스 정의
class Student(Person):
    # 초기화메서드르 상속받아서 재정의(덮어씀)
    def __init__(self, name, phoneNumber, subject, studentID):
        self.name = name
        self.phoneNumber = phoneNumber
        # 위처럼 다 정의하지 않고, 부모꺼를 호출해도됨
        #Person.__init__(self, name, phoneNumber, subject, StudentID)
        self.subject = subject
        self.studentID = studentID

#인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
print(p.__dict__)
print(s.__dict__)
p.printInfo
s.printInfo



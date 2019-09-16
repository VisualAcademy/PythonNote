# 생성자 매개변수

class My:
    # 생성자의 매개변수를 사용하여 필드 초기화
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myInfo(self):
        print("이름: {0}, 나이: {1}".format(self.name, self.age))

my = My("홍길동", 21)
my.myInfo()


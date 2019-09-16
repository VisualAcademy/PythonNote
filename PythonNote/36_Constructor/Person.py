# 클래스 선언
class Person:
    # 생성자
    def __init__(self, name):
        self.name = name
    # 메서드
    def get_name(self):
        return self.name

# 개체 생성
person1 = Person("홍길동")
print(person1.get_name())

person2 = Person("백두산")
print(person2.get_name())

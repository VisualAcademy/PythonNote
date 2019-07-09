# 생성자(Constructor): 클래스에서 제일 먼저 실행되는 메서드

class MyClass:
    def __init__(self):
        print("[1] 생성자가 호출되었습니다.")
    def otherMethod(self):
        print("[2] 다른 메서드가 호출됩니다.")

myClass = MyClass()
myClass.otherMethod()



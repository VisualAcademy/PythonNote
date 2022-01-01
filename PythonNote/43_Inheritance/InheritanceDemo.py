# [?] 상속(Inheritance): 부모 클래스의 기능을 자식 클래스에서 물려받아 사용

# 부모: Base
class Parent():
    def Say(self):
        print("부모 말하다.")

# 자식: Derived
class Child(Parent):
    #pass
    def Say(self):
        Parent.Say(self) 
        print("자식 말하다.")

# 자식 클래스의 인스턴스 생성
child = Child()
child.Say() # 부모로부터 상속

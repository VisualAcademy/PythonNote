# 클래스 선언
class Car():
    def Run(self):
        print("자동차가 달립니다.")
    def RunBy(self, direction):
        print("자동차가 달립니다. 어디로? " + direction)


# 클래스의 인스턴스 생성
car = Car()
car.Run()
car.RunBy("왼쪽")
car.RunBy("오른쪽")

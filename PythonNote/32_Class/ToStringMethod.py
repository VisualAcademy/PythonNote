# __str__

class My:
    pass

my = My()
print(my)

class Your:
    def __str__(self):
        return "새로운 문자열로 개체의 값을 반환"

your = Your()
print(your)

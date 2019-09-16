# 익명 형식(Anonymous Type): 이름이 없는 클래스

class AnonymousType(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__

hong = AnonymousType(name = "홍길동", age = 21)
print(hong)

if hong.age > 19:
    print("{0}은/는 성인이군요.".format(hong.name))
else: 
    print("{0}은/는 학생이군요.".format(hong.name))

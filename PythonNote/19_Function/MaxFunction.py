# Max 함수: 두 수 중에서 큰 수를 반환해주는 함수
def Max(x, y):
    if x > y:
        return x
    else:
        return y

def Min(x, y):
    if x < y:
        return x
    else:
        return y

print(Max(3, 5)) # 5
print(Max(-3, -5)) # -3
print(Min(3, 5)) # 3
print(Min(-3, -5)) # -5

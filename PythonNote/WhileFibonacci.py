# 피보나치 수열: 1 1 2 3 5 8 13 21 ...
a = 0
b = 1

while b <= 20:
    print(b)
    r = a + b
    a = b
    b = r


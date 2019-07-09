# 피보나치 수열 
def fibonacci():
    current, next = 1, 1
    yield current
    
    while True:
        current, next = next, current + next
        yield current

count = 10
i = 0
for f in fibonacci():
    print(f)
    i = i + 1
    if i > count:
        break

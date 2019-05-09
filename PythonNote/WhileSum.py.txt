# while문을 사용해 1~100까지 합

# Input
sum = 0
i = 1

# Process: Sum
while i <= 100:
    sum = sum + i
    i = i + 1    

# Output
print("1~100 합:", sum) # 5050


# 1~100까지 3의 배수 또는 4의 배수의 합
sum = 0
i = 1
while i <= 100:
    if (i % 3 == 0) or (i % 4 == 0):
        sum += i
    i += 1
print("1~100까지 3의 배수 또는 4의 배수의 합:", sum)


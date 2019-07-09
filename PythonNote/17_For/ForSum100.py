# for문을 사용하여 합계 구하기

# 1~100

# Input
sum = 0

# Process : 합계
for i in range(1, 100+1):
    sum = sum + i

# Output
print("1~100까지 합: ", sum)


# 1~100까지 짝수의 합
sum = 0
for i in range(1, 101):
    if i % 2 == 0:          # 필터링: 짝수
        sum = sum + i
print("1~100까지 짝수의 합: ", sum)


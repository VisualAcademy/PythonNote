N = 5

# 나선형으로 값을 채울 2차원 배열 초기화
arr = [[0] * N for _ in range(N)]

num = 1

# 위쪽, 아래쪽, 왼쪽, 오른쪽 경계
top, bottom = 0, N - 1
left, right = 0, N - 1

# 나선형으로 배열 채우기
while top <= bottom and left <= right:  # 나선형으로 덮지 않은 영역이 남아 있는 동안 반복

    # → 오른쪽으로 채우기
    for i in range(left, right + 1):
        arr[top][i] = num
        num += 1
    top += 1

    # ↓ 아래쪽으로 채우기
    for i in range(top, bottom + 1):
        arr[i][right] = num
        num += 1
    right -= 1

    # ← 왼쪽으로 채우기
    for i in range(right, left - 1, -1):
        arr[bottom][i] = num
        num += 1
    bottom -= 1

    # ↑ 위쪽으로 채우기
    for i in range(bottom, top - 1, -1):
        arr[i][left] = num
        num += 1
    left += 1

# 결과 출력
for row in arr:
    print(" ".join(f"{n:3}" for n in row))
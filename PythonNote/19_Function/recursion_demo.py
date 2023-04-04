# 재귀 함수(Recursion)를 사용한 팩토리얼 계산

# 3항 연산자를 사용한 팩토리얼 구하기
def fact(n):
    return n * fact(n - 1) if n > 1 else 1

# 재귀 함수를 사용한 팩토리얼 함수 만들기: 단, 재귀함수는 Tree 구조 탐색에 유리
def factorial(n):
    # 종료
    if n == 0 or n == 1:
        return 1
    # 재귀 호출
    return n * factorial(n - 1)

# 단순한 팩토리얼은 이 방법이 좋음
def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # ((((1 * 1) * 2) * 3) * 4)
    return result

# 재귀 호출을 사용하여 Factorial을 구하기: 4! = 4 * 3 * 2 * 1 = 24
print(4 * 3 * 2 * 1)  # 24
print(factorial_for(4))
print(factorial(4))
print(fact(4))

# 37.3. ParamsDemo.py
# 가변 길이 매개 변수를 갖는 함수 만들기
# => sum_all() 함수는 정수 형식의 값을 가변 형식으로 받을 수 있음
def sum_all(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

# 가변 길이 매개 변수를 갖는 함수 호출하기 
sum_all(3, 5) # 8
sum_all(3, 5, 7) # 15
sum_all(3, 5, 7, 9) # 24

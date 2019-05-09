print("예외 처리")

try:
    number = 3 / 0
except Exception as error:
    print("에러가 발생했습니다.")
    print(error)

print("정상 종료됩니다.")

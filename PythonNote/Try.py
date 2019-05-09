# 비정상 종료
# test = 1234 + "안녕하세요."

# 정상 종료
try:
    test = 1234 + "안녕하세요."
except Exception as err:
    print("에러가 발생했습니다.")
    print(err)

print("프로그램을 종료합니다.")


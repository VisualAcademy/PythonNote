# 문자열 관련 주요 함수

message = "Hello World"

message = 'Hello World'

message = """helloworld"""

print(message)

print(message.capitalize()) # Helloworld

print(message.isalpha()) # helloworld -> True, hello world -> False

print("123".isdigit()) # True

print(message.replace("hello", "안녕하세요.").replace("world", " 세계."))


print(1234 + 1234) # 숫자 더하기 -> 2468

print(str(1234) + str(1234)) # 문자열 더하기 -> 12341234

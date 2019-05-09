# 텍스트 파일 읽어오기
f = open("data.txt", "r", encoding="UTF8")

for line in f.readlines():
    print(line, end='')

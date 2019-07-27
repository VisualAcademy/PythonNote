print("텍스트 파일의 내용 읽어서 출력하기")

f = open("abc1229.txt", "r")

for t in f.readlines():
    print(t)

f.close()

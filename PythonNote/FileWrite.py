# 파일 저장
f = open("data.txt", "a")
f.write("Hello\n")
f.close()

# 파일 읽기
r = open("data.txt", "r")
for d in r.readlines():
    print(d)
r.close()




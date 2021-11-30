# 파일 저장: 같은 경로 또는 프로젝트 경로에 data.txt 파일 생성
f = open("data.txt", "a") # a => append
f.write("Hello\n")
f.close()

# 파일 읽기
r = open("data.txt", "r")
for d in r.readlines():
    print(d)
r.close()

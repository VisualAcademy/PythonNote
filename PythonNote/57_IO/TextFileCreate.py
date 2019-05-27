# 텍스트 파일 생성 및 줄 입력 
f = open("TextFileCreate.txt", "w+") # 생성 및 덮어쓰기 Write Plus
f = open("TextFileCreate.txt", "a") # 생성 및 하단에 추가하기 Append

for i in range(5):
    f.write("줄 " + str(i) + "\n")

f.close()

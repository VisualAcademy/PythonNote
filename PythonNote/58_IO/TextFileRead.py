# 텍스트 파일 생성 및 줄 입력 
f = open("TextFileCreate.txt", "r") # Read 읽기모드

if f.mode == 'r':
    #data = f.read() # 전체 읽어서 출력
    #print(data)

    datas = f.readlines() # 한 줄씩 읽어서 출력
    for d in datas:
        print(d)

f.close()

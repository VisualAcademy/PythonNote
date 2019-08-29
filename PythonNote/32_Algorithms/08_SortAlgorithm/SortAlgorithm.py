#[?] 무작위 데이터를 순서대로 [오름차순(ASC)|내림차순(DESC)] 정렬 

# 정렬 알고리즘(Sort Algorithm): 가장 [작은|큰] 데이터를 왼쪽으로 순서대로 이동
def main():
    #[1] Input: Data Structure(Array, List, Stack, Queue, Tree, DB, ...)
    data = [ 3, 2, 1, 5, 4 ] # 정렬되지 않은 데이터 
    N = len(data) # 의사코드(슈도코드) 형태로 알고리즘을 표현하기 위함
    # print(data)

    #[2] Process: Selection Sort(선택 정렬) 알고리즘
    for i in range(0, N - 1): # i = 0 to N - 1
        for j in range(i + 1, N): # j = i + 1 to N 
            if data[i] > data[j]: # 부등호 방향: 오름차순(>), 내림차순(<)
                temp = data[i]; data[i] = data[j]; data[j] = temp # SWAP
        # print(data)

    #[3] Output: UI(Console, Desktop, Web, Mobile, ...)
    for i in range(N):
        print(data[i]) # print(data)

if __name__ == "__main__":
    main()

#[?] 주어진(지정한 범위) 데이터의 순위(등수)를 구하는 로직

# 순위 알고리즘(Rank Algorithm): 점수 데이터에 대한 순위 구하기 
def main():
    #[1] Input
    scores = [ 90, 87, 100, 95, 80 ] # 등수: 3, 4, 1, 2, 5 
    N = len(scores)
    rankings = [1] * N # 모두 1로 초기화

    #[2] Process: RANK
    for i in range(N):
        rankings[i] = 1 # 1등으로 초기화, 순위 배열을 매 회전마다 1등으로 초기화
        for j in range(N):
            if scores[i] < scores[j]: # 현재(i)와 나머지들(j) 비교
                rankings[i] += 1 # RANK: 나보다 큰 점수가 나오면 순위 1증가

    #[3] Output
    for i in range(N):
        print(f"{scores[i]:3}점: {rankings[i]}등")

if __name__ == "__main__":
    main()

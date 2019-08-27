#[?] 주어진 데이터 중에서 가장 작은 [짝수] 값
import sys

# 최솟값 알고리즘(Min Algorithm): (주어진 범위 + 주어진 조건)의 자료들의 가장 작은 값
def main():
    #[0] Initialize
    min = +sys.maxsize # 숫자 형식의 데이터 중 가장 큰 값으로 초기화

    #[1] Input
    numbers = [ 2, 5, 3, 7, 1 ]; # MIN: 1 -> MIN: 2(짝수)
    N = len(numbers) # 슈도코드

    #[2] Process: MIN
    for i in range(0, N): 
        if numbers[i] < min and numbers[i] % 2 == 0: # 짝수 최솟값
           min = numbers[i] # MIN: 더 작은 값으로 할당 

    #[3] Output
    print(f"짝수 최솟값: {min}")

if __name__ == "__main__":
    main()

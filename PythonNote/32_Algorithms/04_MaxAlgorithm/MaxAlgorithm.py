#[?] 주어진 데이터 중에서 가장 큰 값
import sys

# 최댓값 알고리즘(Max Algorithm): (주어진 범위 + 주어진 조건)의 자료들의 가장 큰 값
def main():
    #[0] Initialize
    max = -sys.maxsize - 1; # 숫자 형식의 데이터 중 가장 작은 값으로 초기화

    #[1] Input
    numbers = [ -2, -5, -3, -7, -1 ] # MAX: -1
    N = len(numbers) # 의사코드

    #[2] Process: MAX
    for i in range(0, N): # 주어진 범위
        if numbers[i] > max: # 더 큰 데이터가 있다면
            max = numbers[i] # MAX: 더 큰 값으로 할당

    #[3] Output
    print(f'최댓값: {max}')

if __name__ == "__main__":
    main()

def find_min(data, n):
    min_value = float('inf')  # 최솟값을 무한대로 초기화

    for i in range(n):
        if data[i] < min_value:
            min_value = data[i]  # 작은 데이터로 재 초기화

    return min_value


def main():
    # [1] Init
    # [2] Input
    data = [-10, -30, -20, -5, -15]
    n = len(data)

    # [3] Process: 최솟값만 구해라!!!
    min_value = find_min(data, n)

    # [4] Output
    print("최솟값:", min_value)  # -30


if __name__ == "__main__":
    main()

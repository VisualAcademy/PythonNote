

def main():
    #[1] Input
    numbers = [3, 2, 1, 5, 4]
    N = len(numbers)

    #[2] Process: Bubble Sort(거품 정렬) 알고리즘
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    #[2] Output
    for i in range(len(numbers)):
        print(numbers[i], end = "\t")
    print()

if __name__ == "__main__":
    main()

#[1] Input
numbers = [3, 2, 1, 5, 4]
N = len(numbers)

#[2] Process: Selection Sort(선택 정렬) 알고리즘
for i in range(N - 1):
    for j in range(i + 1, N):
        if (numbers[i] > numbers[j]):
            temp = numbers[i]
            numbers[j] = numbers[j + 1]
            numbers[j] = temp

#[2] Output
for i in range(len(numbers)):
    print(numbers[i])


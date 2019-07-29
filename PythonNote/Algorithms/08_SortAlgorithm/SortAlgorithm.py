#[1] Input
numbers = [3, 2, 1, 5, 4]

#[2] Process: Selection Sort(선택 정렬) 알고리즘
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] > numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

#[2] Output
for i in range(len(numbers)):
    print(numbers[i])

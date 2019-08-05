#[?] 2개의 정수 배열 합치기: 단, 2개의 배열은 오름차순으로 정렬되어 있다고 가정

# 병합 알고리즘(Merge Algorithm): 오름차순으로 정렬되어 있는 정수 배열을 하나로 병합

#[1] Input
first = [ 1, 3, 5 ] # 오름차순 정렬
second = [ 2, 4 ] # 오름차순 정렬
M = len(first); N = len(second); # M:N 관행
merge = [0] * (M + N) # 병합된 배열 
i = 0; j = 0; k = 0; # i, j, k 관행 

#[2] Process: MERGE
while (i < M and j < N): # 둘 중 하나라도 배열의 끝에 도달할 때까지 
    if first[i] < second[j]: # 작은 값을 merge 배열에 저장 
        merge[k] = first[i]; k += 1; i += 1;
    else: 
        merge[k] = second[j]; k += 1; j += 1;
while (i < M): # 첫 번째 배열이 끝까지 도달할 때까지 
    merge[k] = first[i]; k += 1; i += 1;
while (j < N): # 두 번째 배열이 끝까지 도달할 때까지 
    merge[k] = second[j]; k += 1; j += 1;

#[3] Output
for item in merge:
    print(item, end=", ")
print()

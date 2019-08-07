#[?] 주어진 데이터에서 가장 많이 나타난(중복된) 값

#최빈값 알고리즘(Mode Algorithm): 점수 인덱스(0~n)의 개수(COUNT)의 최댓값(MAX)

import sys

#[1] Input
scores = [ 1, 3, 4, 3, 5 ] # 0~5까지만 들어온다고 가정 
indexes = [0] * (5 + 1) # 0~5까지 점수 인덱스의 개수 저장 
max = -sys.maxsize - 1 # MAX 알고리즘 적용
mode = 0 # 최빈값이 담길 그릇

#[2] Process: Data -> Index -> Count -> Max -> Mode 
for i in range(0, len(scores)):
    indexes[scores[i]] = indexes[scores[i]] + 1 # COUNT
for i in range(0, len(indexes)):
    if indexes[i] > max:
        max = indexes[i] # MAX
        mode = i # MODE

#[3] Output
print(f'최빈값: {mode} -> {max}번 나타남')


data = [ 1, 3, 5, 7, 9]
N = len(data)
search = 3
flag = False
index = -1

low = 0
high = N - 1
while low <= high:
    mid = int((low + high) / 2)
    if data[mid] == search:
        flag = True; index = mid; break;
    if data[mid] > search:
        high = mid - 1
    else:
        low = mid + 1

if flag:
    print(f"{search}를 {index}위치에서 찾았습니다.")
else:
    print("찾지 못했습니다.")

# 리스트(배열, 컬렉션)
colors = ["red", "green", "blue"]

print(colors[0])
print(colors[1])
print(colors[2])

print(colors[-1]) # blue
print(colors[-2]) # green
print(colors[-3]) # red

print(len(colors)) # 3

# 범위
print(colors[1:2])
print(colors[1:]) # 1 인덱스 이후로 가져오기

for color in colors:
    print(color)


# 리스트에 값 추가
colors.append("black")
colors.append("white")

print(colors)

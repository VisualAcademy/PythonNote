# 좋아하는 음식
foods = ["짜장면", "짬뽕", "짬짜면"]

print(foods) # ['짜장면', '짬뽕', '짬짜면']

print(len(foods)) # 3

foods.append("라면")

print(foods) # ['짜장면', '짬뽕', '짬짜면', '라면']

foods.insert(0, "곰탕")

print(foods) # ['곰탕', '짜장면', '짬뽕', '짬짜면', '라면']

del(foods[3])

print(foods) # ['곰탕', '짜장면', '짬뽕', '라면']


# 사람을 나타내는 클래스
class Person:
    def __init__(self, id, name, age):
        self.id = id  # 사람의 id
        self.name = name  # 사람의 이름
        self.age = age  # 사람의 나이

# 사람들을 나타내는 리스트
people = [
    Person(1, "홍길동", 20),
    Person(2, "백두산", 25),
    Person(3, "임꺽정", 30),
    Person(4, "한라산", 28)
]

print("정렬되지 않은 사람들:")
for person in people:
    print(f"{person.id}: {person.name}, {person.age}")

# 나이를 기준으로 사람들을 정렬
people.sort(key=lambda person: person.age)

print("나이별로 정렬된 사람들:")
for person in people:
    print(f"{person.id}: {person.name}, {person.age}")
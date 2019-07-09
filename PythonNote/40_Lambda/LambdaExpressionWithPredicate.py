# 람다식: predicate
def find_numbers(predicate):
    for i in range(1, 100):
        if predicate(i):
            yield i

numbers = find_numbers(lambda n : n % 33 == 0)

for n in numbers:
    print(n, end=', ')

print()

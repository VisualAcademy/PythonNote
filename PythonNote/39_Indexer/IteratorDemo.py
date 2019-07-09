# 이터레이터

class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price):
        self.items.append((name, price))

    def __iter__(self):
        return self.items.__iter__()

cart = Cart()
cart.add('TV', 1000)
cart.add('Video', 2000)

for item in cart:
    print(item)

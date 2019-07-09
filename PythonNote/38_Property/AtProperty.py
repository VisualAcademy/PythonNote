# 속성(Property)

class Product:
    def get_price1(self):
        return 1234

    @property
    def get_price2(self):
        return 1234

product = Product()
print("가격: {0:,}".format(product.get_price1())) # 메서드
print("가격: {0:,}".format(product.get_price2)) # 속성


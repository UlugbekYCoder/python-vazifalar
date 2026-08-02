class Management:

    products = []

    @classmethod
    def add_product(cls, product):
        cls.products.append(product)


class Product:

    def __init__(self, name, price, year, product_type):
        self.name = name
        self.price = price
        self.year = year
        self.product_type = product_type


class User:

    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)

    def get_total(self):
        total = 0

        for product in self.cart:
            total += product.price

        return total

    def clear_cart(self):
        self.cart.clear()
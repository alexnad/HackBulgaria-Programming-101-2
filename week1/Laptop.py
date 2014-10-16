class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, ram, hdd):
        super().__init__(name, stock_price, final_price)
        self.ram = ram
        self.hdd = hdd


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display, pixels):
        super().__init__(name, stock_price, final_price)
        self.display = display
        self.pixels = pixels


class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}
        self.income = 0

    def load_new_products(self, product, amount):
        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount

    def list_products(self, product_type):
        for product in self.products:
            if isinstance(product, product_type):
                print("{0} - {1}".format(product.name, self.products[product]))

    def sell_product(self, product):
        if product in self.products and self.products[product] > 0:
            self.products[product] -= 1
            self.income += product.profit()
            return True
        return False

    def total_income(self):
        return self.income


def main():
    store = Store('Laptop.bg')
    smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    store.load_new_products(smarthphone, 2)
    store.sell_product(smarthphone)
    store.list_products(Laptop)
    store.list_products(Smartphone)
    print(store.total_income())

if __name__ == "__main__":
    main()

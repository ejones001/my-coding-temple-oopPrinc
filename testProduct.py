# Task 4
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product_info(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)


class Book(Product):
    def __init__(self, product_id, name, price, author, genre):
        super().__init__(product_id, name, price)
        self.author = author
        self.genre = genre

    def display_product_info(self):
        super().display_product_info()
        print("Author:", self.author)
        print("Genre:", self.genre)


class Electronic(Product):
    def __init__(self, product_id, name, price, brand, specs):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.specs = specs

    def display_product_info(self):
        super().display_product_info()
        print("Brand:", self.brand)
        print("Specs:", self.specs)


class Clothing(Product):
    def __init__(self, product_id, name, price, size, color):
        super().__init__(product_id, name, price)
        self.size = size
        self.color = color

    def display_product_info(self):
        super().display_product_info()
        print("Size:", self.size)
        print("Color:", self.color)


# Instantiate objects of each subclass
book = Book("B001", "Python Programming", 39.99, "Guido van Rossum", "Programming")
electronic = Electronic("E001", "Smartphone", 599.99, "Samsung", "6.7-inch display, 8GB RAM")
clothing = Clothing("C001", "T-shirt", 19.99, "M", "Blue")

# Call display methods to ensure correct information is shown
book.display_product_info()
print("\n")
electronic.display_product_info()
print("\n")
clothing.display_product_info()

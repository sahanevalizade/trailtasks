class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
    def display_info(self):
        print(f"Mehsul: {self.name}")
        print(f"Qiymet: {self.price} AZN")
        print(f"Miqdar: {self.quantity}")
        print(f"Umumi deyer: {self.total_value()}AZN")


# Sinif test etmek ucun numune:
p1 = Product("Qelem", 0.5, 100)
p1.display_info()

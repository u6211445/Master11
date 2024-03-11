class Shoe:
    def __init__(self, brand, model, size, price):
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price

    def display(self):
        return f"{self.brand} {self.model} {self.size} {self.price}"


class TennisShoe(Shoe):
    def __init__(self, brand, model, size, price, court):
        super().__init__(brand, model, size, price)
        self.court = court

    def display(self):
        return f"{self.brand} {self.model} {self.size} {self.court} {self.price}"

shoe = Shoe("Addidas", "YeeZy ", 9.5, 300)
tennis_shoe = TennisShoe("Adidas", "JaneDoe", 9.5, 105, "OffWhite")
def run():
    print(shoe.display())
    print(tennis_shoe.display())

if __name__ == '__main__':
    run()

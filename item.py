class Item:
    def __init__(self, chest, item):
        self.chest = chest
        self.item = item

    def __repr__(self):
        return f"<chest:{self.chest} item:{self.item}>"

    def __str__(self):
        return f"From str method of Test: a is {self.a}, b is {self.b}"
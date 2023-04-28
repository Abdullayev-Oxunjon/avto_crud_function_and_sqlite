from uuid import uuid4


class Avto:

    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.id = uuid4()

    def __str__(self):
        return f"""

        Id : {self.id}
        Make : {self.make}
        Model : {self.model}
        Color : {self.color}
        Price : {self.price}


        """
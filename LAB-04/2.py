# Decorator/alldecorators/CoffeeShop.py
# Coffee example using decorators

class ComponentePizza:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost

class Chapa(ComponentePizza):
    cost = 0.0

class Decorator(ComponentePizza):
    def __init__(self, componentepizza):
        self.component = componentepizza
    
    def getTotalCost(self):
        return self.component.getTotalCost() + ComponentePizza.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ‘ ‘+ComponentePizza.getDescription(self)

class 4Queijos(Decorator):
    cost = 0.75
    def __init__(self, componentepizza):
        Decorator.__init__(self, componentepizza)

class Calabresa(Decorator):
    cost = 0.0
    def __init__(self, componentepizza):
        Decorator.__init__(self, componentepizza)

class Mussarela(Decorator):
    cost = 0.25
    def __init__(self, componentepizza):
        Decorator.__init__(self, componentepizza)

class Pepperoni(Decorator):
    cost = 0.25
    def __init__(self, componentepizza):
        Decorator.__init__(self, componentepizza)

class Frango(Decorator):
    cost = 0.25
    def __init__(self, componentepizza):
        Decorator.__init__(self, componentepizza)

class Chocolate(Decorator):
    cost = 0.25
    def __init__(self, componentepizza):
        Decorator.__init__(self, componentepizza)

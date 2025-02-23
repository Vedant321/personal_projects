# This is a creational pattern
class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)
    

class BurgerFactory:

    def createCheeseBurger(self):
        ingredients = ['bun', 'cheese', 'beef-patty']
        return Burger(ingredients)

    def createDeluxCheeseBurger(self):
        ingredients = ['bun', 'cheese', 'beef-patty', 'tamatos', 'lettuce']
        return Burger(ingredients)

    def createVeganCheeseBurger(self):
        ingredients = ['bun', 'special-sauce', 'veg-patty']
        return Burger(ingredients)

burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxCheeseBurger().print()
burgerFactory.createVeganCheeseBurger().print()
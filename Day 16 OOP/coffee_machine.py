class MenuItem:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients
class Menu:
    @staticmethod
    def get_item():
        pass

    @staticmethod
    def find_drink(order_name):
        pass

class Coffeemaker:
    @staticmethod
    def report():
        pass

    @staticmethod
    def is_resource_sufficient(drink):
        pass

    @staticmethod
    def make_coffee(order):
        pass

class MoneyMachine:
    @staticmethod
    def report():
        pass

    @staticmethod
    def make_payment(cost):
        pass




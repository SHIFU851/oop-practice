from shop import *
from colorama import Fore

class shop:
    def __init__(self, egg, milk, meat, cola, cheese):
        self.egg = egg
        self.milk = milk
        self.meat = meat
        self.cola = cola
        self.cheese = cheese
    def __str__(self):
        return (f"egg: {self.egg}"
                f"milk: {self.milk}"
                f"meat: {self.meat}"
                f"cola: {self.cola}"
                f"cheese: {self.cheese} ")

    shop_items = {'egg': 10,
                  'milk': 15,
                  'meat': 20,
                  'cola': 5,
                  'cheese': 10}

    balance = int(input(Fore.LIGHTCYAN_EX + "enter you're balance: "))
    market()










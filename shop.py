import colorama
from colorama import Fore

shop_items = {'egg': 10,
              'milk': 15,
              'meat': 20,
              'cola': 5,
              'cheese': 10}

colorama.init(autoreset=True)

balance = int(input(Fore.LIGHTCYAN_EX + "enter your balance: "))

def market():
    print("welcome to our shop!".title())

market()

while True:
    print(Fore.LIGHTWHITE_EX + '----------------------------------------------------')
    print(Fore.LIGHTCYAN_EX + f"Your Balance is: {balance}$")

    user_items = input("what do you want to buy?").lower()

    if user_items not in shop_items:
        print(Fore.LIGHTRED_EX + 'we cant find this item please try again!'.title())
        continue

    item_price = shop_items[user_items]

    if item_price > balance:
        print(Fore.LIGHTCYAN_EX + f"You don't have enough balance to buy {user_items}.")
        continue

    balance -= item_price
    print(Fore.LIGHTWHITE_EX + f"You bought {user_items}. Your Balance Now is: {balance}$")

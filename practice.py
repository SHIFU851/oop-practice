shop_items = {'egg': 10, 'milk': 15, 'meat': 20}
user_items = input("what do you want to buy?").lower()
item_price = shop_items[user_items]
print(item_price)

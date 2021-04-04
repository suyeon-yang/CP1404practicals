list_of_prices = []
items = int(input("Number of items: "))

while True:
    if items > 0:
        for i in range(items):
            price = float(input("Price of item: "))
            list_of_prices.append(price)
        print('Total price for', items, 'item(s) is: ', sum(list_of_prices))
        break
    else:
        print('invalid')
        items = int(input("Number of items: "))

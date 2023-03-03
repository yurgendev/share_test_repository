def shop(**dic):
    return sale_script


sale_script = {
    "igrushka1": [10200, 100],
    "igrushka2": [10300, 200],
    "igrushka3": [20300, 500]
}

print(shop(**sale_script))


def max_price_func():
    max_price = 0
    for item, price in sale_script.items():
        if price[1] > max_price:
            max_price = price[1]
    return item, price


print(max_price_func())


import os

print(os.getcwd())

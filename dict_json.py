import json

order = {"name": "Маша", "form": "круг", "flavor": "орех", "topping": "сахарная пудра"}

order1 = {
    "name": "Алекс",
    "form": "звездочка",
    "flavor": "шоколад",
    "topping": "сахарная пудра",
}

orders = []

orders.append(order)
orders.append(order1)

f = open("orders.json", "w", encoding='utf-8')
json.dump(orders, f, indent=4, ensure_ascii=False)
f.close()

saved_orders = []
f = open("orders.json", "r", encoding='utf-8')
saved_orders = json.load(f)
print(saved_orders)
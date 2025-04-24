import json
import os


def main_menu(orders):
    while True:
        order = get_order()
        if order == {}:
            print("Вы ввели X, это значит, увидимся позже.")
            return
        print("Проверьтие ваз заказ")
        print_order(order)
        confirm = input("Все верно? Тогда нажмите Y, если да, либо N: ")
        if confirm == "Y" or confirm == "y":
            orders.append(order)
            print("Спасибо за ваш заказ!")
            print_order(order)
        else:
            continue


def menu(choices, title="Меню магазина 'Самые вкусные печеньки'", prompt="Выберите вариант: "):
    print(len(title) * "-")
    print(title)
    i = 1
    for c in choices:
        print(i, c)
        i += 1
    while True:
        choice = input(prompt)
        allowed_answers = []
        for a in range(1, len(choices) + 1):
            allowed_answers.append(str(a))

        allowed_answers.append("X")
        allowed_answers.append("x")

        if choice in allowed_answers:
            if choice == "X" or choice == "x":
                answer = ""
                break
            else:
                answer = choices[int(choice) - 1]
                break
        else:
            print("Введите номер от 1 до", len(choices), "или", '"X"', "для выхода")
            answer = ""
    return answer


def read_menu(filename):
    with open(filename, "r", encoding="utf-8") as f:
        temp = f.readlines()
    result = []
    for item in temp:
        new_item = item.strip()
        result.append(new_item)
    return result


def get_order():
    order = {}
    name = input("Введите ваше имя или X для выхода: ")
    if name == "X" or name == "x":
        return {}
    else:
        order["name"] = name
    forms = read_menu("forms.txt")
    flavors = read_menu("flavors.txt")
    toppings = read_menu("toppings.txt")
    order["form"] = menu(forms, "Формы наших печенек: ", "Выберите форму печеньки: ")
    order["flavor"] = menu(flavors, "Вкусы наших печенек: ", "Выберите вкус печеньки: ")
    order["topping"] = menu(toppings, "Обсыпки наших печенек: ", "Выберите обсыпку печеньки: ")
    return order


def print_order(order):
    print("Итак,", order["name"] + ",", "вы выбрали самую вкусную печеньку!")
    print("Форма вашей печеньки: ", order["form"])
    print("Вкус вашей печеньки: ", order["flavor"])
    print("Обсыка вашей печеньки: ", order["topping"])
    print("Мы уже готовим ее для вас!")
    return


def save_orders(orders, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(orders, f, indent=4, ensure_ascii=False)

def load_orders(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            orders = json.load(f)
        return orders
    else:
        return []



orders = load_orders("orders.json")
main_menu(orders)
save_orders(orders, "orders.json")
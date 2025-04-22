def menu(choices, title="Меню магазина 'Самые вкусные печеньки'", prompt="Выберите вариант: "):
    print(len(title) * '-')
    print(title)
    i = 1
    for c in choices:
        print(i, c)
        i = i + 1
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

forms = ["круг", "квадрат", "звездочка"]
flavors = ["шоколад", "ваниль", "орех", "клубника", "малина"]
toppings = ["шоколадная глазурь", "сахарная пудра", "ореховая обсыпка"]
form = menu(forms)
flavor = menu(flavors)
topping = menu(toppings)

print(f"Итак, мы уже начали готовить для вас самую вкусную печеньку: форма: {form} со вкусом {flavor} и {topping}")

print("Спасибо, что выбрали нас!")

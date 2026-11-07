price = input("Введите цену 1 кг конфет: ")

while type(price) != float:
    try:
        price = float(price)
    except ValueError:
        print("Неправильно ввели!")
        price = input("Введите цену 1 кг конфет: ")

weight = 1.2

while weight <= 2:
    print("Вес:", weight, "кг")
    print("Стоимость:", round(price * weight))
    weight = round(weight + 0.2, 1)
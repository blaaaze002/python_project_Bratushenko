a = input("Введите первое число - ")
b = input("Введите первое число - ")

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите целое число A: ")

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите целое число B: ")

if a > 0 or b >-2:
    print("Высказывание истинно")
else:
    print("Высказывание ложно")
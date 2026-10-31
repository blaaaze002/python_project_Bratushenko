while True:
    try:
        num = int(input("Введите трёхзначное число: "))

        if num < 106 or num > 414:
            print("Неверное число")
            continue

        masts = ["пик", "треф", "бубен", "червей"]
        cards = {
            6: "шестёрка",
            7: "семёрка",
            8: "восьмёрка",
            9: "девятка",
            10: "десятка",
            11: "валет",
            12: "дама",
            13: "король",
            14: "туз"
        }

        mast = num // 100
        card = num % 100

        if mast < 1 or mast > 4 or card < 6 or card > 14:
            print("Такой карты нет")
            continue

        print(cards[card], masts[mast - 1])
        break

    except ValueError:
        print("Введите целое число!")
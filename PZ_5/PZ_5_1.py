#С помощью функций получить вертикальную и горизонтальную линии. Линия проводится многократной печатью символа. Заключить слово в рамку из полученных линий.#
def horizont(length):
    print(symb * length)


def vertical(height , width):
    for i in range(height):
        print(symb + " " * width + symb)


def centr_word(word):
    width = len(word) + 2

    horizont(width + 2)
    print(symb + " " + word + " " + symb)
    horizont(width + 2)

symb = input("Введите символ")
centr_word("Python")
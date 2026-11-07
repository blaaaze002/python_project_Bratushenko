n = input("Введите целое положительное число: ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите число: ")

while n <= 0:
    print("Число должно быть больше нуля!")
    n = input("Введите число: ")

count = 0
total = 0

while n > 0:
    digit = n % 10
    total += digit
    count += 1
    n = n // 10

print("Количество цифр:", count)
print("Сумма цифр:", total)
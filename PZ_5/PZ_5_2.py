def DigitCountSum(K):
    C = 0
    S = 0

    while K > 0:
        digit = K % 10
        S += digit
        C +=  1
        K //= 10
    return S,C

for i in range(5):
    K = int(input("Введите целое число: "))

    C, S = DigitCountSum(K)

    print("Количество цифр:",  C)
    print("Сумма цифр:",  S)
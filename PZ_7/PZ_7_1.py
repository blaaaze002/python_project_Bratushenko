# "Вывести N последних строчных (маленьких) букв латинского алфавитав обратном порядке, начиная с буквы «z»."

n = int(input("Введите число - "))
alph = "abcdefghijklmnopqrstuvwxyz"
res = alph[-1:-n-1:-1]
print(res)

s = (input("Введите строку - "))
k = int(input("Введите число - "))

lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
upper = lower.upper()
res = ""
for c in s:
    if c in lower:
        i = lower.index(c)
        res += lower[(i + k) % 32]
    elif c in upper:
        i = upper.index(c)
        res += upper[(i + k) % 32]
    else:
        res += c
print(res)
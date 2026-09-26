V1 = int(input("введите скорость 1 автомобиля - "))
V2 = int(input("ВВедите скорость 2 автомобиля - "))
S = int(input("Введитие начальное рассотяние - "))
T = int(input("Введите время - "))

sum_dist = T * (V1+V2)
put = abs(S - sum_dist)

print(f"В пути {T}ч")
print(f"осталось проехать -  {put}км")

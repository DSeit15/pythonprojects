# Ввод трехзначного числа
number = input("Введите трехзначное число: ")

# Получение цифр числа
a, b, c = number

# Вывод перестановок
print(f"{a}{b}{c}")
print(f"{a}{c}{b}")
print(f"{b}{a}{c}")
print(f"{b}{c}{a}")
print(f"{c}{a}{b}")
print(f"{c}{b}{a}")

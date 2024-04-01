# Ввод четырехзначного числа
number = int(input("Введите четырехзначное число: "))

# Разбиваем число на цифры
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

# Вывод результатов
print("Цифры четырехзначного числа:")
print("Тысячи:", thousands)
print("Сотни:", hundreds)
print("Десятки:", tens)
print("Единицы:", units)
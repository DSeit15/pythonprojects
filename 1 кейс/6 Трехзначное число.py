# Ввод трехзначного числа
number = int(input("Введите трехзначное число: "))

# Разбиваем число на цифры
digit1 = number // 100  # первая цифра
digit2 = (number // 10) % 10  # вторая цифра
digit3 = number % 10  # третья цифра

# Вычисляем сумму и произведение цифр
sum_digits = digit1 + digit2 + digit3
product_digits = digit1 * digit2 * digit3

# Вывод результата
print("Сумма цифр:", sum_digits)
print("Произведение цифр:", product_digits)
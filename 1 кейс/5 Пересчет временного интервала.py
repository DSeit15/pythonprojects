# Ввод количества минут
minutes = int(input("Введите количество минут: "))

# Вычисление часов и минут
hours = minutes // 60
remaining_minutes = minutes % 60

# Вывод результата
print("Временной интервал равен:", hours, "часов и", remaining_minutes, "минут")
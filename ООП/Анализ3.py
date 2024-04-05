from random import randint

class Person:
    count = 0
    
    def __init__(self, c):
        self.id = Person.count
        Person.count += 1
        self.command = c

class Hero(Person):
    def __init__(self, c):
        super().__init__(c)
        self.level = 1
        
    def up_level(self):
        self.level += 1

class Soldier(Person):
    def __init__(self, c):
        super().__init__(c)
        
    def follow(self, hero):
        self.my_hero = hero.id

# Создание героев
h1 = Hero(1)  # первый герой
h2 = Hero(2)  # второй герой

# Создание армий
army1 = []  # первая армия
army2 = []  # вторая армия

# Наполнение армий солдатами
for i in range(20):
    n = randint(1, 2)
    if n == 1:
        army1.append(Soldier(n))  # добавление солдата в первую армию
    else:
        army2.append(Soldier(n))  # добавление солдата во вторую армию

# Вывод численности армий
print(len(army1), len(army2))

# Повышение уровня героя для команды с большей численностью
if len(army1) > len(army2):
    h1.up_level()
elif len(army1) < len(army2):
    h2.up_level()

# Первому солдату первой армии следовать за 1 героем
if army1:  # Добавлена проверка на наличие солдат в армии перед доступом
    army1[0].follow(h1)
    print(army1[0].id, h1.id)  # Вывод ID первого солдата и первого героя
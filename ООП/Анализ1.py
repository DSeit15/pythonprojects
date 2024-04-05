class Student:
    # Конструктор класса с инициализацией атрибутов экземпляра
    def __init__(self, full_name="", group_number=0, progress=[]): 
        self.full_name = full_name # Имя студента
        self.group_number = group_number # Номер группы студента
        self.progress = progress # Список оценок студента

    # Метод для генерации строкового представления объекта
    def __str__(self):
        txt = 'Студент: ' + self.full_name + ' Группа: ' + str(self.group_number)
        txt += ' Оценки:'
        for x in self.progress:
            txt += ' ' + str(x)  # Преобразование оценок в текстовую строку
        return txt

# Функция для определения ключа сортировки по полному имени студента
def SortParam(st):
    return st.full_name

# Количество студентов для ввода
st_size = 5  

students = []  # Создаем пустой список для хранения объектов студентов

# Ввод информации о каждом студенте
for i in range(st_size):
    print("Введите полное имя студента: ")
    full_name = input()
    print("Введите номер группы: ")
    group_number = input()
    n = 5
    print('Введите ', n, ' оценок в столбик: ')
    progress = []
    for i in range(n):  
        score = int(input())  # Ввод оценки студента
        progress.append(score)  # Добавление оценки в список
    st = Student(full_name, group_number, progress)  # Создание экземпляра класса Student
    students.append(st)  # Добавление экземпляра в список студентов

# Вывод списка студентов
print("Students list:")
for st in students:
    print(st)

# Сортировка списка студентов по полному имени
students = sorted(students, key=SortParam)

# Вывод отсортированного списка студентов
print("Sorted students:")
for st in students:
    print(st)

# Вывод списка студентов, имеющих неудовлетворительные оценки
print("bad students:")
n = 0  # Счетчик студентов с неудовлетворительными оценками
for st in students:
    for val in st.progress:
        if val < 3:  # Проверка на неудовлетворительную оценку
            print(st)  # Вывод информации о студенте
            n += 1
            break
if n == 0:
    print("no matches were found.")

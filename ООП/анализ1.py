class Student:
    def __init__(self, full_name="", group_number=0, progress=[]):  # конструктор
        self.full_name = full_name  # имя
        self.group_number = group_number  # номер группы
        self.progress = progress  # оценки

    def __str__(self):  # печатаемое представление экземпляра класса
        txt = 'Студент: ' + self.full_name + ' Группа: ' + str(self.group_number)  # преобразование числа в строку
        txt += ' Оценки: '
        for x in self.progress:
            txt += ' ' + str(x)  # добавляем список оценок
        return txt

# Функция, определяющая атрибут для сортировки
def SortParam(st):
    return st.full_name
  
st_size = 5  # количество студентов
students = []  # создание пустого списка

for i in range(st_size):  # цикл для ввода st_size студентов
    print("Введите полное имя студента: ")
    full_name = input()  # ввод фамилии
    print("Введите номер группы: ")
    group_number = input()  # ввод группы
    n = 5
    print(f'Введите {n} оценок в столбик: ')  # у каждого студента n оценок

    progress = []
    for i in range(n):
        score = int(input())  # ввод оценок
        progress.append(score)  # добавление оценок

    # создание экземпляра класса Student:
    st = Student(full_name, group_number, progress)
    students.append(st)  # добавление экземпляра в список

print("Students list:")
for st in students:  # вывод полного списка студентов
    print(st)

# сортировка по фамилии, ключ сортировки определяется функцией SortParam:
students = sorted(students, key=SortParam)

print("Sorted students:")
for st in students:  # вывод отсортированного списка
    print(st)

print("bad students:")
n = 0  # счетчик количества неуспевающих
for st in students:  # вывод неуспевающих
    for val in st.progress:
        if val < 3:  # есть плохая оценка
            print(st)  # выводим студента с плохой оценкой
            n += 1
            break

if n == 0:
    print("no matches were found.")

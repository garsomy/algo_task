class Student:

    def __init__(self, name, age, average_mark):
        self.name = name
        self.age = age
        self.average_mark = average_mark

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_average_mark(self):
        return self.average_mark

    def set_average_mark(self, average_mark):
        self.average_mark = average_mark

s = Student('Аня', 20, 4.5)

print('Имя:', s.get_name())
print('Возраст:', s.get_age())
print('Средний балл:', s.get_average_mark())

s.set_name('Александр')
s.set_age(22)
s.set_average_mark(4.2)

print('\nПосле изменения:')
print('Имя:', s.get_name())
print('Возраст:', s.get_age())
print('Средний балл:', s.get_average_mark())
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        try:
            return 2 * (self.length + self.width)
        except TypeError:
            return 'Ошибка: Type Error. Возможны буквы в расчётах'
        except ArithmeticError:
            return 'Ошибка: Arithmetic Error. Арефметическая ошибка'
        except IndexError:
            return 'Ошибка: Index Error'
        except ValueError:
            return 'Ошибка: ValueError. Введено неправильное значение'


r = Rectangle(4, 'wte')

area = r.area()
perimeter = r.perimeter()

print("Площадь:", area)
print("Периметр:", perimeter)
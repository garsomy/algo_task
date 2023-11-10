class Car:
    def __init__(self, brand, model, year, kilometers):
        self.brand = brand
        self.model = model
        self.year = year
        self.kilometers = kilometers

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_kilometers(self, kilometers):
        self.kilometers = kilometers

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_kilometers(self):
        return self.kilometers

c = Car('Supra', 'MkII', 2022, 73675)

print('Марка:', c.get_brand())
print('Модель:', c.get_model())
print('Год производства:', c.get_year())
print('Пробег:', c.get_kilometers())

c.set_brand('Lada')
c.set_model('granta')
c.set_year(2018)
c.set_kilometers(6757356)

print('\nПосле изменения:')
print('Марка :', c.get_brand())
print('Модель:', c.get_model())
print('Год производства:', c.get_year())
print('Пробег:', c.get_kilometers())
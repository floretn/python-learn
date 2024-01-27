class Cat:
    name = None
    age = None
    isHappy = None

    # def __init__(self):
    #     pass

    def __init__(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def set_date(self, name, age, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def to_string(self):
        return f'{self.name} is {self.age} years and ' + ('happy' if self.isHappy else 'unhappy')

cat1 = Cat()
# cat1.name = 'Barsic'
# cat1.age = 3
# cat1.isHappy = True
cat1.set_date('Barsic', 3, True)

# cat2 = Cat()
# cat2.name = 'Jopen'
# cat2.age = 6
# cat2.isHappy = False
cat2 = Cat('Jopen', 6, False)

print(cat1.name)
print(cat2.name)
print(cat1.to_string())
print(cat2.to_string())

class Building:
    __year = None
    def __init__(self, year, city):
        self.year = int(year)
        self.city = city

    def to_string(self):
        return f'Building of {self.year} year in city {self.city}'

class House(Building):
    pass

class School(Building):
    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = int(pupils)

    def to_string(self):
        return f'School of {self.pupils} pupils ' + super().to_string()

class Shop(Building):
    pass

school = School(1000, 2020, "California")
house = House(2023, "Moscow")
shop = Shop(2024, "Archangels")
print(school.to_string())
print(house.to_string())
print(shop.to_string())

#print(school.__year) -- don't work:)))
print(school.year) # work:)))))))))))))))))))))))))))

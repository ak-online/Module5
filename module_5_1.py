
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if new_floor > 0 and new_floor < self.number_of_floors:
            print(f' Квартал:{self.name}, Этаж: {new_floor}, Всего этажей - {self.number_of_floors}.')
        else:
            print(f' Квартал:{self.name}, такого этажа: {new_floor} нет! Всего этажей - {self.number_of_floors}.')


h1 = House('ЖК Горский', 18)
h1.go_to(5)

h2 = House('Домик в деревне', 2)
h2.go_to(10)

h3 = House('ЖК Кремль ', 25)
h3.go_to(-1)

h4 = House('КП "Супер избинг" ', 2)
h4.go_to(5)
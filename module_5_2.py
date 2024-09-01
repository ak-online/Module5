
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # def go_to(self, new_floor):
    #
    #     if new_floor > 0 and new_floor < self.number_of_floors:
    #         print(f' Квартал:{self.name}, Этаж: {new_floor}, Всего этажей - {self.number_of_floors}.')
    #     else:
    #         print(f' Квартал:{self.name}, такого этажа: {new_floor} нет! Всего этажей - {self.number_of_floors}.')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f' Название:{self.name}, кол-во этажей: {self.number_of_floors}.'



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# h1.go_to(5)
# h2.go_to(10)
# h3.go_to(-1)
# h4.go_to(5)

print(str(h1))
print(str(h2))

print(len(h1))
print(len(h2))
class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        # cls.houses_history.insert(0,args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(House.houses_history)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории...')


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Матрёшки', 20)
h4 = House('ЖК АБВ', 11)
h5 = House('ЖК КЛЁПИКИ', 2)

# Удаление объектов
del h2
del h3

print(House.houses_history)
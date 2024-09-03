class House:
    def __init__(self, name, number_of_floors):
       self.name = name
       self.number_of_floors = number_of_floors

    def __len__(self):
         return self.number_of_floors
    def __str__(self):
       title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
       return title

    def __eq__(self, other):    # 1
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):    # 2
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self


hightower = House('Башня', 12)
warehouse = House('Склад', 4)

print(hightower)
print(warehouse)
# 1
print(hightower == warehouse)
# 3
print(warehouse.__add__(8))
print(hightower == warehouse)
# 2
print(hightower < warehouse)
print(hightower <= warehouse)
print(hightower > warehouse)
print(hightower >= warehouse)
print(hightower != warehouse)
# 5
print(hightower.__radd__(7))
print(warehouse.__iadd__('8'))
print(warehouse.__iadd__(8))
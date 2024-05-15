# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
from abc import ABC, abstractmethod
import re

class Person:
    def __init__(self, id, name, is_a_student):
        self.id = id
        self.name = name
        self.is_a_student = is_a_student

    @staticmethod
    def is_valid_name(name):
        pattern = "\\w+ \\w.*"
        if bool(re.match(pattern, name)):
            return True
        return False
    ## match geeft geen bool maar match object waar slecht null is door bool te zetten, zetten we om naar bool.
    
    
    ## Test of het werkt!!! 
    ## print(Person.is_valid_name("Machine "))
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self.is_valid_name(value):
            self._name = value
        else:   
            raise ValueError("Invalid name")
    
    ## in het voorbeeldgebruik gaan ze errors zetten die niet mogen en deze moeten we dan als messages zetten bij de valueerror

## person = Person(1, "Machine", False)

class Residence(ABC):
    
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self._occupants = dict()

    @property
    def number_of_occupants(self):
        return len(self._occupants)

    @property
    def maximum_occupants(self):
        ppa = self.area // 20
        ppr = self.number_of_rooms * 2
        return min(ppa, ppr)
    
    def register_resident(self, person):
        if person in self._occupants:
            return
        if self.number_of_occupants >= self.maximum_occupants:
            raise RuntimeError(" too much man")
        self._occupants[person.id] = person
    ## unregister_resident(id) home

    @abstractmethod
    def calculate_value():
        ...

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity = garage_capacity


    def calculate_value(self):
        return (25000 * self.number_of_rooms) + (2100 * self.area) + (10000 * self.garage_capacity)
    
    ## studentenkot zelf proberen

    
aimee = Person("12.34.56-789.01","Aimee Backiel",False)
bastian = Person("01.02.03-040.05", "Bastian Li Backiel", True)

my_villa = Villa("Roeselbergdal 44, 3012 Wilsele", 151, 4, 1)
print(my_villa.calculate_value())

my_villa.register_resident(aimee)
my_villa.register_resident(bastian)

print(my_villa.number_of_occupants)
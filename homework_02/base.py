from abc import ABC
from homework_02 import exceptions



class Vehicle(ABC):
    def __init__(self,weight,fuel,fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False


    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError('Ошибка с низким расходом топлива')


    "добавьте метод move, который проверяет, " \
    "что топлива достаточно для преодоления переданной дистанции (вплоть до полного расхода), " \
    "и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions.NotEnoughFuel"

    def move(self, distance):
        calculate = self.fuel_consumption * distance
        if self.fuel >= calculate:
             self.fuel -= calculate
        else:
            raise exceptions.NotEnoughFuel()


# ver1
from abc import abstractmethod

class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y

class Calc2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y

    def multiply(self):
        return self.x * self.y

# ver2
class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.calc2 = Calc2(x, y)
    
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.calc2.multiply()

calc1 = Calc(1, 2)
print(calc1.add())
print(calc1.subtract())
print(calc1.multiply())


class Character:
    def __init__(self, name='yourname', health_point=100, striking_power=3, defensive_power=3):
        self.name = name
        self.health_point = health_point
        self.striking_power = striking_power
        self.defensive_power = defensive_power

    def info(self):
        print(self.name, self.health_point, self.striking_power, self.defensive_power)

    @abstractmethod
    def attack(self, second):
        pass

    @abstractmethod
    def receive(self):
        pass


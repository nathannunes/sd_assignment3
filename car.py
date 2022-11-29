from vehicle import Vehicle


class Car(Vehicle):
    _speed = int(0)
    _model = "Toyota"
    _color = "Red"
    numCars = int(0)

    # Multiple constructors not supported in python, this is how we do it
    def __init__(self, s=10, c='White', m='Porsche'):

        self._speed = s
        self._color = c
        self._model = m
        Car.numCars += 1

    def getSpeed(self):
        return int(self._speed)

    def setSpeed(self, s):
        self._speed = s

    def getModel(self):
        return self._model

    def setModel(self, m):
        self._model = m

    def getColor(self):
        return self._color

    def setColor(self, c):
        self._color = c

    def print(self):
        print("speed : ", self.getSpeed(), "\nmodel : ", self.getModel(), "\ncolor : ", self.getColor())

    def decelerate(self):
        print('slowing down')
        self._speed = 0 if (self._speed - 10) <= 0 else (self._speed - 10)

    def accelerate(self):
        if self._speed + 10 >= 80:
            print("speed is ", self._speed,"mph, you are approaching the max. speed limit")
            print("speed capped at 80 mph")
            self._speed = 80
        else:
            print('increasing speed ....')
            self._speed += 10

    def getNumCars(self):
        return Car.numCars

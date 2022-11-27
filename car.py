from vehicle import Vehicle


class Car(Vehicle):
    _speed = int(0)
    _model = "toyota"
    _color = "red"
    numCars = int(0)

    def __int__(self, s=10, c="orange", m="ford"):
        self._speed = s
        self._color = c
        self._model = m
        self.numCars += 1

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
        print("speed : ", self._speed, "\nmodel : ", self._model, "\ncolor : ", self._color)

    def decelerate(self):
        return 0 if (self._speed - 5) <= 0 else (self._speed - 5)

    def accelerate(self):
        if self._speed + 10 >= 350:
            print("speed is ", self._speed, "  mph, you are approaching the max. speed limit\n")
            print("speed capped at 350 mph")
            return 350
        else:
            return self._speed + 10

    def getNumCars(self):
        return self.numCars

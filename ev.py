from car import Car


class EV(Car):
    _range = float(0)
    _gen = 0

    # Python does not allow explicit use of multiple constructors,
    # instead it allows the use of optional parameters as shown below
    def __init__(self, r=100, g=1):
        self._range = float(r)
        self._gen = g
        self.numCars += 1

    def getRange(self):
        return self._range

    def getGen(self):
        return self._gen

    def setRange(self, input_range):
        self._range = input_range

    def setGen(self, input_gen):
        self._gen = input_gen

    def print(self):
        print("range of EV :  ", self._range, "\ngen of EV   :  ", self._gen)
        print("model of EV :  ", self.getModel())

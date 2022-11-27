from car import Car


class EV(Car):
    _range = float(0)
    _gen = 0

    def __int__(self):
        self._range = float(100)
        self._gen = 1

    def __init__(self, r, g):
        self._range = float(r)
        self._gen = g

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

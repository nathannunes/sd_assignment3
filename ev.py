from car import Car


class EV(Car):
    _range = float(0)
    _gen = 0
    _validGen = [1, 2, 3]
    _num_of_ev = int(0)

    # Python does not allow explicit use of multiple constructors,
    # instead it allows the use of optional parameters as shown below
    def __init__(self, r=100, g=3):
        self._range = float(r)
        self._gen = g if g in self._validGen else 3
        self._num_of_ev += 1
        Car.numCars += 1

    def getRange(self):
        return self._range

    def getGen(self):
        return self._gen

    def setRange(self, input_range):
        self._range = input_range

    def setGen(self, input_gen):
        if input_gen in self._validGen:
            self._gen = input_gen
        else:
            print('gen can only be 1,2 or 3. defaulting to 3')
            self._gen = 3

    def getNumEVs(self):
        return self._num_of_ev

    def print(self):
        print("range of EV :  ", self.getRange(), "\ngen of EV   :  ", self.getGen())
        print("model of EV :  ", self.getModel())
        print("speed of EV :  ", self.getSpeed())
        print("color of EV :  ", self.getColor())

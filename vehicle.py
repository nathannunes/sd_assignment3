class Vehicle:
    _class = "Hatch Back"
    _speed = int(0)
    _model = "Lincon"
    _color = "Red"

    def __init__(self, s, m, co):
        self._speed = s
        self._model = m
        self._color = co


    def print(self):
        print("class of vehicle :  ", self._class, "\nspeed : ", self._speed, '\nmodel : ', self._model, '\ncolor : ', self._color)

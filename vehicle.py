class Vehicle:
    _class = "hatch back"

    def __init__(self, t="sedan"):
        self._class = t

    def print(self):
        print("class of vehicle :  ", self._class, "\n")

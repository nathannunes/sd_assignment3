from car import Car
from ev import EV

#Param EV
print("\nparam EV")

# Valid gen values for EV are 1, 2 and 3 , other values are invalid and will default to 3, example below
ev = EV(r=10, g=4)
ev.setModel('Tesla')
ev.setColor('black')
for i in range(3):
    ev.accelerate()
ev.print()
ev.decelerate()
print('\n')
ev.print()

print("\ncar with param")
r = Car(10, 'Mercedes Benz', 'Titanium')
r.setSpeed(60)
print('car speed  : ', r.getSpeed())
r.accelerate()
r.print()


print('total no of Cars : ', r.getNumCars())
print('total no of EVs : ', ev.getNumEVs())

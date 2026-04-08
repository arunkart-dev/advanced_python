class Vehicle:
    def ride(self):
        print("Ride the bike !!")
class Bike(Vehicle):
    def tuo(self):
        print("Book thr bike !!")

b = Bike()
b.ride()
b.tuo()
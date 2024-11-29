class Vehicle:
    def move(self):
        pass
class Bus(Vehicle):
    def move(self):
        print("Electric Bus")

class Yatch(Vehicle):
    def move(self):
        print("Sailing Yatch")
class Plane(Vehicle):
    def move(self):
        print("Flying Plane")

class Bike(Vehicle):
    def move(self):
        print("Riding Bike")

def test_move(means_of_transport):
    for mot in means_of_transport:
        mot.move()

# create a list of different vehicles
mot = [Bus(), Yatch(), Plane(), Bike()]

test_move(mot)

        
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    
    def addpass(self, name):
        if not self.openseats():
            return False
        self.passengers.append(name)
        return True

    def openseats(self):
        print(self.capacity - len(self.passengers))
        return self.capacity - len(self.passengers)


flight = Flight(3)
people = ['Harry', 'Hemione', 'Drazco', 'Mona']
for person in people:
    success = flight.addpass(person)
    if success:
        print(f'{person} added')
    else:
        print('full capacaity')

print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(3))
print(bool(45))
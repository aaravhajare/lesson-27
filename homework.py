class vehical :

    def __init__(self,name,capacity,mileage):
        self.name = name
        self.capacity = capacity
        self.mileage = mileage

    def fare(self):
        return self.capacity * 100
    

class bus(vehical) :
    
    def fare(self) :
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = bus("school bus" , 35 , 12)
print("fare of bus is :" , School_bus.fare()) 
class vehical :

    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

class bus(vehical) :
    pass

School_bus = bus("school bus" , 35 , 12)
print("properties of vehical are :" , School_bus.name , School_bus.speed , School_bus.mileage)
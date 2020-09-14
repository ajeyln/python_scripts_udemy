# Creating a class Mescom
class Mescom(object):
    power_source = "Electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
    
    def switch_on(self):
        self.on = True

kenwood = Mescom("Kenwood", 8.59)
print(kenwood.make)
print(kenwood.price)

hamilton = Mescom("Hamilton", 14.55)
print("Model: {} = {}, {}= {}".format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))
print("Model:{0.make}:{0.price}, {1.make}:{1.price}".format(kenwood,hamilton))
# Class: template for creating objects. All objects created using the same class will have the same characteristics.
# Objects: an instance of a class.
# Instantiate : create an instance of a class.
# Method:a function defined in a class.
# Attribue: a variable bound to an instance of class.

Mescom.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on()

print('*' * 120)

kenwood.power = 1.5
print(kenwood.power)

print('switch to atomic power')
Mescom.power_source = "atomic"
print(Mescom.power_source)
print("switch kennwood to gas")
kenwood.power_souce = "gas"
print(kenwood.power_source)
print(hamilton.power_source)

print(Mescom.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
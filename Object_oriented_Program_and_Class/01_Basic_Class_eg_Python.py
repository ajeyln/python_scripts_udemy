# Creating a class of Kettel
class Kettel:
#Creating method under class
    def __init__(self, make, price): # Initiallization of method where self is object
        self.make = make
        self.price = price
        self.on = False

phillips = Kettel("Phillips", 750)
print(phillips.make)
print(phillips.price)

prestige = Kettel("Prestige", 850)
print("*" * 50)
print("Maker1 : {}, price : {}\nMaker2 : {}, price : {}"
      .format(phillips.make, phillips.price, prestige.make, prestige.price))

# Class: template for creating objects. All objects created using the same class will have the same characteristics.
# Objects: an instance of a class.
# Instantiate : create an instance of a class.
# Method:a function defined in a class.
# Attribue: a variable bound to an instance of class.



# class MyClass:
#     variable = "blah"
#     def function(self):
#         print("This is blah")
        
# myObjectX = MyClass()
# myObjectY = MyClass()

# myObjectY.variable = "This is another blah"

# print(myObjectX.variable)
# print(myObjectY.variable)
# print(myObjectX.function())

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car2 = Vehicle()

car1.color = "red"
car1.name = "Ferrari"
car1.kind = "convertible"
car1.value = 60000.00

car2.color = "blue"
car2.name = "Van"
car2.kind = "Jump"
car2.value = 10000.00
    
print(car1.description())
print(car2.description())
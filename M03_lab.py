#Author: Fleur Mushumba
#date: 02/06/2022
#description: This app asks the user to input the type of vehicle they have and then asks about the details of the vehile. 
# the program will then output the result in an easily readable format
class Vehicle:
    def __init__(self, car_type):
        self.car_type=car_type

class Automobile(Vehicle):
    def __init__(self,car_type):
        Vehicle.__init__(self,car_type)
        self.year=input("Enter year of your vehicle: ")
        self.make=input("Enter the make of your vehicle: ")
        self.model=input("Enter your car model: ")
        self.doors=input("Enter the number of doors on your car: ")
        self.roof=input("Enter the roof type of your car: ")
    def get_car(self): 
        return f"Vehicle type: {self.car_type} \nYear: {self.year} \nMake: {self.make} \nModel: {self.model} \nNumber of doors: {self.doors} \nType of roof: {self.roof}"

c1=Automobile("car")
print(c1.get_car())
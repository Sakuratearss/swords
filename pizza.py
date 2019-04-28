def make_pizza(size,*toppings):
	print("\nMake a"+str(size)+
		  "-inch pizza:")
	for topping in toppings:
		print("-"+topping)
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green pepper','cheese')

class Cat():   #创建类
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def catch(self):
		print(self.name.title()+"is now catching mouse.")
	def flee(self):
		print(self.name.title()+"is runaway before dog catch it!")
my_cat= Cat('miao',6)
your_dog = Cat('wang',3)
print("My cat's name is " + my_cat.name.title()+".")
print("My cat is " + str(my_cat.age) + " years old.")
print("Your dog names "+your_dog.name.title()+ " is " +	 str(your_dog.age) + " old."	)
my_cat.catch()
my_cat.flee()


class Car():
	def __init__(self,make,model,year):
		self.make=make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' +self.make + ' ' + self.model
		return long_name.title()
		def read_odometer(self):
			print("This car has "+str(self.odometer_reading)+"miles on it.")
	def read_odometer(self,mileage):
		if mileage>=self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("Your can't roll back it.")
	def increment_odometer(self,miles):
		self.odometer_reading += miles
class ElectricCar(Car):
	def __init__(self,make,model,year):
		super().__init__(make,model,year)
		self.battery_size = 70
	def describe_battery(self):
		print("This car has a "+ str(self.battery_size)+"-kwh battery.")
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_used_car=Car('subaru','outback',2013)
print(my_used_car.get_descriptive_name())
my_used_car.read_odometer(23500)
my_used_car.increment_odometer(100)
print("My car has "+str(my_used_car.odometer_reading)+" on it")
my_tesla.describe_battery()

from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name,language in favorite_languages.items():
	print(name.title()+"'s favorite language is "+language.title()+".")
		


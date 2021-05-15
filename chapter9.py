class Dog:
	"""A simple attempt to model a dog"""
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")
		
	def roll_over(self):
		"""Simulate rolling over in response to a cmommand."""
		print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


### 9-1
class Restaurant:
	"""docstring for Restaurant"""
	def __init__(self, restaurant_type, cuisine_type):
		"""Initilize restaurant type and cuisine type"""
		self.restaurant_type = restaurant_type
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Describing your type of restaurant"""
		print("This is a classical restaurant. Most prefer this type")

	def open_restaurant(self):
		"""Current status of the restaurant: whether open or not"""
		print("This restaurant is open at all times of the day.")

city_restaurant = Restaurant("classical", "opened")

print(f"\nI prefer to stay in a {city_restaurant.restaurant_type} restaurant_type")
print(f"This restaurant type is {city_restaurant.cuisine_type} at all times\n")
city_restaurant.describe_restaurant()
city_restaurant.open_restaurant()
		
		
### Importing functions and classes
from random import randint
randint(1, 6)
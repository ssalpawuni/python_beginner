with open('pi.txt') as file_object:
	contents = file_object.read()
print(f"{contents}\n")

with open('pi.txt') as file_object:
	for line in file_object:
		print(line.rstrip())

with open('pi.txt') as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	#pi_string += line.rstrip() # rstrip() strips to the right
	pi_string += line.strip() # strips() strips both sides

print(pi_string)
print(len(pi_string))

message = "I love my father"
print(message)
print(message.replace("father", "mother"))

# Birthday in pi
with open('pi.txt') as file_object:
	lines = file_object.readlines()



pi_string = ''
for line in lines:
	pi_string += line.strip() # strips() strips both sides

#birthday = input("Enter your birthday, in the format mmddyy: ")
birthday = ''
if birthday in pi_string:
	print("Your birthday appears in the first 1 million of pi!")
else:
	print("Your birthday does not appear in the first 1 million digits of pi!")

## writing to a file
filename = "programming.txt"
with open(filename, 'w') as file_object:
	file_object.write("Salpawuni loves to progm in Python. How about you?\n")
	file_object.write("I studied R programming first before Python")

# Exception
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

## using json.dump() and json.load()
import json

numbers = [2, 3, 5, 7, 11, 13]

file_name = 'numbers.json'
with open(file_name, 'w') as f:
	json.dump(numbers, f)
with open(file_name) as f:
	numbers_1 = json.load(f)
print(numbers_1)















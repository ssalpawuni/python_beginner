prompt = "If you tell us who you are, we can personalize the message to you."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\n Hello, {name.title()}!")

mom = input("\nPlease enter your mom's name: ")
print(f"\nHello, {mom.title()}!")

age = input("\nHow old are you? ")
age = int(age)
print(f"Your age times 3 is: {3 * age} years")

# Dealing with ##while()## 
prom = "\nTell me something and I will repeat it back to you."
prom += "Enter 'quit' to end the program. "

messg = ""
while messg != "quit":
	messg = input(prom)
	if messg != 'quit':
		print(messg)


prompt = "Please enter your age: "
age = input(prompt)
age = int(age)

while age > 0:
	if age < 3:
		print("\nThe ticket is $0.")
	elif age >= 3 and age <= 12:
		print("\nThe ticket is $10.00")
	elif age >= 12:
		print("\nThe ticket is $15.00")
	else:
		print("\nInvalid entery!")
	age = 0

# alternative to above
age = 0
while age != -1:
	prompt = "Please enter your age: "
	prompt += "\n Enter -1 to quit the programme. "

	age = input(prompt)
	age = int(age)

	if age >= 0 and age < 3:
		print("\nThe ticket costs $0.00")
	elif age >= 3 and age <= 12:
		print("\nThe ticket costs $10.00")
	elif age >= 12:
		print("\nThe ticket costs $15.00")
	else:
		print("Invalid entery")

counter = 0
while counter <= 5:
	counter += counter
	prompt = "Please enter your age: "

	age = input(prompt)
	age = int(age)

	if age >= 0 and age < 3:
		print("The ticket costs $0.00")
	elif age >= 3 and age <= 12:
		print("\nThe ticket costs $10.00")
	elif age >= 12:
		print("\nThe ticket costs $15.00")
	else:
		print("Invalid entery")




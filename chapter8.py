def greet_user(username):
	"""greet user"""
	print(f"Hello, {username.title()}!")
greet_user('Salpawuni')

def get_formatted_name(first_name, last_name):
	"""Return a full name, nicely formatted"""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

muscian = get_formatted_name('jimi', 'hendrix')
print(muscian)

# using a function with a while loop

def greeting_user(first_name, last_name):
	"""Nicely formatting a name"""
	ful_name = f"{first_name} {last_name}"
	return ful_name

# while loop
flag = True
while flag:
	print("\nPlease tell me your name.")
	f_name = input("Enter your first name, please: ")
	l_name = input("Enter your last name, please: ")
	
	ful_name = greeting_user(f_name, l_name)
	print(f"\nHello {ful_name.title()}!")

	choice = input("Do you want to repeat again (yes/no)? ")
	if choice == "no":
		flag = False
	else:
		flag = True

# alternative to while loop above
flag = True
while flag:
	print("\nPlease tell me your name.")
	print("Enter 'q' at anytime to quit.")
	f_name = input("Enter your first name, please: ")
	if f_name == 'q':
		break
	l_name = input("Enter your last name, please: ")
	if l_name == 'q':
		break
	
	ful_name = greeting_user(f_name, l_name)
	print(f"\nHello {ful_name.title()}!")
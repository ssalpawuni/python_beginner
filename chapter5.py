cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# 5-8 (Hello Admin)
usernames = ['sam', 'jerry', 'doobia', 'admin', 'fusey']

for username in usernames:
	if username == 'admin':
		print(f"Hello, {username.title()}! Would you like to see a status report?")
	else:
		print(f"Hello, {username.title()}! Thanks for logging in again.")

# 5-9 (No users)
usernames = []

if usernames:
	for username in usernames:
		if username == 'admin':
			print(f"Hello, {username.title()}! Would you like to see a status report?")
		else:
			print(f"Hello, {username.title()}! Thanks for logging in again.")
else:
	print("We need to find some users.")

# 5-10 (Checking usernames)
current_users = ['sam', 'jerry', 'doobia', 'zack', 'fusey']
new_users = ['alan', 'jerry', 'doobia', 'mike']

for new_user in new_users:
	if new_user in current_users:
		print(f"\nUsername '{new_user}' already exists. Enter a new username.")
	else:
		print(f"\nUsername '{new_user}' is available.")

# 5-11 (Ordinal numbers)
ord_numbers = list(range(1,10))
for ord_number in ord_numbers:
	if ord_number == 1:
		print("1st")
	elif ord_number == 2:
		print("2nd")
	elif ord_number == 3:
		print("3rd")
	else:
		print(f"{ord_number}th")
	












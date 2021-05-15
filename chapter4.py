# Chapter 4
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"When is your next trick coming, {magician.title()}?\n")

print("Thank you for showing up today. That was awesome!")

for value in range(5):
	print(value)

numbers = list(range(2, 11, 2))
print(numbers)

# Squares of the first 10 numbers
squares = []
for value in range(1,11):
	square = value ** 2 # or squares.append(value ** 2)
	squares.append(square)
print(squares)

# multiples of 3
print([3*val for val in range(1, 11)])
# alternative (shortcut)
squares_1 = [value**2 for value in range(1, 11)]
print(squares_1)

print(sum(squares))
print(min(squares))
print(max(squares))

# slicing list via ':' operator
# using the ":" operator makes it easy to copy list
print(squares[0:3])

# creating immutables (called tuple in python)
# tuples are non-destructive, created using ()
dimensions = (200, 250)
print(dimensions)


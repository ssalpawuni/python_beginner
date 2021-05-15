# 3-4 (guest list)
guests = ['azumi', 'tunteiya', 'salpawuni', 'fusey', 'bushra']

for fam in guests:
	print(f"{fam.title()}\n")

print(f"Hello {guests[0].title()}, you are invited to dinner at 6.30pm")
print(f"Hello {guests[1].title()}, you are invited to dinner at 6.30pm")
print(f"Hello {guests[2].title()}, you are invited to dinner at 6.30pm")
print(f"Hello {guests[3].title()}, you are invited to dinner at 6.30pm")

# 3-5 (changing guest list)
guest_cancel = guests.pop(2)
print(f"Unfortunately, {guest_cancel.title()} isn't available for dinner.")

guests.insert(2, "walker")
print(f"Hello {guests[0].title()}, you are invited to dinner at 6.30pm")
print(f"Hello {guests[1].title()}, you are invited to dinner at 6.30pm")
print(f"Hello {guests[2].title()}, you are invited to dinner at 6.30pm")
print(f"Hello {guests[3].title()}, you are invited to dinner at 6.30pm")

# 3-6 (shrinking guest lists)
print(f"Sorry {guests.pop().title()}, I'm unable to invite to dinner.")
print(f"Sorry {guests.pop().title()}, I'm unable to invite to dinner.")
print(f"Sorry {guests.pop().title()}, I'm unable to invite to dinner.")

# 3-7 (empty list)
print(f"{guests[0].title()} and {guests[1].title()} are invited.")

del guests[0]
del guests[0]
print(guests)

alien_0 = {'colors': 'green', 'points': 5}
print(alien_0['colors'])
print(alien_0['points'])
print(alien_0)

favorite_language = {
	'salpawuni' : 'r',
	'victor' : 'python',
	'mike' : 'ruby',
	'sandra' : 'java'
	}
print(favorite_language)

# 6-1
bio_dat = {
		'first_name' : "Salaam",
		'last_name' : "Kareem",
		'country_name' : "Ghana", 
		'town_name' : "Agona"
		}
print(bio_dat)

for name, language in favorite_language.items():
	print(f"\n{name.title()}'s favorite languse is {language.upper()}!")

for language in favorite_language.keys():
	print(f"\n{favorite_language[language].title()} is a popular programming language!")

verbs = {
		'verb_1' : 'pop()',
		'verb_2' : 'get()',
		'verb_3' : 'remove()',
		'verb_4' : 'append()',
		'verb_5' : 'lower()'
		}

for verb in verbs:
	#print(verbs[verb])
	print(verbs.get(verb))

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")









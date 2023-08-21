acronyms = {'LOL': 'Laugh out loud',
            'TBH': "To be honest",
            'IDK': "I don't know"}
# Look up value by using the key as an index of the dictionary.
print("Printing index 'LOL'", acronyms['LOL'], "\n\n")

print('\n---------------------\n')

# Test removal and removal value of dictionary
print('First attempt to get TBH. TBH result: ', acronyms.get('TBH'))
del acronyms['TBH']
result = acronyms.get('TBH')

print('\n---------------------\n')
# None is the absence of a value. Also == false
print('Second attempt to get TBH after deletion. Result: ', result)


print('\n---------------------\n')

print('Third attempt to get TBH with a try/except block: \n')

try:
    definition = acronyms['TBH']
    print("(try) Found acronym:", definition)
except:
    print("(except) Exception handled. The key does not exist. Unable to find:", 'TBH')
finally:
    print('\n(finally) Third attempt complete')

print('\n---------------------\n')

if result:
    print('If None value is true')
elif not result:
    print("If None result value is false. If 'not false' is true.")

if result == None:
    print("If result == None is true.")

# Iterating through the dictionary object

menus = { 'Breakfast' : ['Egg Sandwich', 'Bagel', 'Coffee'],
          'Lunch' : ['BLT', 'PB&J', 'Turkey Sandwich'],
          'Dinner' : ['Soup', 'Salad', 'Spaghetti', 'Taco']}

print(menus['Breakfast'])

# Return just the keys

for item in menus:
    print(item, "\n")

# Return keys and values

for menu, options in menus.items():
    print(menu, ': ', options)
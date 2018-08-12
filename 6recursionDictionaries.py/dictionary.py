my_dict = {}
grades = {'Ana':'B','John':'A+','Denise':'A','Katy':'A'}

# add an entry
grades['Sylvan'] = 'A'

# test if key in dictionary
print('John' in grades)
print('Someone' in grades)

# delete entry
del(grades['Ana'])

# return all keys, not guaranteed order
print(grades.keys())

# return all values, not guaranteed order
print(grades.values())

print('John\'s grade is',grades['John'])
print('john\'s grade is',grades['john'])

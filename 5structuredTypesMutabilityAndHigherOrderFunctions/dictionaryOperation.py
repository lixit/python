d = {1:'one', 2:'two'}

print(len(d))
print(d.keys())
print(d.values())
print(1 in d)
print(d[1])
print(d.get(3,'no'))
d[1] = 'first'
print(d)
del d[1]
print(d)


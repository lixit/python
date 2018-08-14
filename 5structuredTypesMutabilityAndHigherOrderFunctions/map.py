# map is designed to be used in conjunction with a for loop. When used in a for loop, map behaves like the range function in that it returns one value for each iteraton of the loop. There values are generated by applying the first argument to each element of the second argument.

for i in map(abs,[-2, 3, -4]):
    print(i)

# the first argument of map can be a function of n arguments, in which case it must be followed by n subsequent ordered collections(each of the same length)

L1 = [1, 28, 36]
L2 = [2, 57, 9]
for i in map(min, L1, L2):
    print(i)

#create anonymous functions using the reserved word lambda

L = []
for i in map(lambda x, y:x**y,[1, 2, 3, 4],[3, 2, 1, 0]):
    L.append(i)
print(L)

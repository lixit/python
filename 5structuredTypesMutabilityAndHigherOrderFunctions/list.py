# singleton lists are written without that comma before the closing bracket.
L = ['I did it all', 4, 'love']
M = []
for i in range(len(L)):
    print(L[i])
print(type(M))

# square brackets are used for literals of type list, indexing into lists, and slicing lists

print([1,2,3,4][1:3][1])

# List comprehension provides a concise way to apply an operation to the values in a sequence. It creates a new list in which each element is the result of applying a given operation to a value from a sequence.

L = [x**2 for x in range(1,7)]
print(L)

# for clause in a list comprehension can be followed by one or more if and for statements that are apply to the values produced by the for clause.

mixed = [1, 2, 'a', 3, 4.0]
print([x**2 for x in mixed if type(x)==int])

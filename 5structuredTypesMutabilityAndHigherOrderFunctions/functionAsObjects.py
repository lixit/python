# The function applyToEach is called higher-order because it has an argument that is itself a function

def applyToEach(l, f):
    """Assume L is a list, f is a function
    Mutates L by replacing each element, e, of L by f(e)"""
    for i in range(len(L)):
        L[i]=f(L[i])

L = [1, -2, 3.33]
print('L=',L)

print('Apply abs to each element of L.')
applyToEach(L,abs)
print('L=',L)

print('Apply int to each element of',L)
applyToEach(L,int)
print('L=',L)

print('Apply factorial to each element of',L)
#applyToEach(L,factR)
print('L=',L)

print('Apply Fibonnaci to each element of',L)
#applyToEach(L, fib)
print('L=',L)

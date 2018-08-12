#if an object is bound to a name anywhere in the function body, it is treated as local to that function
def f():
    print(x)

def g():
    print(x)
    x=1

x=3
f()
x=3
g()

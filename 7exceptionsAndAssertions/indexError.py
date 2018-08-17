test = [1, 2, 3]
try:
    test[3]
except IndexError:
    print('There is a IndexError')

def readInt():
    while True:
        val = input('Enter an integer: ')
        try:
            return(int(val))
        except ValueError:
            print(val,'is not an integer')

def readVal(valType, requestMsg, errorMsg):
    print(type(valType))
    while True:
        val = input(requestMsg + ' ')
        try:
            return(valType(val))
        except ValueError:
            print(val, errorMsg)
readInt()
readVal(float, 'Enter a float: ', 'is not a float')

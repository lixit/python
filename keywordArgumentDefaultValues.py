def printName(firstName, lastName, reverse=False):
    if reverse:
        print(lastName+','+firstName)
    else:
        print(firstName,lastName)
printName(1,2,False)
printName(1,2,reverse=False)
printName(1,lastName=2,reverse=False)
printName(lastName=2,firstName=1,reverse=False)
#can not follow a keyword argument with non-keyword argument
#printName(1,lastName=2,False)

#default value allow programmers to call a function wiht fewer than the specified number of arguments

printName('First','Second')
printName('First','Second',True)
printName('First','Second',reverse=True)

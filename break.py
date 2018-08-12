#Find a positive integer that is divisible by both 11 and 12
x=int(input('enter an integer: '))
while True:
    if x%11==0 and x%12==0:
        break
    x=x+1
print(x,'is divisible by 11 and 12')

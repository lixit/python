x=int(input('pls input x:'))
if x%2==0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')
if x%2==0:
    if x%3==0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3==0:
    print('Divisible by 3 and not by 2')
else:
    print('not divisible by 3 and 2')

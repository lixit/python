x=int(input('intput x:'))
y=int(input('intput y:'))
z=int(input('intput z:'))
flag=0
if x%2==1:
    flag+=1;
if y%2==1:
    flag+=2
if z%2==1:
    flag+=4
print('the flag is:',flag)


if flag==0:
    print('no odd number!')
elif flag==1:
    print(x)
elif flag==2:
    print(y)
elif flag==4:
    print(z)
elif flag==3:
    if x<y:
        print(x)
    else:
        print(y)
elif flag==5:
    if x<z:
        print(x)
    else:
        print(z)
elif flag==6:
    if y<z:
        print(y)
    else:
        print(z)
else:
    if x<y and x<z:
        print(x)
    elif y<z:
        print(y)
    else:
        print(z)


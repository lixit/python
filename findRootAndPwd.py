value=int(input('enter a positive integer'))
pwr=1
root=1
i=1
while pwr<6:
    while root**pwr < value:
        root +=1
    if root**pwr == value:
        print(root,pwr)
    root=1
    pwr+=1

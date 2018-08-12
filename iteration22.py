#square an integer, the hard way
x=int(input('intput x: '))
ans=0
itersLeft=x
while(itersLeft!=0):
    ans = ans+x
    itersLeft =itersLeft-1
print(str(x)+'*'+str(x)+'='+str(ans))

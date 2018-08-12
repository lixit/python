#Newton-Raphson for square root
#Find x such that x**2 -24 is within epsilon of o
epsilon=0.0000001
k=24.0
guess=k/2.0
i=0
while abs(guess*guess-k)>=epsilon:
    guess = guess -(((guess**2)-k)/(2*guess))
    i+=1
    print(i)

print('Square root of',k,'is about',guess)

def always_sunny(t1, t2):
    """t1, t2 are non empty"""
    sun = ("sunny","sun")
    first = t1[0] +t2[0]
    return(sun[0],first)

print(always_sunny('cloudy',('cold',)))

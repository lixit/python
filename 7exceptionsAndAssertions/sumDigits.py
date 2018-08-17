def sumDigits(s):
    """Assumes s is a string
    Returns the sum of the decimal digits in s"""
    sums=0
    for i in s:
        if i in '0123456789':
            sums += int(i)
    return sums

print(sumDigits('d66d'))


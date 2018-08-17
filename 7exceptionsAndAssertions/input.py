while True:
    val = input('Enter an integer: ')
    try:
        val = int(val)
        print('The square root of number you entered is', val**2)
        break
    except ValueError:
        print(val,'is not an integer')

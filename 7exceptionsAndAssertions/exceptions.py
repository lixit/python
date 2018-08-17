try:
    successFailureRatio =numSuccesses/numFailures
    print('The success/failure ratio is', successFailureRatio)
except NameError:
    print('there has some name errors')
except ZeroDivisionError:
    print('No failures, so the success/failure ratio is undefined')
print('Now here')

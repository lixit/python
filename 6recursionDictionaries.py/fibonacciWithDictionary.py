def fib_efficient(n, d):
    findTimes=0
    notFindTimes=0
    if n in d:
        findTimes += 1
        print('Finds',findTimes,'times value in dictionary')
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        notFindTimes += 1
        print('not find',notFindTimes,'times. add value to Dictionary')
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib_efficient(12, d))

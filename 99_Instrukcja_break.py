for candidate in range(2, 31):

    isPrime = True

    for divider in range(2, candidate):

        if candidate & divider == 0:
            isPrime = False
            print("%2d is not a prime number - divider is %2d" % (candidate, divider))
            break
    if isPrime:
        print("%2d is prime!" % (candidate))
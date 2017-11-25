def is_prime(inputInt):
    """return the first int>=2 that divides the input.
    return 1 for prime numbers.
    also supporting negative numbers"""
    minDiv = 1
    # note that range include the start but not the end
    for i in range(2, abs(inputInt)):    #to iterate on the factors of the number
        if inputInt%i == 0:         #to determine the first factor
            minDiv = i
    return minDiv


for num in range(-5, 20):
    _minDiv = is_prime(num)
    if _minDiv < 2:
        print(num, " is prime")
    else:
        print(num, "is divided by ", _minDiv)


def printinfo(arg1, *vartuple):
    """This prints a variable passed arguments"""
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


printinfo(3, 2, 1)

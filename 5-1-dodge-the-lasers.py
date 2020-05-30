from decimal import *
import math

# Copied solution from mercio's answer at: https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
def solution(s):
    getcontext().prec = 500
    num = int(s)

    my_sqrt = Decimal(2).sqrt()

    answer = computeStuff(my_sqrt, num)

    return str(answer)

def computeStuff(my_sqrt, k):

    # For some reason, using int(math.floor()) was causing some floating point errors which took me 2 days to figure out. Using int() just
    # made it work somehow.
    # Eg: math.floor(4.9999999999999999) returns 5 for some stupid reason.
    if k <= 100000:
        accumulator = 0
        for i in range(k):
            accumulator += int(my_sqrt * (i+1)) #math.floor(my_sqrt * (i+1))
        return int(accumulator)

    else:
        k2 = int((my_sqrt-1) * Decimal(k)) #int(math.floor((my_sqrt-1) * Decimal(k)))
        return int( int((k*k2) + k*(k+1)/2 - k2*(k2+1)/2) - computeStuff(my_sqrt, k2) )
import math


def trigResults(x):
    return math.sin(x), 1 / (math.sin(x))


def eulersFormula():
    return math.e ** (1j * math.pi) + 1


# n = eulersFormula()
# print(n)

# a, b = trigResults(60)
# print(a, b)

# countdown function
def toTheMoon(countdown):
    '''count down to zero
    gewngekjwjn
    '''
    for i in range(countdown, -1, -1):
        print("{}...".format(i))
    print("BLAST OFF!!!!")


# % use the function
# toTheMoon(10)
print(10%2)

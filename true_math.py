from math import inf

def divide(first, second):
    rez = 0
    if second == 0:
        rez = inf
    else:
        rez =  first / second
    return rez


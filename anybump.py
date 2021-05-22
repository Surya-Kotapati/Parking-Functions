# Copyright 2021, Surya Vikramaditya Kotapati, All Rights Reserved.

# runc generates potential preference vectors of size n, parking checks if
# preference vector is parking function and tracks total number of bumps
__all__ = ['runc','parking']

from random import randint
from math import pow

def runc(n,m):
    result = dict() # Dictionary containing all parking functions for given n
    while len(result) < pow(n+1,n-1):
        func = []           # Empty preference vector
        for _ in range(n):  # For loop builds preference vector of n size
            func.append(randint(1,n))
        # Vector added to result list if parking function and not already in result
        inter = parking(func, n)
        if inter[0] and tuple(func) not in result:
            result[tuple(func)] = inter[1]
    final = [pf for pf in result if result[pf] == m]
    return final     # Return all parking functions of length n and total bumps m


def parking(func, n):
    spaces = []         # Empty vector of the spaces in which the cars actually park
    bumps = 0           # Car parks in preferred spot if space is not occupied
    for i in range(n):
        if func[i] not in spaces:
            spaces.append(func[i])
        else:           # Car continues down the street until empty spot found
            for r in range(func[i]+1, n+1):
                if r not in spaces:
                    spaces.append(r)
                    bumps += r-func[i]
                    break
    # Return whether vector is parking function and associated total number of bumps
    return [len(spaces)==n,bumps]   


if __name__ == "__main__":
    from sys import argv
    n = int(argv[1]) # Accepts n as command-line input
    m = int(argv[2]) # Accepts total number of bumps as command-line input
    if m > (n*(n-1)/2):                        # Handles edge cases
        print("There are no parking functions of that profile")
    else:
        printed = runc(n,m)
        print(printed)
        print("Total number of",m, "bumps is", len(printed))
        


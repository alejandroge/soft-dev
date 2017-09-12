# A n positive integer number is given, the algorithm will display
# "TRUE", if n can be decomposed as two prime numbers addition
# and "FALSE" if not. In case of "TRUE", it must show the two numbers

from math import floor # for floor functionality

# Following function determine if a number is primer or not
def is_prime(n):
    if (n == 2):
        return True
    elif (n > 2):
        for i in range(2, n):
            if (n % i == 0):
                return False
    else:
        return False
    return True

n = int(input('Input your positive integer number ... '))

f = False
for i in range(2, floor(1+n/2)):
    if (is_prime(i) and is_prime(n-i)):
        print('True - '+str(i)+' + '+str(n-i)+' = '+str(i+n-i))
        f = True
if not f:
    print('False')

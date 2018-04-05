import math
import sys


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# >>python RSA_keygen.py -pq 2 3 -x 1
# >>sys.argv -> [RSA_keygen.py, -pq, 2, 3, -x, 1]


if '-pq' in sys.argv:
    flag_index = sys.argv.index('-pq')
    flag_index += 1
    p = int(sys.argv[flag_index])
    flag_index += 1
    q = int(sys.argv[flag_index])
else:
    p = 1009
    q = 2741

if not is_prime(p) or not is_prime(q):
    raise ValueError('P or Q were not prime')

if '-x' in sys.argv:
    flag_index = sys.argv.index('-x')
    flag_index += 1
    x = int(sys.argv[flag_index])
else:
    x = 1

eq = (p - 1) * (q - 1) + 1

y = 1
xy = x*y

while xy != eq:
    x += 1
    y = eq / x
    xy = x*y


print ("public key, x: " + str(x))
print ("private key, y: " + str(y))
print ("modulo (pq): " + str(p*q))

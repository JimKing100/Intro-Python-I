import sys
import math
import time


num_args = len(sys.argv)
arg_list = sys.argv
num = int(arg_list[1])


# If the integer is less than or equal to 1 - False
# If the integer is divisible by any number from 2 - n - False
# Otherwise the integer is a prime
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


# If the integer is less than or equal to 1 - False
# If the integer is 2 - True
# If the integer is greater than 2 and divisible by 2 - False
# If the integer is divisible by any number from 3 to square root of integer - False
# Otherwise the integer is a 16_prime
def check_prime_opt(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if (n > 2) and (n % 2) == 0:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if (n % i) == 0:
            return False
    return True


if num_args != 2:
    print('Format expected: 16_prime.py integer')
else:
    t0 = time.time()
    if check_prime(num) is True:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
    t1 = time.time()
    print('check_prime time required: ', t1 - t0)

if num_args != 2:
    print('Format expected: 16_prime.py integer')
else:
    t0 = time.time()
    if check_prime_opt(num) is True:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')
    t1 = time.time()
    print('check_prime_opt time required: ', t1 - t0)

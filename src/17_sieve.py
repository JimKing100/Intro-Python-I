import sys
import math


num_args = len(sys.argv)
arg_list = sys.argv
num = int(arg_list[1])


# Determine all the prime numbers up to n
def sieve(n):
    # Boolean array set to True
    primes = [True for i in range(2, n + 3)]

    # Iterate through the array with multiples of primes
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i] is True:
            # Set multiples of primes to False
            for j in range(i + i, n + 1, i):
                primes[j] = False
    return primes


prime_nums = sieve(num)
# Iterate through final array to print primes
for i in range(2, num + 1):
    if prime_nums[i] is True:
        print(i)

# The sieve function should return the list of all prime numbers 
# less than or equal to n
def sieve(n):
    primes = list(range(2, n + 1))
    i = 0
    while i < (len(primes) - 1):
        newprimes = primes[:i+1]
        for n in primes[i+1:]:
            if n % primes[i] != 0:
                newprimes.append(n)
        primes = newprimes
        i += 1
    return primes

assert sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]

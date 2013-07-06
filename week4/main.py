def assertEqual(a, b):
    if a != b:
        raise AssertionError("expected " + str(a) + ", got " + str(b))

# The sieve function should return the list of all prime numbers 
# less than or equal to n
def sieve(n):
    # Put your implementation here

assertEqual(sieve(20), [2, 3, 5, 7, 11, 13, 17, 19])

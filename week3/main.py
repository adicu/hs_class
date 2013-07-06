def assertEqual(a, b):
    if a != b:
        raise AssertionError("expected " + str(a) + ", got " + str(b))

def euclid(a, b):
    while b != 0:
        if a < b:
            c = a
            a = b
            b = c
        else:
            r = a - b
            a = b
            b = r
    return a

# The following code will test several a-b pairs to make sure the function
# you wrote outputs the correct answer.
# If the answer is wrong, you will see an error message print out when you
# run the code. Otherwise, the program will print nothing.
assertEqual(euclid(6, 4), 2)
assertEqual(euclid(13, 7), 1)
assertEqual(euclid(48, 72), 24)

#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

if len(sys.argv) != 2:
    print("Error: Usage - {} <non-negative integer>".format(sys.argv[0]))
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError
except ValueError:
    print("Error: Please provide a valid non-negative integer.")
    sys.exit(1)

result = factorial(num)
print(result)

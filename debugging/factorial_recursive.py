def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer recursively.

    Parameters:
    - n: A non-negative integer for which factorial needs to be calculated.

    Returns:
    Factorial of the input number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input from the command line argument and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the factorial
print(f)

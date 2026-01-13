#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    # Read the input number from command-line arguments
    f = factorial(int(sys.argv[1]))
    # Print the result
    print(f)


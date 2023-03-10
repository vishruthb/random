import sys
import math

# Helper function to read integer inputs
def read_int():
    return int(sys.stdin.readline().strip())

# Helper function to read multiple integer inputs
def read_ints():
    return map(int, sys.stdin.readline().strip().split())

# Helper function to read string inputs
def read_str():
    return sys.stdin.readline().strip()

# Helper function to read multiple string inputs
def read_strs():
    return sys.stdin.readline().strip().split()

# Helper function to calculate factorial of a number
def factorial(n):
    return math.factorial(n)

# Helper function to calculate GCD of two numbers
def gcd(a, b):
    return math.gcd(a, b)

# Helper function to calculate LCM of two numbers
def lcm(a, b):
    return a * b // gcd(a, b)

# Main function to solve the problem
def solve():
    # read inputs
    n = read_int()
    a = list(read_ints())
    
    # perform required operations
    # ...
    
    # output the result
    print(result)

# run the main function
if __name__ == '__main__':
    solve()

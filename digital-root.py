# What is the sum of the digits in the sum of the first 123456789 positive integers?

# Sum of Integers formula
def sum_of_integers(n):
    return int(n*(1+n)/2)

# Digital Root recursive formula
def digit_root(n): 
    return (n - 1) % 9 + 1

# Test
n = 123456789
N = digit_root(sum_of_integers(n))
print(f'The sum of the digits in the sum of the first {n} positive integer is {N}')
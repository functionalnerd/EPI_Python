"""
Solutions to Chapter 5.1.

This solution will review computing the parity of a word, including the brute 
force method, along with the final optimized solution.
"""
__author__ = "Justin Oliver"
__email__ = "functionaln3rd@gmail.com"

def brute_force(x):
    """
    Computes the parity of the input.

    The parity of a binary word is 1 if the number of 1s is odd, otherwise, it 
    is 0.
    
    :param int x: parity is calculated on x
    :returns: parity of x
    :raises: ValueError

    .. doctest::

       >>> from Primitive_Types._5_1 import brute_force
       >>> brute_force(0b1010)
       0
       >>> brute_force(0b10101)
       1
    """
    if isinstance(x, int) is False:
        raise ValueError("Invalid input")
    
    result = 0
    while x:
        result ^= (x & 1)
        x >>= 1
    
    return result

# Experiment imports
import tracemalloc
import time

import math
import random
import copy

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    result = 0
    for i in range(len(xs)):
        result += xs[i] * (x ** i)
    return result

def find_zero(xs: list):
    """ 
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Check if the number of coefficients is even
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    
    # Find the largest non-zero coefficient
    largest_coefficient = max(xs, key=abs)
    if largest_coefficient == 0:
        raise ValueError("The largest non-zero coefficient must be non-zero.")
    
    # Find the zero point
    zero_point = None
    for x in range(-100, 101):
        if poly(xs, x) == 0:
            zero_point = x
            break
    
    return zero_point

tracemalloc.start()
start_time = time.perf_counter()

find_zero([1, 2]) # -0.5

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)
print(tracemalloc.get_traced_memory())
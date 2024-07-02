# Experiment imports
import tracemalloc
import time
#import cProfile
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    
    >>> factorize(8)
    [2, 2, 2]
    
    >>> factorize(25)
    [5, 5]
    
    >>> factorize(70)
    [2, 5, 7]
    """
    fact = []
    while n % 2 == 0:
        fact.append(2)
        n //= 2
    i = 3
    while i <= int(math.sqrt(n) + 1):
        while n % i == 0:
            fact.append(i)
            n //= i
        i += 2
    if n > 1:
        fact.append(n)
    return fact

tracemalloc.start()
start_time = time.perf_counter()

factorize(8) # [2, 2, 2]

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)

# RAM Measurement
print(tracemalloc.get_traced_memory()) # the amount of memory current allocated + the peak allocated memory
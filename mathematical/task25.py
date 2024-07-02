# Experiment imports
import profile
from typing import List

#Prompt
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
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

#tracemalloc.start()
#start_time = time.perf_counter()

#cProfile.run('factorize(8)') # [2, 2, 2]
pr = profile.Profile()

print(pr.run(factorize(8)))

#end_time = time.perf_counter()
#print("Execution time: (s)", end_time - start_time)

# RAM Measurement
#print(tracemalloc.get_traced_memory())
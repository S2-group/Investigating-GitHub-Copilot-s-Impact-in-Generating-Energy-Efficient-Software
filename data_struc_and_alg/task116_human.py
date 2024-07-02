# Experiment imports
import tracemalloc
import time

def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    the number of ones in their binary representation in ascending order.
    For a similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) == [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

tracemalloc.start()
start_time = time.perf_counter()

sort_array([1, 5, 2, 3, 4]) # [1, 2, 3, 4, 5]


end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)

# RAM Measurement
print(tracemalloc.get_traced_memory()) 
import time
import tracemalloc

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

start_time = time.perf_counter()
tracemalloc.start()

generate_integers(2, 8) == [2, 4, 6, 8]

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)
print(tracemalloc.get_traced_memory()) 
import time
import tracemalloc
def triangle_area(a, h):
    """
    Given length of a side and height, return the area of a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h * 0.5 

start_time = time.perf_counter()
tracemalloc.start()

triangle_area(5, 3) == 7.5

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)
print(tracemalloc.get_traced_memory()) 
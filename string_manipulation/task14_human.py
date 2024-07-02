# Experiment imports
import tracemalloc
import time

from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result

tracemalloc.start()

start_time = time.perf_counter()

all_prefixes('abc') # ['a', 'ab', 'abc']

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)

# RAM Measurement
print(tracemalloc.get_traced_memory()) # the amount of memory current allocated + the peak allocated memory

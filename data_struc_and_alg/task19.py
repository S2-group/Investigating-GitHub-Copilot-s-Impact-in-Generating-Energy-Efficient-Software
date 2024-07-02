# Experiment imports
import tracemalloc
import time

from typing import List

#Prompt
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: number_map[x])

    return ' '.join(numbers_list)

tracemalloc.start()
start_time = time.perf_counter()


sort_numbers('three one five') # 'one three five'

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)

# RAM Measurement
print(tracemalloc.get_traced_memory())
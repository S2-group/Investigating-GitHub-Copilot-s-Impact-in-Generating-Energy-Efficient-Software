# Experiment imports
import tracemalloc
import time

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    res = ''
    for i in range(len(num)):
        while number >= num[i]:
            res += sym[i]
            number -= num[i]
    return res.lower()

tracemalloc.start()
start_time = time.perf_counter()

int_to_mini_roman(19) == 'xix'

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)
print(tracemalloc.get_traced_memory()) # the amount of memory current allocated + the peak allocated memory
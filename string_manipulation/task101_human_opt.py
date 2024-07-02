# Experiment imports
import tracemalloc
import time

def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    if not s:
        return []

    s_list = s.replace(',', ' ').split()
    return s_list

tracemalloc.start()
start_time = time.perf_counter()

words_string("Hi, my name is John")

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)

# RAM Measurement
print(tracemalloc.get_traced_memory()) # the amount of memory current allocated + the peak allocated memory
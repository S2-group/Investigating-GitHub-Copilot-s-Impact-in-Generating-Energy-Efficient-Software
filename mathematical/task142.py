import time
import tracemalloc


def sum_squares(lst):
    """
    This function takes a list of integers. For each entry in the list, the function squares the integer if its index is a multiple of 3,
    and cubes the integer if its index is a multiple of 4 but not a multiple of 3. The function does not change entries whose indexes
    are not multiples of 3 or 4. The function then returns the sum of all entries.
    
    Examples:
    For lst = [1,2,3], the output should be 6.
    For lst = [], the output should be 0.
    For lst = [-1,-5,2,-1,-5], the output should be -126.
    """
    result = []
    for i in range(len(lst)):
        if i % 3 == 0:
            result.append(lst[i] ** 2)
        elif i % 4 == 0 and i % 3 != 0:
            result.append(lst[i] ** 3)
        else:
            result.append(lst[i])
    return sum(result)

tracemalloc.start()
start_time = time.perf_counter()

sum_squares([1,2,3]) == 6

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)

print(tracemalloc.get_traced_memory()) 
# Experiment imports
import tracemalloc
import time

def decimal_to_binary(decimal):
    """
    You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    decimal_to_binary(15)   # returns "db1111db"
    decimal_to_binary(32)   # returns "db100000db"
    """
    binary = bin(decimal)[2:]  # Convert decimal to binary string
    return "db" + binary + "db"  # Add 'db' at the beginning and end of the binary string


tracemalloc.start()

start_time = time.perf_counter()

decimal_to_binary(15)  
# returns "db1111db"

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)

# RAM Measurement
print(tracemalloc.get_traced_memory())
# Experiment imports
import tracemalloc
import time
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ 
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    begin, end = -1., 1.
    poly_begin = poly(xs, begin)
    poly_end = poly(xs, end)
    while poly_begin * poly_end > 0:
        begin *= 2.0
        end *= 2.0
        poly_begin = poly(xs, begin)
        poly_end = poly(xs, end)
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        poly_center = poly(xs, center)
        if poly_center * poly_begin > 0:
            begin = center
            poly_begin = poly_center
        else:
            end = center
            poly_end = poly_center
    return begin

tracemalloc.start()
start_time = time.perf_counter()

find_zero([1, 2]) # -0.5

end_time = time.perf_counter()
print("Execution time: (s)", end_time - start_time)
print(tracemalloc.get_traced_memory()) # the amount of memory current allocated + the peak allocated memory
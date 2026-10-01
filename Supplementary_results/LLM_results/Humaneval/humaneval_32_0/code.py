## main.py
import math
from typing import List

def poly(xs: List[float], x: float) -> float:
    """Evaluate a polynomial at a given point.

    Args:
        xs (List[float]): List of coefficients of the polynomial.
                          For example, [1, 2] represents the polynomial 1 + 2x.
        x (float): The point at which to evaluate the polynomial.

    Returns:
        float: The evaluated polynomial value at x.
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: List[float], lower_bound: float = -1000.0, upper_bound: float = 1000.0, tolerance: float = 1e-7) -> float:
    """Find a root of the polynomial using the bisection method.

    Args:
        xs (List[float]): List of coefficients of the polynomial.
                          Must have an odd number of coefficients.
        lower_bound (float): The lower bound of the interval to search for a root.
                             Default is -1000.0.
        upper_bound (float): The upper bound of the interval to search for a root.
                             Default is 1000.0.
        tolerance (float): The tolerance for stopping the search.
                           Default is 1e-7.

    Returns:
        float: A single root of the polynomial.

    Raises:
        ValueError: If the number of coefficients is not odd or if no root is found in the interval.
    """
    if len(xs) % 2 != 1:
        raise ValueError("The number of coefficients must be odd.")
    
    f_lower = poly(xs, lower_bound)
    f_upper = poly(xs, upper_bound)

    if f_lower * f_upper > 0:
        raise ValueError("The function must have different signs at the bounds.")

    while (upper_bound - lower_bound) > tolerance:
        midpoint = (lower_bound + upper_bound) / 2
        f_mid = poly(xs, midpoint)

        if f_mid == 0:
            return midpoint  # Found exact root
        elif f_lower * f_mid < 0:
            upper_bound = midpoint
            f_upper = f_mid
        else:
            lower_bound = midpoint
            f_lower = f_mid

    return (lower_bound + upper_bound) / 2  # Return the midpoint as the root

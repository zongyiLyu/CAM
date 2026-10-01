## main.py

import math

def angle_complex(real: float, imag: float) -> float:
    """Calculate the angle of a complex number in radians.

    Args:
        real (float): The real part of the complex number.
        imag (float): The imaginary part of the complex number.

    Returns:
        float: The angle in radians calculated using atan2.
               If both real and imaginary parts are zero, returns 0.0.
    """
    # Handle the edge case where both real and imaginary parts are zero
    if real == 0 and imag == 0:
        return 0.0
    
    # Calculate the angle using atan2
    angle = math.atan2(imag, real)
    return angle

## main.py
import math

def surfacearea_sphere(radius: float) -> float:
    """Calculate the surface area of a sphere given its radius.

    Parameters:
    radius (float): The radius of the sphere. Must be a non-negative number.

    Returns:
    float: The surface area of the sphere.

    Raises:
    ValueError: If the radius is negative or not a number.
    """
    # Validate the input
    if not isinstance(radius, (int, float)):
        raise ValueError("The radius must be a numeric value.")
    if radius < 0:
        raise ValueError("The radius must be a non-negative number.")

    # Calculate the surface area using the formula 4 * π * r^2
    surface_area = 4 * math.pi * (radius ** 2)
    
    return surface_area

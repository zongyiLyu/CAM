## main.py

def parabola_directrix(a: float, b: float, c: float) -> float:
    """
    Calculate the directrix of a parabola given its coefficients.

    Parameters:
    a (float): Coefficient of x^2
    b (float): Coefficient of x
    c (float): Constant term

    Returns:
    float: The directrix of the parabola.
    
    Raises:
    ValueError: If the coefficient 'a' is zero, as it would not represent a parabola.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero for a parabola.")

    # Calculate the vertex (h, k) of the parabola
    h = -b / (2 * a)
    k = (4 * a * c - b**2) / (4 * a)

    # Calculate the distance p from the vertex to the focus
    p = 1 / (4 * a)

    # Calculate the directrix using the formula
    directrix = k - p

    return directrix

## main.py
from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    """Convert a list of GPAs to letter grades based on a defined scale.

    Args:
        grades (List[float]): A list of GPAs (0.0 to 4.0).

    Returns:
        List[str]: A list of corresponding letter grades.

    Raises:
        ValueError: If any GPA is not in the range [0.0, 4.0].
    """
    # Define the grading scale
    grade_scale = [
        (4.0, 'A+'),
        (3.7, 'A'),
        (3.3, 'A-'),
        (3.0, 'B+'),
        (2.7, 'B'),
        (2.3, 'B-'),
        (2.0, 'C+'),
        (1.7, 'C'),
        (1.3, 'C-'),
        (1.0, 'D+'),
        (0.7, 'D'),
        (0.0, 'F')
    ]
    
    letter_grades = []

    for gpa in grades:
        # Validate GPA
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError(f"Invalid GPA: {gpa}. GPA must be in the range [0.0, 4.0].")
        
        # Determine letter grade
        for threshold, letter in grade_scale:
            if gpa >= threshold:
                letter_grades.append(letter)
                break

    return letter_grades

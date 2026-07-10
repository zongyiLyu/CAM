## main.py
from collections import Counter

def histogram(test: str) -> dict[str, int]:
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    if not test:
        return {}
    
    # Split the input string into a list of letters
    letters = test.split()
    
    # Count occurrences of each letter using Counter
    letter_counts = Counter(letters)
    
    # Determine the maximum count
    max_count = max(letter_counts.values())
    
    # Create a dictionary of letters with the maximum count
    max_letters = {letter: count for letter, count in letter_counts.items() if count == max_count}
    
    return max_letters

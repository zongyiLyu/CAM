## main.py

def is_bored(S: str) -> int:
    """
    Count the number of sentences starting with 'I'.
    
    Parameters:
    S (str): The input string containing sentences.
    
    Returns:
    int: The count of sentences that start with 'I'.
    """
    # Define the sentence delimiters
    delimiters = {'.', '?', '!'}
    
    # Split the input string into sentences
    sentences = []
    current_sentence = []
    
    for char in S:
        current_sentence.append(char)
        if char in delimiters:
            sentences.append(''.join(current_sentence).strip())
            current_sentence = []
    
    # Add the last sentence if it exists
    if current_sentence:
        sentences.append(''.join(current_sentence).strip())
    
    # Count sentences that start with 'I'
    count = sum(1 for sentence in sentences if sentence.startswith('I'))
    
    return count

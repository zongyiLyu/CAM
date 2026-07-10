## main.py

def lps(s: str) -> int:
    """
    Calculate the length of the longest palindromic subsequence in a given string.

    Parameters:
    s (str): The input string to analyze.

    Returns:
    int: The length of the longest palindromic subsequence.
    """
    # Normalize the input string by removing non-alphanumeric characters and converting to lowercase
    normalized_s = ''.join(char.lower() for char in s if char.isalnum())
    
    n = len(normalized_s)
    
    # Edge case: if the string is empty, return 0
    if n == 0:
        return 0
    
    # Create a DP table to store lengths of longest palindromic subsequences
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the DP table
    for length in range(2, n + 1):  # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if normalized_s[i] == normalized_s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # The length of the longest palindromic subsequence is in dp[0][n-1]
    return dp[0][n - 1]

def solution(N):
    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Initialize the result string
    result = ''

    # Determine the number of letters needed to fill the string
    num_letters = N // 2

    # Fill the result string with pairs of letters from the alphabet
    for i in range(num_letters):
        result += alphabet[i % 26] * 2

    # If there's an odd number of characters, add one more letter to the result
    if N % 2 != 0:
        result += alphabet[0]

    return result

# Test cases
print(solution(3))  
print(solution(5)) 
print(solution(30)) 

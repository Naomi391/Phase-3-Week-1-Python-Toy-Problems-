def digit_sum(num):
    # Function to calculate the sum of digits of a number
    return sum(int(digit) for digit in str(num))

def solution(A):
    max_sum = -1  # Initialize the maximum sum as -1
    digit_sums = {}  # Dictionary to store numbers grouped by their digit sums
    
    # Group numbers by their digit sums
    for num in A:
        sum_digits = digit_sum(num)
        if sum_digits not in digit_sums:
            digit_sums[sum_digits] = []
        digit_sums[sum_digits].append(num)
    
    # Check for pairs with equal digit sums
    for sum_digits, numbers in digit_sums.items():
        if len(numbers) > 1:
            # Sort numbers to get the largest pair
            numbers.sort(reverse=True)
            # Add the largest pair to the maximum sum
            max_sum = max(max_sum, sum(numbers[:2]))
    
    return max_sum

# Test cases
print(solution([51, 71, 17, 42]))  # Output should be 93
print(solution([42, 33, 60]))      # Output should be 102
print(solution([51, 32, 43]))      # Output should be -1

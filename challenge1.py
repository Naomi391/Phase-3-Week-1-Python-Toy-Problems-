def solution(A):
    total_bricks = sum(A)
    target_bricks_per_box = 10
    num_boxes = len(A)
    
    if total_bricks % num_boxes != 0:
        return -1
    
    moves = 0
    target_bricks = total_bricks // num_boxes
    
    for i in range(1, num_boxes):
        diff = A[i] - target_bricks_per_box
        A[i] -= diff
        A[i-1] += diff
        moves += abs(diff)
    
    return moves

# Example usage:
A1 = [7, 15, 10, 8]
print(solution(A1)) # Output: 7

A3 = [7, 14, 10]
print(solution(A3)) # Output: -1

def solution(A):
    moves = 0
    for i in range(1, len(A)):
        difference = A[i] - 10
        A[i] -= difference
        A[i - 1] += difference
        moves += abs(difference)

    if all(box == 10 for box in A):
        return moves
    else:
        return -1

print(solution([7, 15, 10, 8]))  # Output: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # Output: 6
print(solution([7, 14, 10]))  # Output: -1

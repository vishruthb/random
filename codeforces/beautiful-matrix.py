def moves(matrix):
    moves = 0
    # find the 1 in matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '1':
                # find the 1's position
                x = i
                y = j
    moves = abs(x - 2) + abs(y - 2)
    return moves


n1 = (input())
n2 = (input())
n3 = (input())
n4 = (input())
n5 = (input())

matrix = [n1.split(), n2.split(), n3.split(), n4.split(), n5.split()]

print(moves(matrix))

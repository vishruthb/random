def get_max_border(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_border = 0
    
    # Check for maximum border in rows
    for i in range(rows):
        j = 0
        while j < cols:
            if matrix[i][j] == "#":
                count = 1
                j += 1
                while j < cols and matrix[i][j] == "#":
                    count += 1
                    j += 1
                max_border = max(max_border, count)
            else:
                j += 1
    
    # Check for maximum border in columns
    for j in range(cols):
        i = 0
        while i < rows:
            if matrix[i][j] == "#":
                count = 1
                i += 1
                while i < rows and matrix[i][j] == "#":
                    count += 1
                    i += 1
                max_border = max(max_border, count)
            else:
                i += 1
                
    return max_border

# Test the function with sample inputs
test_cases = int(input())
for i in range(test_cases):
    rows, cols = map(int, input().split())
    matrix = [input().strip() for j in range(rows)]
    max_border = get_max_border(matrix)
    print(max_border)

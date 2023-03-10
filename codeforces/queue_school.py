n, t = map(int, input().split())
queue = list(input())

for i in range(t):
    j = 0
    while j < n - 1:
        if queue[j] == 'B' and queue[j+1] == 'G':
            queue[j], queue[j+1] = queue[j+1], queue[j]
            j += 2
        else:
            j += 1

print(''.join(queue))
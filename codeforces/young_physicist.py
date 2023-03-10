n = int(input())

x_cord = []
y_cord = []
z_cord = []

for i in range(n):
    pos = input().split()
    x_cord.append(int(pos[0]))
    y_cord.append(int(pos[1]))
    z_cord.append(int(pos[2]))

if sum(x_cord) == 0 and sum(y_cord) == 0 and sum(z_cord) == 0:
    print("YES")
else:
    print("NO")
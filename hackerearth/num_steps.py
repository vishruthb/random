def solve(ar1, ar2, n):
    
    ans = 0
     
    flag = True
     
    while min(ar1) > -1:
        a = min(ar1)

        for i in range(n):
            if ar1[i]!= a:
                ar1[i]-= ar2[i]
                ans+= 1
                 
        if len(set(ar1))== 1:
            flag = False
            return ans
            break

    if flag:
        return -1


n = int(input())

a_1 = list(map(int, input().split()))
a_2 = list(map(int, input().split()))
     
print(solve(a_1, a_2, n))

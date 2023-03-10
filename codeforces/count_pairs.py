t = int(input())  # number of test cases

for _ in range(t):
    n, k = map(int, input().split())  # read n and k for the current test case
    s = input()  # read the string for the current test case
    
    # initialize variables for counting uppercase and lowercase letters
    upper_count = [0] * 26
    lower_count = [0] * 26
    
    # count the number of uppercase and lowercase letters
    for c in s:
        if c.isupper():
            upper_count[ord(c) - ord('A')] += 1
        else:
            lower_count[ord(c) - ord('a')] += 1
    
    # calculate the number of burles that can be obtained without any operations
    burles = 0
    for i in range(26):
        burles += min(upper_count[i], lower_count[i])
    
    # calculate the number of burles that can be obtained with operations
    if k > 0:
        for i in range(26):
            for j in range(k):
                if upper_count[i] == lower_count[i]:
                    break
                elif upper_count[i] < lower_count[i]:
                    if k - j >= upper_count[i]:
                        k -= upper_count[i]
                        lower_count[i] -= upper_count[i]
                        burles += upper_count[i]
                        upper_count[i] = 0
                    else:
                        upper_count[i] -= k - j
                        lower_count[i] -= k - j
                        burles += k - j
                        k = 0
                else:
                    if k - j >= lower_count[i]:
                        k -= lower_count[i]
                        upper_count[i] -= lower_count[i]
                        burles += lower_count[i]
                        lower_count[i] = 0
                    else:
                        upper_count[i] -= k - j
                        lower_count[i] -= k - j
                        burles += k - j
                        k = 0
    
    # output the result for the current test case
    print(burles)
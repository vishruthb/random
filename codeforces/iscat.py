t = int(input())  # read the number of test cases

for i in range(t):
    n = int(input())  # read the length of the string
    s = input()  # read the string

    # check if the string starts with "m" or "M"
    if s[0] != 'm' and s[0] != 'M':
        print("NO")
        continue  # go to the next test case

    # check if the string contains only "m", "e", "o", "w" or their uppercase versions
    for c in s:
        if c not in ['m', 'M', 'e', 'E', 'o', 'O', 'w', 'W']:
            print("NO")
            break  # go to the next test case
    else:
        # check if the string contains "e", "o", and "w" in order
        if 'e' in s[1:] and 'o' in s[s.index('e')+1:] and 'w' in s[s.index('o')+1:]:
            print("YES")
        else:
            print("NO")
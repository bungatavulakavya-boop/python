s=[1,6,7,8,13,2]
target=10
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]+s[j]==target:
            print(i,j)
            break

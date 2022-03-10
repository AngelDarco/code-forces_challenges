n = int(input())
s = str(input())
res = 0
if n >= 1 and n <= 50:
    for i,x in enumerate(s):
        if i != len(s)-1 and x == s[i+1] :
            res += 1
print(res)
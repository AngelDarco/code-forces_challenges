x = int(input())
res = int()
if x >= 1 and x <= 10**6:
        while x >= 5:
            x = x-5
            res +=1
if x > 0:
    print(res+1)
else:
    print(res)
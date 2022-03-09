w = str(input())
res = str()
if len(w) < 10**3:
    for i,x in enumerate(w):
        if i > 0:
            res += x
        else: 
            res += w[0].upper()
print(res)
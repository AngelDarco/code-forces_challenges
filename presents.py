n = int(input())
p = [int(x) for x in input().split()]
coun = int(1)
res,j = [],[]

if n >= 1 and n <= 100 :
    for u in p:
        j.append(u)
    while len(p) != len(res) :
        for i,x in enumerate(p) :
            if x == coun :
                res.append(i+1)
                coun += 1
print(' '.join([str(x) for x in res]))
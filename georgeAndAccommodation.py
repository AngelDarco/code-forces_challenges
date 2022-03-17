n = int(input())
arr,p,q = [],[],[]
res = int()

if n >=1 and n <= 100 :
    for x in range(n) :
        arr.append([int(i) for i in input().split()])
    for a in arr :
        p.append(a[0])
        q.append(a[1])
    for m in range(n) :
        if p[m] >= 0 and q[m] >= p[m] and q[m] <= 100 :
            if p[m]+2 <= q[m] :
                res += 1
print(res)
n,t = map(int,input().split())
s = input()
con = int()
res = []

for x in s:
    res.append(x)

if n >= 1 and t <= 50 :
    while t > 0 :
        for _ in enumerate(range(n)):
            if con+1 < n :
                if res[con] == 'B' and res[con+1] == 'G':
                    res[con] = 'G'
                    res[con+1] = 'B'
                    con +=1 
            con += 1       
        t -= 1
        con = 0
print(''.join(res))

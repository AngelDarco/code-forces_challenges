n = int(input())
en = int()
ex = []
res = []

if n >= 2 and n <= 1000:
    for x in range(n):
        a,b = map(int,input().split())
        if a >= 0 and b <= 1000:
            if x != 0:
                ex.append(en) 
                en = en+b-a
            else: en = en + b                         
res = sorted(ex)
print(res[-1])
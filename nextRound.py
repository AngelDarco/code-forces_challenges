n,k = map(int, input().split())
a = []
c = 0
t = int()
m = int()
j = int()
if n >= k :
    if k >= 1 and n <= 50:
        a = input().split()
        for i,x in enumerate(a, start=1):
            if int(x) >= 0 and int(x) <= 100:
                if int(x) == 0:
                    m +=1
                    if m == len(a):
                        t = 0 
                elif n == k:
                    if int(x) != 0:
                        j +=1
                    if j == k: t = k
                    else: t = j
                else:     
                    if k+c < len(a):
                        if  a[k-1] == a[k+c] :
                            c+=1
                    if c != 0 :
                        if int(k+c) >= int(i) :
                            t +=1 
                    else: 
                        t = k 
print(t)            
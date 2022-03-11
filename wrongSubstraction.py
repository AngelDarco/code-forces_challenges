n,k = map(int, input().split())
res = int()

if n >= 2 and n <= 10**9 and k >= 1 and k <= 50 :
    for x in range(k):
        if n%10 == 0:
            n = n/10
        else:
            n = n-1
print(int(n))
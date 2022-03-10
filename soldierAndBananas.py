k,n,w = map(int, input().split())
res = int()
if 1 <= k and k <= 1000 and w <= 1000 and 0 <= n and n <= 10**9:
    for x in range(1, w+1):
        res = res +(k*x)
    if res <= n :
        print(0)
    else:
        print(res-n)
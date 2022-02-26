m,n = map(int, input().split())
if m >=1 and n >= m and n <= 16 :
    if m == 1 and n == 1:
        print(0)
    else:
        print(int(m * n) // 2)
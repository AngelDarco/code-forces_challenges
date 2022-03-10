a,b = map(int, input().split())
res = int()
if a >= 1 and b >= a and b <= 10:
    while a <= b:
        a = a*3
        b = b*2
        res += 1
print(res)

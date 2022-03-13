n = int(input())
s = str(input())
a = int()
d = int()

if n >=1 and n <= 10**6 :
    for x in s :
        if x == 'A' :
            a += 1
        elif x == 'D' :
            d += 1
    if a > d :
        print('Anton')
    elif a < d :
        print('Danik')
    else:
        print('Friendship')
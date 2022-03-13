n = int(input())
coun = int()
coun2 = int()

if n >= 1 and n <= 10**18 :
    for x in str(n) :
        if x == '4' or x == '7' :
            coun += 1
    for y in str(coun) :
        if y == '4' or y == '7' :
            coun2 += 1
    if coun2 == len(str(coun)) :
        print('YES')
    else: 
        print('NO')
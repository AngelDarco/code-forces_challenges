y = int(input())
a,b,c,d = int(), int(), int(), int()

if y >= 1000 and y <= 9000 :
    while 1 == 1 :
        y += 1 
        a = y/1000
        b = y/100%10
        c = y/10%10
        d = y%10
        if int(a) != int(b) and int(a) != int(c) and int(a) != int(d) and int(b) != int(c) and int(b) != int(d) and int(c) != int(d) :
            break 
print(y)
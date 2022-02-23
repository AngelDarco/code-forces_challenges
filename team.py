n = int(input())
a = []
o = int()
c = int()
d = int()
if(n >= 1 and n <= 1000):
    for x in range(n):
        a.append( input())
    for i in a:  
        for m in i: 
            if m == '1':
                o +=1
            elif m != ' ':
                c +=1
        if o > c:
            d +=1
            o = 0
            c = 0
        else:
            o = 0
            c = 0
print(d)

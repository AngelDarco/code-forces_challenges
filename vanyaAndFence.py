n,h = map(int, input().split())
a = [int(x) for x in input().split()]

coun =  int()
if n >= 1 and n <= 1000 and h >= 1 and h <= 1000 :
    for z in a:
        if z >= 1 and z <= h*2:
            if z > h :
                coun += 2
            else:
                coun += 1
print(coun)
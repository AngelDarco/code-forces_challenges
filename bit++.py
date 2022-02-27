n = int(input())
x = 0
for a in range(n):
    y = str(input().upper())
    if y == 'X++' or y == '++X':
        x +=1
    else :
        x -=1
print(x)
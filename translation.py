s = input().lower()
t = input().lower()

if s != '' and t != '' and len(s) <= 100 and len(t) <= 100 :
    if (s[::-1] == t) :
        print('YES')
    else:
        print('NO')
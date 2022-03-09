w = str(input())
res = []
if len(w) < 100 and w != '':
    for x in sorted(w):
        if x not in res :
            res.append(x)
    if len(res) % 2 == 0 :
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
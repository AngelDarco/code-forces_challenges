s = input().split('+')
s2 = sorted(s)
res = str()
for i, x in enumerate(s2):
    if len(s2) > i+1:
        res += x+'+'
    else: res += x

print(res)
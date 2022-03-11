w = input()
low = int()
upp = int()

if len(w) > 1 and len(w) < 100:
    for x in w :
        if x.isupper():
            upp += 1
        else:
            low +=1
    if upp > low:
        print(w.upper())
    elif low >= upp:
        print(w.lower())
    
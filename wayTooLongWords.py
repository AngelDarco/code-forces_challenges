n = int(input())
word = []
if n >= 1 and n <= 100:
    for i in range(n) :
        word.append(input())
for x in word:
        if(len(x) > 10):
                f = str(x[0])
                n = str(len(x)-2)
                l = str(x[-1])
                print(f+n+l)
        else:
            print(x) 
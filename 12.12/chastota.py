import random
someList = [random.randint(0, 100) for i in range(random.randint(5, 50))]
schet = 0
schet2 = 0
a = 0
b = -1
d = -1
num = 0
for i in someList:
    b+=1
    a = someList[b]
    for i in someList:
        d+=1
        if someList[d]== a:
            schet+=1
    if schet > schet2:
        schet2 = schet
        num = b 
print(num,"повторяется",schet2, "раз")

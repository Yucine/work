import random
seriy=0
i=0
b=0
while i<=20:
    while seriy < 12:
        a=(random.randint(0,2))
        seriy+=a
        b =a
        print(b, end = "")
    if seriy == 12:
        i+=1
        print("")
    seriy=0

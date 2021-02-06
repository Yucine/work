a = input("введи строку для зашифровки")
b = 0
schet = 0
a1=[]
a2=[]
for i in a:
    b+=1
c = b // 2
for i in range(c):
    a1+=(a[schet])
    schet+=1
while schet < b:
    a2+=(a[schet])
    schet+=1
schet=0
print (a1,a2)
for i in a1:
    print(a1[schet])
    schet+=1
schet=0
for i in a2:
    print(a2[schet])
    schet+=1


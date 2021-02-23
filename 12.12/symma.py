import random
someList = []
bufer = []
schet = 0
someList = [random.randint(0, 100) for i in range(random.randint(5, 50))]
print (someList)
a = someList[0] + someList[1] + someList[2]
for i in range (3):
    bufer+=[someList[schet]]
    schet+=1
for i in range (3):
    one = someList[i]
    two = someList[i+1]
    three = someList[i+2]
    b = someList[i] + someList[i+1] + someList[i+2]
    if b > a:
        a = b
        bufer+=[one,two,three]
print (bufer[-1], bufer[-2],bufer[-3],'-три последовательныx числа с самой большой суммой')


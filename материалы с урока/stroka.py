import random
list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
zamena=4
S = input("введите строку")
a = 0
for i in S:
    for i in range(3):
        if a == 1 :
            print(random.choice(list), end="")
            a+=1
        elif a == zamena:
            print(random.choice(list), end="")
            a+=1
            zamena+=3
        else:
            print (S[a], end="")
            a+=1
    print("")

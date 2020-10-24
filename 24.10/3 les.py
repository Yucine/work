import random
n = int(input("сколько игр сыграть:"))
win=0
loose=0
draw=0
for i in range (n) :
        a = int(input("чем сыграть 1-камень, 2-ножницы, 3 -бумага"))
        b = (random.randint(1, 3))
        if a == b:
            print("ничья")
            draw+=1
        elif a == 1 and b == 2:
            print("победа, камень ломает ножницы")
            win+=1
        elif a ==1 and b ==3:
            print("поражение, бумага накрывает камень")
            loose+=1
        elif a ==2 and b == 1:
            print("поражение, камень ломает ножницы")
            loose+=1
        elif a ==2 and b == 3:
            print("победа, ножницы режут бумагу")
            win+=1
        elif a == 3 and b ==1:
            print("победа, бумага накрывает камень")
            win+=1
        elif a == 3 and b ==2:
            print("поражение, ножницы режут бумагу")
            loose+=1
print("побед",win,"раз")
print("поражений",loose,"раз")
print("ничья",draw,"раз")

            
            
             
            
            
        
        


import random
win = 0
loose = 0
draw = 0
def game(yourComand, botComand):
        if yourComand == botComand:
                print("ничья")
                draw+=1
        elif yourComand== 1 and botComand == 2 or yourComand ==2 and botComand == 3 or yourComand == 3 and botComand ==1:
                print("победа")
                win+=1
        else :
                print("проигрыш")
                loose+=1
n=int(input("сколько игр сыграть"))
for i in range (n) :
        yourComand = int(input("чем сыграть 1-камень, 2-ножницы, 3 -бумага"))
        botComand = (random.randint(1, 3))
        game(yourComand, botComand)
print("побед",win,"раз")
print("поражений",loose,"раз")
print("ничья",draw,"раз")



            
            
             
            
            
        
        


start = 12
#начальное положение робота
a = float(input("введите команду(0-продолжить движение , 1-поворот направо, -1-поворот налево"))
end = start + (a)
if -1<=a<=1:
#проверка на существование команды
    if end == 11 :
        print("робот смотрит на север")
    elif end == 12 :
        print("робот смотрит на запад")
    elif end == 13 :
        print("робот смотрит на юг")
    elif end == 14 :
        print("робот смотрит на запад восток")
else :
    print ("я же сказал, какие есть команды.Но нет, ты же самый умный")
 




a = -1
b = 0
c = 0
d = 0
p1 = 0
p2 = 0
p3 = 0
spisok = ['0','1','2','3','4','5','6','7','8','9']
spisok1 = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
while b < 1:
    parol = input("введите пароль(пароль должен содержать от 8 до 32 символов, только лат.символы,мин. 1 заглавную и одну цифру)")
    while c < 1:
        for i in parol:
            a+=1
            for i in spisok:
                if i == str(parol[a]):
                    a = 0
                    p1 = 1
                    break
        for i in parol:
            a+=1
            for i in spisok1:
                if i == str(parol[a]):
                    a = 0
                    p2 = 1
                    break
        for i in parol:
            d+=1
        if d >= 8 and d <= 32:
            p3 = 1
        if p1 == p2 == p3 == 1:
            parol2 = input("повторите свой пароль")
            if parol == parol2:
                print("пароль одобрен")
                b=1
                break
            else :
                print("пароли не совпадают")
                break
        else:
            print("пароль не коректен")
            break

    

a = int(input("введите число:"))
b = a//1000
one = b//100
two = b%11
three = b%10
c = a%1000
four = c//100
five = c%11
six = c%10
end = 0
if 3<one<8:
    end+=1
if 3<two<8:
    end+=1
if 3<three<8:
    end+=1
if 3<four<8:
    end+=1
if 3<five<8:
    end+=1
if 3<six<8:
    end+=1
print(end)

#a
print("пробег лыжника за 10 дней / условие а")
a=10.0
for i in range(10):
    print(i+1,"день  =", a,"км")
    a=a+a*0.1
#б
print("       ")
print("суммарный путь за 7 дней / условие б")
a=10.0
b=0
for i in range(7):
    i+=1
    a=a+a*0.1
    b+=a
print(b)
#в
print("       ")
print("суммарный путь за n дней / условие в")
n = int(input("кол-во дней:"))
for i in range(n):
    i+=1
    a=a+a*0.1
    b+=a
print(b)
#г
print("       ")
print("в какой день ему следует прекратить увеличивать пробег,")
print("если он не должен превышать 80 км? / условие г")
a = 10
n = 0
while a<=80:
    n+=1
    a=a+a*0.1
print("на", n,"день он должен прекратить увеличевать пробег")

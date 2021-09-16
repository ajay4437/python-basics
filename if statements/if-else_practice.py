a=int(input("entert the number: "))
b=int(input("entert the number: "))
c=int(input("entert the number: "))
d=int(input("entert the number: "))
if(a>b and a>c and a>d):
    print('the greatest number is:', a)
elif(b>a and b>c and b>d):
    print(b)
elif(c>a and c>b and c>d):
    print(c)
else:
    print(d)

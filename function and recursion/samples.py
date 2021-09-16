def function(a):
    percentage= (a[0]+a[1]+a[2]+a[3])/400*100
    return percentage
marks=[99,98,97,96]
result=function(marks)
print(result)

#2
def greet(name):
    print('good day, '+ name)
greet('ajay')

#3
def mysum(num1, num2):
    sum=(num1+num2)
    return sum
num1=int(input())
num2=int(input())
a=mysum(num1,num2)
print(a)
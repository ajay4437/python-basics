#factorial: (no recursion )
def factorial(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product
num=int(input('enter the number: '))
print(factorial(num))

#2 factorial using recursion: n!=n*(n-1)
def factorial(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product
def factorial_recursion(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursion(n-1)
num=int(input('enter the number: '))
print(factorial(num))

#or simply recursion can be easy done as:
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("enter the number: "))
print(factorial(n))   

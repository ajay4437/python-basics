#1 maximum of 3 numbers:
def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    else:
        return n3
n1=int(input('enter the number: '))
n2=int(input('enter the number: '))
n3=int(input('enter the number: '))
print(greatest(n1,n2,n3))

#2 celcius to faherinhet:
# F=1.8c+32
def farenheit(c):
    return ((1.8)*c)+32
c=int(input('enter the degree celcius: '))
f=farenheit(c)
print(f)

#3 sum of n natural numbers:
def addition(n):
    add=0
    for i in range(1,(n+1)):
        add=add+i
        i=i+1
    return add
n=int(input('enter the number: '))
print(addition(n))

#4 sum of n natural numbers using recursion:
def sum(n):
    add=0
    for i in range(1,(n+1)):
        add=add+i
    return add
def sum_rec(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
n=10
print(sum_rec(10))

#5 pattern:
def pattern(n):
    for i in range(n):
        print('*'*(n-i))

n=int(input('enter the number: '))
print(pattern(n))

#6 remove and strip:
string='    ajay is good    '
def remove_strip(word):
    new_string=string.replace(word,'')
    return new_string.strip()
word=input('enter the word: ')
print(remove_strip(word))

#7 print table:
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
n=int(input('enter the number: '))
print(table(n))
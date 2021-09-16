class Employee:
    company='google'
    salary=100

ajay=Employee()
nikki=Employee()
ajay.salary=300
nikki.salary=400
print(ajay.company)
print(nikki.company)
Employee.company='Youtube'
print(ajay.company)
print(nikki.company)
print(ajay.salary)
print(nikki.salary)
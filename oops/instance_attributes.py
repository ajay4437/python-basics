class Employee:
    company='google' 
    salary=100 #class attribute

ajay=Employee()
nikki=Employee()
#these are instance attributes.
#ajay.salary=300
#nikki.salary=400
print(ajay.salary)
print(nikki.salary)
#due to instance attribute are commented out
#salary was 100 

#ajay.attribute----> 1.instance attribute or object attribute  (if not there it choose 2)
#                    2.class attribute

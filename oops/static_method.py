class Employee:
    company='Google'
    
    def getsalary(self,signature):
        print(f"salary for this employee working in {self.company} is  {self.salary}\n{signature}")

    @staticmethod # this method doesnot requried any  or parameter , such as 'self' in the above 
    def greet():
        print('good morning, sir!')

ajay=Employee()
ajay.salary=100000
ajay.getsalary('Thanks!') #-->this will work as--->  #Employee.getsalary(ajay) 
ajay.greet()   #Employee.greet() 
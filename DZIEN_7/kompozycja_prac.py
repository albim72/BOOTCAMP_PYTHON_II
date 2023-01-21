class Employee:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def emp_data(self):
        print(f'imię pracownika: {self.name}')
        print(f'wiek pracownika: {self.age}')
        
        
class Data:
    def __init__(self,address,salary,emp_obj):
        self.address = address
        self.salary = salary
        self.emp_obj = emp_obj
        
    def display(self):
        self.emp_obj.emp_data()
        print(f"adres zamieszkania pracownika: {self.address}")
        print(f"wyskość sprzdaży: {self.salary} zł")

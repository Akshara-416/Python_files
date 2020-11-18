# Creates the Employee superclass and initializes the attributes
# This ia the Parent class
class Employee:
    
    emp_id = 1
    #Adding initial comments    
    def __init__(self, name, age, salary, designation):
        
        self.__empid = Employee.emp_id
        Employee.emp_id = Employee.emp_id + 1
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__designation = designation
    
    def set_empid(self, empid):
         self.__empid = empid
    
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age
    
    def set_salary(self, salary):
        self.__salary = salary
    
    def set_designation(self, designation):
        self.__designation = designation
        
    def get_empid(self):
        return self.__empid
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_salary(self):
        return self.__salary
    
    def get_designation(self):
        return self.__designation
    
    def get_details(self):
        
        #Print statements using print format
        print("Employee ID: {}".format(self.get_empid()))
        print("Employee Name: {}".format(self.get_name()))
        print("Employee Age: {}".format(self.get_age()))
        print("Employee Salary: {}".format(self.get_salary()))
        print("Employee Designation: {}".format(self.get_designation()))
        
    def calculate_new_salary(self, percent):
        
        increment = (percent*self.get_salary())/100
        new_salary = self.get_salary()+increment
        return new_salary

class Manager(Employee):
    
    designation = "Manager"
    
    #Dictionary to store bonus for each level
    manager_bonus = {"Level 1": 10, "Level 2":20, "Level 3":30}
    def __init__(self, name, age, salary, level):
        
        super().__init__(name, age, salary, Manager.designation)
        self.__level = level
        
    def set_level(self,level):
        self.__level = level
        
    def get_level(self):
        return self.__level
    
    #Fetching the bonus from the static variable using DICTIONARY operations
    def get_bonus(self):
        
        
        if self.get_level() == "Level 1":
            bonus = Manager.manager_bonus["Level 1"]
        elif self.get_level() == "Level 2":
            bonus = Manager.manager_bonus["Level 2"]
        elif self.get_level() == "Level 3":
            bonus = Manager.manager_bonus["Level 3"]
        else:
            bonus = 50
        return bonus
    
    #Method overriding
    def calculate_new_salary(self, percent):
        
        manger_bonus = self.get_bonus
        increment = (percent*self.get_salary())/100
        new_salary = self.get_salary()+increment+manger_bonus
        
        return new_salary

class Department:
    
    def __init__(self, emp_list, dept_id, dept_name):
        
        self.__emp_list = emp_list
        self.__dept_id = dept_id
        self.__dept_name = dept_name
        
    def get_emp_list(self):
        return self.__emp_list
    
    def get_dept_id(self):
        return self.__dept_id
    
    def get_dept_name(self):
        return self.__dept_name
    
    def get_employees(self):
        
        #Fetching names of employee in the department using LIST operations
        employee_names = []
        for employee in self.get_emp_list():
            name = employee.get_name()
            employee_names.append(employee)
            
        return employee_names

# imports employee class
#import employee

# Main function
def main():
    
    dev_emp_list = []
    test_emp_list = []
    hr_emp_list = []
    
    #Using List operations
    employee_list = make_employeelist()
    manager_list = make_managerlist()
    
    for employee in employee_list:
        if employee.get_designation() in ["SSE","SE"]:
            dev_emp_list.append(employee)
        elif employee.get_designation() in ["TEST_ENGINEER"]:
            test_emp_list.append(employee)
        else:
            hr_emp_list.append(employee)
    
    
    dev_dept = Department(dev_emp_list, 1, "DEVELOPMENT")  
    test_dept = Department(test_emp_list, 2, "TESTING")
    hr_dept = Department(hr_emp_list, 3, "HR")
    
    
def make_employeelist():
    
    #Using List operations
    employee_list = []
    count = int(input("Please Enter the Number of Employees:"))
    
    for i in range(count):
        name = input("Enter the Name of Employee:")
        age = input("Enter the Age:")
        salary = input("Enter the Salary:")
        designation = input("Enter the designation:")

        emp = Employee(name,age,salary,designation)
        employee_list.append(emp)
    
    return employee_list

def make_managerlist():

    #Using List operations
    manager_list = []
    count = int(input("Please Enter the Number of Managers:"))
    
    for i in range(count):
        name = input("Enter the Name of Manager:")
        age = input("Enter the Age:")
        salary = input("Enter the Salary:")

        mgr = Manager(name,age,salary)
        manager_list.append(mgr)
    -
    return manager_list

main()





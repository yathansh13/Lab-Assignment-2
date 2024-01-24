class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t\t{self.name}\t{self.age}\t{self.salary}"

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=self.get_age)
        elif key == 2:
            self.employees.sort(key=self.get_name)
        elif key == 3:
            self.employees.sort(key=self.get_salary)

    def get_age(self, emp):
        return emp.age

    def get_name(self, emp):
        return emp.name

    def get_salary(self, emp):
        return emp.salary

    def print_table(self):
        print("Employee ID\tName\tAge\tSalary")
        for emp in self.employees:
            print(emp)


emp1 = Employee("161E90", "Ramu", 35, 59000)
emp2 = Employee("171E22", "Tejas", 30, 82100)
emp3 = Employee("171G55", "Abhi", 25, 100000)
emp4 = Employee("152K46", "Jaya", 32, 85000)

employees_list = [emp1, emp2, emp3, emp4]

emp_table = EmployeeTable(employees_list)

print("Choose a sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")


sorting_key = int(input("Enter your choice: "))
if sorting_key >3 or sorting_key<1:
    print("Invalid Sorting key")
    exit()

emp_table.sort_employees(sorting_key)
print("\nSorted Employee Table:\n")
emp_table.print_table()


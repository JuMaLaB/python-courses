from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("My employees are:")
        for e in self.employees:
            print(e.fname, e.lname)
        print("--------------")

    def display_paycheck(self):
        print("My employees paycheck:")
        for e in self.employees:
            print("name:", e.fname, e.lname)
            print(f"amout: ${e.caluclate_paycheck():,.2f}")
            print("--------------")
          
          
def main():
        my_company = Company()

        employee1 = SalaryEmployee('Ju', 'Malab', 30000)
        employee2 = SalaryEmployee('Bourk', 'Malab', 20000)

        employee3 = HourlyEmployee('Harry', 'Potter', 12, 55)
        employee4 = HourlyEmployee('Micheal', 'Jackson', 11, 666)

        employee5 = CommissionEmployee('Zinzin', 'Space', 22000, 9, 33)
        employee6 = CommissionEmployee('Tonton', 'Disco', 11000, 66, 11)

        my_company.add_employee(employee1)
        my_company.add_employee(employee2)
        my_company.add_employee(employee3)
        my_company.add_employee(employee4)
        my_company.add_employee(employee5)
        my_company.add_employee(employee6)

        my_company.display_paycheck()

main()
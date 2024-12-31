class Employee:
    def __init__(self, first_name_val, last_name_val):
        self.fname = first_name_val
        self.lname = last_name_val
    
class SalaryEmployee(Employee):
    def __init__(self, first_name_val, last_name_val, salary_val):
        super().__init__(first_name_val, last_name_val)
        self.salary = salary_val

    def caluclate_paycheck(self):
        return self.salary/12
    
class HourlyEmployee(Employee):
    def __init__(self, first_name_val, last_name_val, weekly_hours, hourly_rate):
        super().__init__(first_name_val, last_name_val)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def caluclate_paycheck(self):
        return self.weekly_hours * self.hourly_rate
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, first_name_val, last_name_val, salary_val, sales_num, com_rate):
        super().__init__(first_name_val, last_name_val, salary_val)
        self.sales_num = sales_num
        self.com_rate = com_rate

    def caluclate_paycheck(self):
        regular_salary = super().caluclate_paycheck()
        total_com = self.sales_num * self.com_rate
        return regular_salary + total_com
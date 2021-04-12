from Employee import Employee
"""
The salaried employee that inherits from the employee class
"""


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, email, phone, employee_no, salary_amount):
        if not isinstance(salary_amount, (int, float)):
            raise TypeError('The salary can only be either an integer or a decimal value')
        self.salary_amount = salary_amount
        super().__init__(first_name, last_name, email, phone, employee_no)

    @property
    def salary_amount(self):
        return self._salary_amount

    @salary_amount.setter
    def salary_amount(self, amount):
        if amount < 0:
            raise ValueError('The salary amount cannot be less than 0')
        self._salary_amount = amount

    def calculate_net_pay(self, deductions):
        net_pay = self.salary_amount - deductions
        print(f'Employee with the identity {self.employee_no} earns a net income of {net_pay:.2f}')

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name} of identity {self.employee_no} earns a gross pay of {self.salary_amount} '


"""
Employee class that defines the Employee attributes and methods
"""


class Employee:
    def __init__(self, first_name, last_name, email, phone, employee_no):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.employee_no = employee_no
        self.employees = []  # An empty list of employees

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if len(phone) >= 10:
            raise ValueError('The phone number must not exceed 10 digits')
        self._phone = phone

    def get_employee_no(self):
        return self.employee_no

    def add_employee(self, employee_data):
        self.employees.append(employee_data)
        
    def list_employees(self):
        print(self.employees)

    def __str__(self):
        return f'The employee is {self.first_name} {self.last_name} and is identified by {self.employee_no}'


"""
The salaried employee that inherits from the employee class
"""


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, email, phone, employee_no, salary_amount):
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
        if deductions > self.salary_amount:
            return False
        net_pay = self.salary_amount - deductions
        print(f'Employee with the identity {self.employee_no} earns a net income of {net_pay:.2f}')

    def __str__(self):
        return f'Employee {self.first_name} {self.last_name} of identity {self.employee_no} earns a gross pay of {self.salary_amount} '


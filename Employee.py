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

        if len(self.phone) < 10:
            raise ValueError('The phone number must not be less than 10 characters long')

    def get_employee_no(self):
        return self.employee_no

    def add_employee(self):
        new_employee = Employee('John', 'Doe', 'john@test.com', '074534321876', 'EMP7123')
        self.employees.append(new_employee)

    def __repr__(self):
        return f'The employee is {self.first_name} {self.last_name} and is identified by {self.employee_no}'


"""
The salaried employee that inherits from the employee class
"""


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, email, phone, employee_no, salary_amount):
        super().__init__(first_name, last_name, email, phone, employee_no)
        self.salary_amount = salary_amount

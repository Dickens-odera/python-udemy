"""
Employee class that defines the Employee attributes and methods
"""


class Employee(object):
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
        if len(phone) < 10:
            raise ValueError('The phone number must not be less than 10')
        elif len(phone) > 10:
            raise ValueError('The phone number must not exceed 10 digits')
        self._phone = phone

    def get_employee_no(self):
        return self.employee_no

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def list_employees(self):
        for employee in self.employees:
            print(employee)

    def __str__(self):
        return f'The employee is {self.first_name} {self.last_name} and is identified by {self.employee_no}'


"""
    def __repr__(self):
        pass
"""

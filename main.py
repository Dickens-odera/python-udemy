from strings import *
from login import login
from Employee import *

# Working with Numbers


def calculate_result():
    print(f'2 to the power of 3 is {2**3}')
    print(f'21 modulo 2 is {21 % 2}')
    print(f'First Value {2 + 2 * 5 - 1}')
    print(f'Second value with parenthesis {(2 + 2) * (5 - 1)}')


if __name__ == '__main__':
    calculate_result()
    login()
    greetings('Dickens')
    print(index_string('Hello There Index'))
    print(slice_string('abcdefghijkl'))
    print(convert_to_upper('Hello There {first_name} {second_name} {last_name}'.format(first_name='Dickens', second_name='Ochieng', last_name='Ooko')))
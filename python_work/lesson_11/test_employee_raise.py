# practice 3/18/25
# chapter 11 - employee
# test_employee_raise.py

import pytest
from employee_11_3 import Employee

@pytest.fixture
def employee():
    employee = Employee('foo', 'bar', 50_000)
    return employee

def test_give_default_raise(employee):
    '''Test give_raise() increases salary by default amount of 5_000.'''
    employee.give_raise()
    assert employee.salary == 55_000

def test_give_custom_raise(employee):
    '''Test give_raise increases salary by a custom amount.'''
    employee.give_raise(10_000)
    assert employee.salary == 60_000
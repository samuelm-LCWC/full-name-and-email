from employee import Employee
import pytest

def test_employee():
    test_case = Employee("John", "Smith")
    assert test_case.fullname == "John Smith"
    assert test_case.email == "john.smith@company.com"
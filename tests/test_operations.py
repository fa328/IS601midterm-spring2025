'''
    The Calculation Class holds two values.
    __init__(self, a, b, operation) initilize the class
    with two number and the operation the user want them to perform.
   perform(self) executes the operation on two values. 
'''
import decimal
from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide

class Calculations: # pylint: disable=too-few-public-methods
    '''Calculation class'''
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        '''Perform the calculation'''
        return self.operation(self.a, self.b)

# Fixture to provide parameters for test_operation
@pytest.fixture
def operation_data():
    '''Operation data'''
    return [
        (Decimal('1'), Decimal('2'), add, Decimal('3')),
        (Decimal('3'), Decimal('1'), subtract, Decimal('2')),
        (Decimal('2'), Decimal('3'), multiply, Decimal('6'))
    ]

def test_operation(operation_data): # pylint: disable=redefined-outer-name
    '''Testing various operations'''
    for a, b, operation, expected in operation_data:
        calculation = Calculations(a, b, operation)
        assert calculation.perform() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(decimal.DivisionByZero):
        calculation = Calculations(Decimal('10'), Decimal('0'), divide)
        calculation.perform()

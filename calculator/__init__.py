'''
    The Calculator class offers static methods 
    for addition, subtraction, multiplication, 
    and division. CalculationsHistory keeps track of 
    past calculations, enabling addition, retrieval, and clearing of entries.
'''
# Import modules and functions for testing a calculator
import pytest # type: ignore
from calculator.calculation import Calculations
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    '''Calculator class functions to perform addition, subtraction, multiplivationa and division'''

    @staticmethod
    def add(a: float, b: float) -> float:
        '''Test that addition function works '''    
        calculation = Calculations(a, b, add)
        return calculation.get_result()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        '''Test that subtract function works '''    
        calculation = Calculations(a, b, subtract)
        return calculation.get_result()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        '''Test that multiply function works '''    
        calculation = Calculations(a, b, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(a: float, b: float) -> float:
        '''Test that divide function works '''    
        if b == 0:
            return "Error: Division by zero"
        return Calculations(a, b, divide).get_result()

class CalculationsHistory:
    '''To store the calculator history'''
    history = []

    @classmethod
    def add_history(cls, calculation: float):
        '''Performs addition, subtraction, multiplication, division'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls):
        '''To get the history of calculations'''
        return cls.history

    @classmethod
    def clear_history(cls):
        '''Use to clears the history'''
        cls.history = []

calc = Calculator()
result = calc.add(2, 2)
CalculationsHistory.add_history(result)
print(CalculationsHistory.get_history())

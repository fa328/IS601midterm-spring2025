'''
    The code is check the add, subtract, 
    multipy and divide function and correclty 
    (add, subtract, multipy and divide) one number by another.
    The history of the calculations is store in the CalculationHistory.
'''
from calculator import add, subtract, multiply, divide, Calculator, CalculationsHistory

def test_addition():
    '''Test that addition function works '''    
    assert add(2, 2) == 4

def test_subtraction():
    '''Test that subtract function works '''    
    assert subtract(2, 2) == 0

def test_multiplication():
    '''Test that multiply function works'''
    assert multiply(2, 2) == 4

def test_division():
    '''Test that division function works'''
    assert divide(2, 2) == 1

# Calculator and CalculationsHistory
calc = Calculator()
result = calc.add(2, 2)
CalculationsHistory.add_history(result)
print(CalculationsHistory.get_history())

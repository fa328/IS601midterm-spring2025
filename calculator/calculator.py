'''
    It add. subract, multiply and divide two number using an add function, 
    which passed to the calculation class as the operation.
    
'''
def add(a: float, b: float) -> float:
    '''add function'''
    return a + b

def subtract(a: float, b: float) -> float:
    '''subtract function'''
    return a - b

def multiply(a: float, b: float) -> float:
    '''multiply fuction'''
    return a * b

def divide(a: float, b: float) -> float:
    '''Returns the result of dividing the first number by the second'''
    if b == 0:
        return "Error: Division by zero"
    return a / b

'''
    Calculations class performs basic operation using a passed function.
    It add two number using an add function, which passed to the calculation class as the operation.

'''
class Calculations:  # pylint: disable=too-few-public-methods
    '''Calculations functions'''

    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        '''Get result of the operation'''
        return self.operation(self.a, self.b)

def add(a, b):
    '''Addition function'''
    return a + b


calc = Calculations(2, 2, add)
print(calc.get_result())

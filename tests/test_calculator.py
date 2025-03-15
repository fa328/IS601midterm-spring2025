'''
    The code is check the add, subtract, 
    multipy and divide function and correclty 
    (add, subtract, multipy and divide) one number by another.
    The history of the calculations is store in the CalculationHistory.
'''
import pandas as pd
from calculator import add, subtract, multiply, divide, Calculator, CalculationsHistory

def log_to_csv(operation, operand1, operand2, result):
    """Logs the calculation to a CSV file using Pandas."""
    data = {
        'operation': [operation],
        'operand1': [operand1],
        'operand2': [operand2],
        'result': [result]}
    df = pd.DataFrame(data)

    # Append to the existing CSV file or create a new one if it doesn't exist
    try:
        existing_df = pd.read_csv('calculations_history.csv')
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass

    # Save the updated Data to CSV
    df.to_csv('calculations_history.csv', index=False)

def test_addition():
    """Test that addition function works.""" 
    addition_test_result = add(2, 2)
    assert addition_test_result == 4
    log_to_csv('add', 2, 2, addition_test_result)

def test_subtraction():
    """Test that subtract function works."""
    subtraction_result = subtract(2, 2)
    assert subtraction_result == 0
    log_to_csv('subtract', 2, 2, subtraction_result)

def test_multiplication():
    """Test that multiply function works."""
    multiplication_result = multiply(2, 2)
    assert multiplication_result == 4
    log_to_csv('multiply', 2, 2, multiplication_result)

def test_division():
    """Test that division function works."""
    # pylint: disable=redefined-outer-name
    division_result = divide(2, 2)
    assert division_result == 1
    log_to_csv('divide', 2, 2, division_result)

# Calculator and CalculationsHistory
calc = Calculator()
calculator_addition_result = calc.add(2, 2)  # Renamed the variable
CalculationsHistory.add_history(calculator_addition_result)

# Log the calculation to CSV
log_to_csv('add', 2, 2, calculator_addition_result)

# Print the history of calculations
history_df = pd.read_csv('calculations_history.csv')
print(history_df)

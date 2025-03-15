'''Main.py'''
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator
from app import App

def calculate_and_print(a, b, operation_name):
    '''calculate and print function'''
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])

        # if operation is not valid, print error
        operation = operation_mappings.get(operation_name)
        if operation:
            result = operation(a_decimal, b_decimal)
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except (ValueError, KeyError) as e:  # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    '''Main function'''
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    # Operation
    _, a, b, operation = sys.argv

    # Call the calculate and print function
    calculate_and_print(a, b, operation)

    # Initialize and start the app
    app = App()
    app.start()

if __name__ == '__main__':
    main()

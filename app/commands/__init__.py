'''Command App'''
from abc import ABC, abstractmethod
from calculator import add, subtract, multiply, divide

class Command(ABC): # pylint: disable=too-few-public-methods
    '''command function'''
    @abstractmethod
    def execute(self):
        '''execute function'''


class CommandHandler:
    '''CommandHandler'''
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        '''Register Command'''
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        #Easier to ask for forgiveness than permission
        # (EAFP) - Use when its going to most likely work
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

# add, subtract, multiply, and divide Command Classes
class AddCommand(Command): # pylint: disable=too-few-public-methods
    '''Add Command'''
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self):
        #add is now a using function in calculator.py
        result = add(self.a, self.b)
        print(f"Result: {result}")

class SubtractCommand(Command): # pylint: disable=too-few-public-methods
    '''Subtract Command'''
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self):
        #Subtract is now a using function in calculator.py
        result = subtract(self.a, self.b)
        print(f"Result: {result}")

class MultiplyCommand(Command): # pylint: disable=too-few-public-methods
    '''Multiply Command'''
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self):
        # multiply is now a using function in calculator.py
        result = multiply(self.a, self.b)
        print(f"Result: {result}")

class DivideCommand(Command): # pylint: disable=too-few-public-methods
    '''Divide Command'''
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def execute(self):
        # divide is now a using function in calculator.py
        if self.b == 0:
            print("Error: Division by zero")
        else:
            result = divide(self.a, self.b)
            print(f"Result: {result}")

class MenuCommand(Command):  # pylint: disable=too-few-public-methods
    '''Menu Command'''
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        print("\nMenu Commands:")
        for command in self.command_handler.commands:
            print(command)

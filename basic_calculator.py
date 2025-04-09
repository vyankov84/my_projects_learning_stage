class Calculator():
    """
    A simple calculator class that can perform basic arithmetic operations.
    """

    def __init__(self, x:float, y:float, operator:str):
        """
        Initialize the calculator with two numbers and an operator.
        :param x: First number (float)
        :param y: Second number (float)
        :param operator: Arithmetic operator as a string (+, -, *, /)
        """
        self.x = x
        self.y = y
        self.operator = operator
        self.result = None

    def add_func(self):
        """Performs addition."""
        self.result = self.x + self.y

    def subtract_func(self):
        """Performs subtraction."""
        self.result = self.x - self.y

    def multiply_func(self):
        """Performs multiplication."""
        self.result = self.x * self.y

    def divide_func(self):
        """Performs division and handles division by zero"""
        if self.y == 0:
            print('Can\'t divide by Zero')
            self.result = None
        else:
           self.result = self.x / self.y

    def calculate(self):
        """
        Calls the appropriate function based on the operator.
        """
        if self.operator == '+':
            self.add_func()
        elif self.operator == '-':
            self.subtract_func()
        elif self.operator == '*':
            self.multiply_func()
        elif self.operator == '/':
            self.divide_func()
        else:
            print('Invalid operator')

    def __repr__(self):
        """
        Return a formated string or a message if there's no result
        """
        if self.result is None:
            return f'No result'
        elif self.result == int(self.result):
            return f'Result: {self.x} {self.operator} {self.y} = {int(self.result)}'
        else:
            return f'Result: {self.x} {self.operator} {self.y} = {self.result:.2f}'


def main():
    """Handles user input and control the calculator loop"""

    print('Welcome to Basic Calculator')

    while True:
        try:
            first_num = float(input('Please enter the first number:\n= '))
            second_num = float(input('Please enter the second number:\n= '))
        except ValueError:
            print('You need to enter valid number!!!')
            continue

        operator = input('Please enter the operation (+,-,*,/): ').strip()

        if operator in ['+','-','*','/']:
            calc = Calculator(first_num, second_num, operator)
            calc.calculate()
            print(calc)
        else:
            print('Not a valid operator (+,-,*,/)!!!')
            continue

        new_calculation = input('New calculation? (Y/N): ').lower()

        if new_calculation in ['n','no']:
            print('Goodbye!👋')
            break

if __name__ == '__main__':
    main()
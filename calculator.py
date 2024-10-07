from collections import deque


class Expression:
    def apply(self, left: int, right: int):
        pass


class Add(Expression):
    def apply(self, left, right):
        return left + right


class Subtract(Expression):
    def apply(self, left, right):
        return right - left


class Multiply(Expression):
    def apply(self, left, right):
        return left * right


class Divide(Expression):
    def apply(self, left, right):
        return right / left


class LeftParenthesis(Expression):

    def apply(self, left: int, right: int):
        pass


class Power(Expression):
    def apply(self, left: int, right: int):
        return right ** left


if __name__ == '__main__':

    while True:
        inp = input('''Enter expression in enclosing parenthesis and separated by whitespaces (e.g. ( ( 2 + 2 ) * 2)
                        For exit enter \'exit\'\n''')
        if inp == 'exit':
            print("Good Bye! ")
            exit(0)

        operator_stack: deque[Expression] = deque()
        values_stack: deque[int] = deque()
        for ch in inp.split(' '):
            if ch.isdigit():
                values_stack.append(int(ch))
            elif ch == '+':
                operator_stack.append(Add())
            elif ch == '-':
                operator_stack.append(Subtract())
            elif ch == '*':
                operator_stack.append(Multiply())
            elif ch == '/':
                operator_stack.append(Divide())
            elif ch == '^':
                operator_stack.append(Power())
            elif ch == '(':
                operator_stack.append(LeftParenthesis())
            elif ch == ')':
                operator = operator_stack.pop()
                while not isinstance(operator, LeftParenthesis):
                    values_stack.append(operator.apply(values_stack.pop(), values_stack.pop()))
                    operator = operator_stack.pop()

        print(f'result = {values_stack.pop()}')

# dz7-3

class Square:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат {self.quantity * "*"}'

    def __add__(self, other):
        return Square(self.quantity + other.quantity)

    def __sub__(self, other):

        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Минус')

    def __mul__(self, other):
        return Square(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Square(round(self.quantity // other.quantity))

    def make_order(self, square_in_row):
        row = ''
        for i in range(int(self.quantity / square_in_row)):
            row += f'{"*" * square_in_row} \\n'
        row += f'{"*" * (self.quantity % square_in_row)}'
        return row

square1 = Square(42)
square2 = Square(18)
print(square1)
print(square1 + square2)
print(square2 - square1)
print(square2.make_order(14))
print(square1.make_order(19))
print(square1 / square2)
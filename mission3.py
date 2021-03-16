class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Слияние двух клеток: {self.quantity + other.quantity}'

    def __sub__(self, other):
        try:
            if self.quantity - other.quantity <= 0:
                raise ValueError
            else:
                return f'Уменьшение клетки: {self.quantity - other.quantity}'
        except ValueError:
            print('Операция не может быть выполнена')

    def __mul__(self, other):
        return f'Создание общей клетки: {self.quantity * other.quantity}'

    def __truediv__(self, other):
        return f'Почкование клетки: {self.quantity // other.quantity}'

    def make_order(self, row):
        ordered = ['*' * row for _ in range(self.quantity // row)]
        ordered.append('*' * (self.quantity % row))
        return f'\n'.join(ordered)


cell_1 = Cell(8)
cell_2 = Cell(6)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print()
print(cell_2.make_order(5))
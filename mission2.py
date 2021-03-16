from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def max_area(self):
        return f'Площадь используемой ткани: {(self.param / 6.5 + 0.5) + (2 * self.param + 0.3)}'

    @abstractmethod
    def abstractmethod(self):
        pass


class Coat(Clothes):
    def __init__(self, param):
        super(Coat, self).__init__(param)

    def max_area(self):
        return f'Ткань для пальто: {self.param / 6.5 + 0.5:.2f}'

    def abstractmethod(self):
        pass


class Suit(Clothes):
    def __init__(self, param):
        super(Suit, self).__init__(param)

    def max_area(self):
        return f'Ткани для костюма: {2 * self.param + 0.3:.2f}'

    def abstractmethod(self):
        pass

coat = Coat(7)
suit = Suit(9)
print(coat.max_area())
print(suit.max_area())
# dz7-2

class Clothes:
    def __init__(self, vvv, hhh):
        self.vvv = vvv
        self.hhh = hhh

    def get_cost_coat(self):
        return self.vvv / 6.5 + 0.5

    def get_cost_suit(self):
        return self.hhh * 2 + 0.3
    @property
    def get_cost_all(self):
        return str(f'Общий расход \n'
                   f' {(self.vvv / 6.5 + 0.5) + (self.hhh * 2 + 0.3)}')

class Coat(Clothes):
    def __init__(self, vvv, hhh):
        super().__init__(vvv, hhh)
        self.cost_coat = round(self.vvv/ 6.5 + 0.5)

    def __str__(self):
        return f'Расход на пальто {self.cost_coat}'

class Jacket(Clothes):
    def __init__(self, vvv, hhh):
        super().__init__(vvv, hhh)
        self.cost_suit = round(self.hhh * 2 + 0.3)

    def __str__(self):
        return f'Расход на костюм {self.cost_suit}'

coat = Coat(9, 9)
jacket = Jacket(8, 8)
print(coat)
print(jacket)
print(coat.get_cost_all)
print(jacket.get_cost_all)
print(jacket.get_cost_coat())
print(jacket.get_cost_suit())

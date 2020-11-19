# TODO:priceは保持しない
#      price表みたいなのを自販機が持っているはず

class Drink():
    def __init__(self, name : str, price : int):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - ¥{self.price}'

class Water(Drink):
    def __init__(self):
        super(Water, self).__init__('水', 100)


class Cola(Drink):
    def __init__(self):
        super(Cola, self).__init__('コーラ', 150)


class Tea(Drink):
    def __init__(self):
        super(Tea, self).__init__('お茶', 130)


if __name__ == '__main__':

    for d in [Water(), Cola(), Tea()]:
        print(d)
# TODO:priceは保持しない
#      price表みたいなのを自販機が持っているはず

class Drink():
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name}'

class Water(Drink):
    def __init__(self):
        super(Water, self).__init__('水')


class Cola(Drink):
    def __init__(self):
        super(Cola, self).__init__('コーラ')


class Tea(Drink):
    def __init__(self):
        super(Tea, self).__init__('お茶')


if __name__ == '__main__':

    for d in [Water(), Cola(), Tea()]:
        print(d)
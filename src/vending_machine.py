class VendingMachine():

    def __init__(self):
        self.stocks = {}


    def AddDrink(self, drink):

        # 当たり付きドリンクがあるかもしれないので、
        # あえてインスタンスとして保持する
        if drink.name in self.stocks:
            self.stocks[drink.name].append(drink)
        else:
            self.stocks[drink.name] = [drink]

    def Exchange(self, drink_name : str, input_amount : int):
        pass

    def __CalcCahnge(self):
        pass
        

    def __PopDrink(self, drink):
        pass

    def DisplayStock(self):
       
        for k, v in self.stocks.items():
            print(k, len(v))

        
